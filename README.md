# 📧 MP-Auto

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-API-green?style=for-the-badge&logo=googlesheets)
![Gmail](https://img.shields.io/badge/Gmail-SMTP-red?style=for-the-badge&logo=gmail)
![Status](https://img.shields.io/badge/status-ativo-brightgreen?style=for-the-badge)

**Automação de envio de comunicações institucionais a partir do Google Sheets**

</div>

---

## 📌 Sobre o Projeto

O **MP-Auto** é um sistema em Python desenvolvido para automatizar o envio de e-mails institucionais — **Intenção de Fornecimento**, **Autorização de Fornecimento** e **Notificação de Infração Contratual** — a partir de dados organizados em uma planilha do Google Sheets, com geração automática de PDF e controle de status de envio.

---

## 🚀 Funcionalidades

- 📊 Leitura automática de dados do Google Sheets
- ☑️ Envio condicionado a checkbox `ENVIAR`
- 📧 Envio de e-mails via Gmail SMTP
- 📝 Corpo do e-mail em HTML institucional
- 🖊️ Assinatura personalizada por servidor
- 📎 Geração e anexo automático de PDF
- 🔁 Verificação automática a cada 30 segundos
- ✅ Atualização da planilha após envio (`ENVIADO`)
- 🔒 Credenciais protegidas via variáveis de ambiente
- 🧠 Tipo de e-mail definido automaticamente pela aba

---

## 📁 Estrutura do Projeto
```bash
MP-Auto/
├── manage.py                 # Script principal (robô)
├── pdf.py                    # Geração de PDFs
├── text.py                   # Textos HTML dos e-mails
├── sheets.py                 # Leitura e escrita no Google Sheets
│
├── functions/
│   ├── __init__.py           # Inicialização do módulo
│   └── dependencies.py       # Imports e utilitários compartilhados
│
├── pdfs/                     # PDFs gerados (ignorado no Git)
│
├── credenciais.json          # Credenciais Google Sheets (ignorado)
├── .env                      # Variáveis sensíveis (ignorado)
├── .gitignore
└── README.md
```

---

## 🧠 Lógica de Funcionamento

O sistema monitora automaticamente as seguintes abas da planilha:

| Aba | Tipo de E-mail |
|-----|----------------|
| `1 Intenção de Fornecimento` | Intenção |
| `2 Autorização de fornecimento` | Autorização |
| `3 Notificação de Infração Contratual` | Infração |

Sempre que a coluna `ENVIAR` for marcada **e** a linha ainda não estiver como `ENVIADO`, o sistema executa automaticamente:

1. 📨 Monta o e-mail correto para o tipo da aba
2. 📄 Gera o PDF correspondente
3. 📤 Envia o e-mail com o PDF anexado
4. ✅ Marca a linha como `ENVIADO`
5. 🔲 Desmarca o checkbox `ENVIAR`

---

## ⚙️ Configuração do Ambiente

**1️⃣ Criar ambiente virtual** *(opcional, mas recomendado)*
```bash
python -m venv ambientevirtual
```

**2️⃣ Instalar dependências**
```bash
pip install gspread fpdf python-dotenv
```

**3️⃣ Variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:
```env
GMAIL_USER=seu_email@gmail.com
GMAIL_PASS=sua_senha_de_app
```

> ⚠️ **Nunca use a senha normal do Gmail.** Utilize uma [Senha de App](https://support.google.com/accounts/answer/185833).

**4️⃣ Credenciais Google Sheets**

Coloque o arquivo `credenciais.json` (Service Account) na raiz do projeto e compartilhe a planilha com o e-mail da Service Account.

---

## ▶️ Executando o Robô
```bash
python manage.py
```

Saída esperada:
```
🚀 Robô iniciado! Verificando planilha a cada 30 segundos...
📄 Verificando: 2 Autorização de fornecimento
📦 Empresa: XYZ LTDA
📨 Email enviado para fornecedor@email.com
✔ Linha marcada como ENVIADO
```

---

## 📊 Modelo de Planilha

Planilha base compatível com a automação do projeto:

🔗 [Acessar planilha no Google Sheets](https://docs.google.com/spreadsheets/d/1ymw9mmaZb5a_WAEbYO0IdSUls1d6d2EGtvFqSAZj7iA)

---

## 👨‍💻 Autor

Desenvolvido por **Caio Agrelli** com foco em automação administrativa, confiabilidade e padronização institucional.

📧 caarr@cin.ufpe.br
