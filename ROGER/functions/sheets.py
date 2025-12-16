from dependencies import *

# --- Dados da Planilha ---
credenciais = 'credenciais.json'
planilha = 'Artefatos de Execução Contratual'

def sheets_parser(credenciais, planilha):
    print('--- Conectando na Planilha ---')
    gc = gspread.service_account(filename=credenciais)
    sh = gc.open(planilha)

    intenção = sh.get_worksheet('1 Intenção de Fornecimento')
    servidores = sh.get_worksheet('9 Informações')

    intenção_dados = intenção.get_all_records()
    servidores_dados = servidores.get_all_records()    


# --- Coleta de dados Servidores ---
    for i, linha in enumerate(servidores):
        nome_servidor = linha['SERVIDOR']
        matrícula_servidor = linha['Matrícula']
        email_servidor = linha['EMAIL']
        telefone_servidor = linha['TELEFONE']
        posição_servidor = linha['POSIÇÃO']
        departamento = linha['DEPARTAMENTO']

# --- Coleta de dados Intenção ---
    for i, linha in enumerate(intenção):
        empenho = linha['EMPENHO']
        empresa = linha['EMPRESA']
        cnpj = linha['CNPJ']
        destinatario = linha['DESTINATÁRIO']
        pregao = linha['PREGÃO']
        remetente = linha['REMETENTE']
        status = linha['ENVIAR']
        bens = linha['BENS']        
    
    # --- TRANSFORMA TUDO EM DICIONÁRIO ---
    dados = {}

    # --- Coleta de dados Servidores ---
    for i, linha in enumerate(servidores):
        dados["nome_servidor"] = linha['SERVIDOR']
        dados["matricula_servidor"] = linha['Matrícula']
        dados["email_servidor"] = linha['EMAIL']
        dados["telefone_servidor"] = linha['TELEFONE']
        dados["posicao_servidor"] = linha['POSIÇÃO']
        break

    # --- Coleta de dados Intenção ---
    for i, linha in enumerate(intenção):
        dados["empenho"] = linha["EMPENHO"]
        dados["empresa"] = linha["EMPRESA"]
        dados["cnpj"] = linha["CNPJ"]
        dados["destinatario"] = linha["DESTINATÁRIO"]
        dados["pregao"] = linha["PREGÃO"]
        dados["remetente"] = linha["REMETENTE"]
        dados["status"] = linha["AÇÃO"]
        dados["bens"] = linha["BENS"]
        dados["departamento"] = linha["DEPARTAMENTO"]
        break
