import csv
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class AnaliseVendas:
    def __init__(self, nome_arquivo):
        # Caminho absoluto baseado no arquivo .py
        base_dir = os.path.dirname(__file__)
        self.caminho_arquivo = os.path.join(base_dir, nome_arquivo)
        self.dados = []

    def ler_csv(self):
        # Limpa a lista antes de carregar novamente
        self.dados = [] 

        if not os.path.exists(self.caminho_arquivo):
            print("Erro: arquivo não encontrado!")
            return

        with open(self.caminho_arquivo, 'r', encoding='utf-8-sig') as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=',')

            if leitor.fieldnames is None:
                print("Erro: CSV vazio ou inválido.")
                return

            print("Colunas detectadas:", leitor.fieldnames)

            for linha in leitor:
                try:
                    self.dados.append({
                        'produto': linha['produto'],
                        'categoria': linha['categoria'],
                        'preco': float(linha['preco']),
                        'quantidade': int(linha['quantidade']),
                        'data': linha['data']
                    })
                except:
                    print("Linha inválida ignorada:", linha)

    def calcular_media(self):
        if not self.dados:
            return 0
        precos = [item['preco'] for item in self.dados]
        return sum(precos) / len(precos)

    def maior_preco(self):
        if not self.dados:
            return 0
        return max(item['preco'] for item in self.dados)

    def menor_preco(self):
        if not self.dados:
            return 0
        return min(item['preco'] for item in self.dados)

    def faturamento_total(self):
        total = 0
        for item in self.dados:
            total += item["preco"] * item['quantidade']
        return total

    def faturamento_categoria(self):
        resultado = {}

        for item in self.dados:
            categoria = item["categoria"]
            total = item['preco'] * item['quantidade']

            if categoria not in resultado:
                resultado[categoria] = 0

            resultado[categoria] += total

        return resultado
    
    def filtrar_data(self, data_busca):
        resultado = []

        for item in self.dados:
            if item['data'] == data_busca:
                resultado.append(item)

        return resultado

    def dia_maior_faturamento(self):
        faturamento_por_dia = {}

        for item in self.dados:
            data = item['data']
            total = item['preco'] * item['quantidade']

            if data not in faturamento_por_dia:
                faturamento_por_dia[data] = 0

            faturamento_por_dia[data] += total

        melhor_dia = max(faturamento_por_dia, key=faturamento_por_dia.get)

        return melhor_dia, faturamento_por_dia[melhor_dia]

    def ranking_produtos(self):
        ranking = {}

        for item in self.dados:
            produto = item['produto']
            total = item['preco'] * item['quantidade']

            if produto not in ranking:
                ranking[produto] = 0

            ranking[produto] += total

        ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

        return ranking_ordenado
    
    def gerar_relatorio(self, nome_arquivo = "relatorio_vendas.pdf"):
        doc = SimpleDocTemplate(nome_arquivo)
        styles = getSampleStyleSheet()
        elementos = []

        elementos.append(Paragraph("Relatório de vendas", styles['Title']))
        elementos.append(Spacer(1, 12))

        total = self.faturamento_total()
        elementos.append(Paragraph(f"Faturamento Total: R$ {total}", styles['Normal']))
        elementos.append(Spacer(1, 12))

        elementos.append(Paragraph("Faturamento por Categoria: ", styles['Heading2']))
        for categoria, valor in self.faturamento_categoria().items():
            elementos.append(Paragraph(f"{categoria}: R$ {valor}", styles['Normal']))
        elementos.append(Spacer(1, 12))

        dia, valor = self.dia_maior_faturamento()
        elementos.append(Paragraph(f"Dia com maior faturamento: {dia} (R$ {valor})", styles['Normal']))
        elementos.append(Spacer(1, 12))

        elementos.append(Paragraph("Ranking de Produtos: ", styles['Heading2']))
        ranking = self.ranking_produtos()

        for i, (produto, valor) in enumerate(ranking, start=1):
            elementos.append(Paragraph(f"{i}º {produto} - R$ {valor}", styles['Normal']))

        doc.build(elementos)

        print(f"Relatório gerado com sucesso: {nome_arquivo}")

    def enviar_email(self, destinatario, arquivo_pdf="relatorio_vendas.pdf"):
        import os.path
        import base64
        from email.message import EmailMessage

        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build

        SCOPES = ['https://www.googleapis.com/auth/gmail.send']

        creds = None

        #Token salvo (evita login toda hora)
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES
                )
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())
            
        service = build('gmail', 'v1', credentials=creds)

        message = EmailMessage()
        message.set_content('Segue o relatório de vendas em anexo.')
        message['To'] = destinatario
        message['From'] = "me"
        message['Subject'] = "Relatório de Vendas"

        with open(arquivo_pdf, 'rb') as f:
            message.add_attachment(
                f.read(),
                maintype = 'application',
                subtype = 'pdf',
                filename = arquivo_pdf
            )
        
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

        service.users().messages().send(
            userId = 'me',
            body = {'raw': raw}
        ).execute()

        print("Email enviado com sucesso!")


caminho = "dados_vendas.csv"
analisador = AnaliseVendas(caminho)
analisador.ler_csv()

while True:
    print('''
        ANÁLISE DE VENDAS DE PRODUTOS
          
        (1) - Calcular Média de vendas
        (2) - Calcular Maior valor de venda
        (3) - Calcular Menor valor de venda
        (4) - Faturamento total
        (5) - Faturamento por categoria
        (6) - Filtrar por data
        (7) - Dia com maior faturamento
        (8) - Ranking de Produtos
        (9) - Gerar Relatório
        (10) - Enviar relatório por email
        (0) - Sair
    ''')

    operador = input("Escolha: ")

    match operador:
        case "1":
            print("Média: ", analisador.calcular_media())
        case "2":
            print("Maior: ", analisador.maior_preco())
        case "3":
            print("Menor: ", analisador.menor_preco())
        case "4":
            print("Faturamento total: ", analisador.faturamento_total())
        case "5":
            resultado = analisador.faturamento_categoria()
            for categoria, total in resultado.items():
                print(f"{categoria}: R$ {total}")
        case "6":
            data = input("Digite a data (YYYY-MM-DD): ")
            resultado = analisador.filtrar_data(data)

            for item in resultado:
                print(item)
        case "7":
            dia, total = analisador.dia_maior_faturamento()
            print(f"Melhor dia: {dia} com faturamento de R$ {total}")
        case "8":
            ranking = analisador.ranking_produtos()

            for i, (produto, total) in enumerate(ranking, start=1):
                print(f"{i}º {produto} - R$ {total}")
        case "9":
            analisador.gerar_relatorio()
        case "10":
            email = str(input("Digite o e-mail destinatário: "))
            analisador.gerar_relatorio()
            analisador.enviar_email(email)
        case "0":
            print("Encerrando...")
            break
        case _:
            print("Operação Inválida")