from dependencies import *

# --- Dados do Gmail ---
gmail = 'dempam@mppe.mp.br'
senha = 'emju bcwm prdr mot'
typemail = 'Intenção'

assunto = 'Hello word!'
corpo = 'Hello word!'
destinatario = 'caiooagrelli@gmail.com'

def enviar_gmail(destinatario, assunto, corpo):
    try:
        msg = MIMEMultipart()
        msg['From'] = gmail
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail, senha)

        server.send_message(msg)
        server.quit()

        print(f"✔ Email enviado para {destinatario}")
        return True

    except Exception as erro:
        print(f"❌ Erro ao enviar email para {destinatario}: {erro}")
        return False