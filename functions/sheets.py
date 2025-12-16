from .dependencies import *

def sheets_parser(credenciais, planilha):
    print('--- Conectando na Planilha ---')
    gc = gspread.service_account(filename=credenciais)
    sh = gc.open(planilha)

    aba_intencao = sh.worksheet('1 Intenção de Fornecimento')
    aba_servidores = sh.worksheet('9 Informações')

    intencoes = aba_intencao.get_all_records()
    servidores = aba_servidores.get_all_records()

    lista_envio = []

    for idx, linha in enumerate(intencoes, start=2):

        enviar = linha["ENVIAR"]
        acao = linha["AÇÃO"]

        # ANTI-DUPLICADO
        if isinstance(acao, str) and acao.strip() != "":
            continue  

        if str(enviar).lower() not in ["true", "1", "x", "sim"]:
            continue

        servidor_nome = linha["REMETENTE"].strip().lower()

        # achar o servidor correspondente
        servidor = next(
            (s for s in servidores if s["SERVIDOR"].strip().lower() == servidor_nome),
            None
        )

        if servidor is None:
            print(f"⚠ Servidor '{servidor_nome}' não encontrado na aba 9 Informações.")
            continue

        # departamentos e dados agora vêm da aba dos SERVIDORES
        dados = {
            "linha_index": idx,

            # dados da intenção
            "empresa": linha["EMPRESA"],
            "cnpj": linha["CNPJ"],
            "destinatario": linha["DESTINATÁRIO"],
            "bens": linha["BENS"],
            "empenho": linha["EMPENHO"],
            "pregao": linha["PREGÃO"],

            # dados do servidor
            "nome_servidor": servidor["SERVIDOR"],
            "matricula_servidor": servidor["MATRÍCULA"],
            "email_servidor": servidor["EMAIL"],
            "telefone_servidor": servidor["TELEFONE"],
            "posicao_servidor": servidor["POSIÇÃO"],
            "departamento": servidor["DEPARTAMENTO"],  # <-- AQUI ESTÁ A CORREÇÃO
        }

        lista_envio.append(dados)

    return lista_envio