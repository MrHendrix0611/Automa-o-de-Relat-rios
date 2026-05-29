# 📊 Sistema de Automação para Análise de Vendas

Sistema completo de análise de vendas desenvolvido em Python.

O projeto realiza:

* Leitura de arquivos CSV
* Processamento de dados de vendas
* Cálculos estatísticos
* Geração automática de relatórios PDF
* Envio automático de relatórios por e-mail

Tudo através de um menu interativo no terminal.

---

# 🚀 Funcionalidades

✅ Leitura automática de arquivos CSV
✅ Cálculo de média de vendas
✅ Identificação do maior e menor valor
✅ Cálculo de faturamento total
✅ Faturamento por categoria
✅ Filtro de vendas por data
✅ Descoberta do melhor dia de vendas
✅ Ranking de produtos
✅ Geração automática de relatório PDF
✅ Envio automático de relatório por e-mail
✅ Tratamento de erros em arquivos CSV

---

# 🧠 Tecnologias Utilizadas

* Python
* CSV
* ReportLab
* Gmail API
* OAuth 2.0
* EmailMessage
* Programação Orientada a Objetos (POO)

---

# 📂 Estrutura do Projeto

```bash
ANALISE_VENDAS/
│
├── dados_vendas.csv
├── credentials.json
├── token.json
├── relatorio_vendas.pdf
├── main.py
│
└── README.md
```

---

# 📋 Como o Sistema Funciona

O sistema segue o seguinte fluxo:

```text
CSV de vendas
      ↓
Leitura e processamento
      ↓
Análise estatística
      ↓
Relatório PDF
      ↓
Envio automático por e-mail
```

---

# 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/MrHendrix0611/Automa-o-de-Relat-rios.git
```

Entre na pasta:

```bash
cd  Automa-o-de-Relat-rios  
```

Instale as dependências:

```bash
pip install reportlab google-auth google-auth-oauthlib google-api-python-client
```

---

# 📄 Estrutura do CSV

O arquivo CSV deve possuir as seguintes colunas:

```csv
produto,categoria,preco,quantidade,data
Notebook,Eletrônicos,3500,2,2025-05-10
Mouse,Periféricos,120,5,2025-05-10
```

---

# ▶️ Executando o Projeto

```bash
python main.py
```

---

# 🖥️ Menu do Sistema

```text
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
```

---

# 📊 Análises Disponíveis

## Média de vendas

Calcula a média dos preços cadastrados.

---

## Maior e menor valor

Identifica:

* Produto mais caro
* Produto mais barato

---

## Faturamento total

Calcula:

```python
preço × quantidade
```

para todos os produtos.

---

## Faturamento por categoria

Exemplo:

```text
Eletrônicos: R$ 12000
Periféricos: R$ 2500
```

---

## Melhor dia de vendas

Identifica qual data teve o maior faturamento.

---

## Ranking de Produtos

Ordena os produtos pelo faturamento total.

Exemplo:

```text
1º Notebook - R$ 7000
2º Monitor - R$ 5000
```

---

# 📄 Geração de Relatórios PDF

O sistema gera automaticamente um PDF contendo:

* Faturamento total
* Faturamento por categoria
* Melhor dia de vendas
* Ranking de produtos

Biblioteca utilizada:

```python
ReportLab
```

---

# 📧 Envio Automático por E-mail

O projeto integra com a API do Gmail para envio automático de relatórios.

## Funcionalidades

✅ Anexo automático do PDF
✅ Autenticação OAuth 2.0
✅ Envio direto pelo Gmail

---

# 🔐 Configuração da Gmail API

Para utilizar o envio de e-mails:

1. Acesse:

   * Google Cloud Console

2. Ative:

   * Gmail API

3. Gere o arquivo:

```text
credentials.json
```

4. Coloque o arquivo na raiz do projeto.

Na primeira execução será gerado:

```text
token.json
```

---

# 🧪 Conceitos Aplicados

Este projeto utiliza conceitos importantes de programação:

* Programação Orientada a Objetos
* Manipulação de arquivos CSV
* Automação
* Geração de PDFs
* APIs
* OAuth 2.0
* Estruturas de dados
* Tratamento de erros
* Organização de código

---

# 📈 Melhorias Futuras

* [ ] Dashboard gráfico
* [ ] Interface web
* [ ] Banco de dados SQL
* [ ] Exportação Excel
* [ ] Gráficos automáticos
* [ ] Integração com Power BI
* [ ] Agendamento automático
* [ ] Sistema multiusuário
* [ ] Backup automático

---

# 🎯 Objetivo do Projeto

O objetivo deste projeto é praticar:

* Python
* Automação de processos
* Manipulação de dados
* Relatórios automatizados
* Integração com APIs
* Programação Orientada a Objetos

---

# 👨‍💻 Autor

Desenvolvido por Guilherme Silva 🚀

GitHub: https://github.com/MrHendrix0611
