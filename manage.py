from functions import *
from dotenv import load_dotenv
load_dotenv()

# CONFIGURAÇÕES DO GMAIL
gmail = os.getenv("GMAIL_USER")
senha = os.getenv("GMAIL_PASS")

# CONFIGURAÇÕES DA PLANILHA
credenciais = 'credenciais.json'
planilha = 'Artefatos de Execução Contratual'

# Função principal que processa intenções
def processar_envios():

    print("\n🔄 Verificando planilha...")

    # Carrega dados atualizados
    intencoes = sheets_parser(credenciais, planilha)

    # abre planilha para atualizar campos
    gc = gspread.service_account(filename=credenciais)
    sh = gc.open(planilha)
    aba_intencao = sh.worksheet('1 Intenção de Fornecimento')

    # nada para enviar
    if len(intencoes) == 0:
        print("⏳ Nenhuma intenção marcada para envio.")
        return

    print(f"📌 {len(intencoes)} registro(s) pronto(s) para envio.\n")

    # processar cada intenção
    for dados in intencoes:

        print("----------------------------------------")
        print(f"📦 Processando empresa: {dados['empresa']}")

        # gerar PDF
        pdf_obj = pdf(
            dados["empresa"],
            dados["bens"],
            dados["departamento"],
            dados["cnpj"]
        )
        caminho_pdf = f"./pdfs/{dados['empresa']}.pdf"

        # corpo do email
        corpo = message_mail(
            dados["empresa"],
            dados["nome_servidor"],
            dados["matricula_servidor"],
            dados["email_servidor"],
            dados["posicao_servidor"],
            dados["telefone_servidor"],
            typeemail,
            dados ["pregao"],
            dados ["empenho"],
            dados ["cnpj"],
            )

        # envio
        enviado = sendmail(
            dados["destinatario"],
            "Intenção de Fornecimento",
            corpo,
            caminho_pdf
        )

        # atualizar planilha
        if enviado:
            
            linha = dados["linha_index"]

            # ✔ Coluna K (11) = AÇÃO
            aba_intencao.update_cell(linha, 11, "ENVIADO")

            # ✔ Coluna I (9) = ENVIAR checkbox
            aba_intencao.update_cell(linha, 9, False)

            print(f"✔ Linha {linha} marcada como ENVIADO e ENVIAR desmarcado")

# Função para enviar e-mail
def sendmail(destinatario, assunto, corpo, caminho_pdf):
    try:
        msg = MIMEMultipart()
        msg['From'] = gmail
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'html'))

        # Anexar PDF
        with open(caminho_pdf, "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="pdf")
            attach.add_header('Content-Disposition',
                              'attachment',
                              filename=caminho_pdf.split('/')[-1])
            msg.attach(attach)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail, senha)
        server.send_message(msg)
        server.quit()

        print(f"📨 Email enviado para {destinatario}")
        return True

    except Exception as erro:
        print(f"❌ Erro ao enviar email para {destinatario}: {erro}")
        return False

# LOOP 30 SEGUNDOS
print("🚀 Robô iniciado! Verificando planilha a cada 30 segundos...\n")
while True:
    try:
        processar_envios()
    except Exception as erro:
        print(f"❌ Erro inesperado: {erro}")

    print("⏲ Aguardando 30 segundos...\n")
    time.sleep(30)