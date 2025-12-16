from functions import sheets

def message(empresa, nome_servidor, matrícula_servidor, email_servidor, posição_servidor, telefone_servidor, typemail):
    
    #--- MENSAGEM DE INTENÇÃO ---
    if typemail == 'Intenção':
        mensagem = f'''
                    Aos fornecedores da empresa: {empresa},

        Por meio deste, notificamos a intenção de solicitação dos materiais listados em anexo, solicitando que a empresa {empresa} adote, desde já, as providências necessárias para garantir a regularidade documental e a disponibilidade dos itens a serem futuramente empenhados.

        Solicitamos especial atenção aos seguintes pontos:

        Regularidade Fiscal:
        É imprescindível que sejam providenciadas e mantidas atualizadas as certidões de regularidade fiscal perante os fiscos federal, estadual e municipal, bem como:

        Certidão de Regularidade do FGTS;

        Certidão Negativa de Débitos Trabalhistas (CNDT).
        Tais documentos serão exigidos conforme previsto no Termo de Referência e no Edital correspondente.

        Preparação dos Materiais:
        Solicitamos que seja verificada previamente a viabilidade de fornecimento dos itens relacionados, a fim de evitar atrasos na entrega após a emissão do empenho.
        Caso haja impossibilidade de fornecimento de algum item ou marca específica, a empresa deverá:

        Propor alternativa equivalente;

        Encaminhar catálogo e/ou amostra para análise e aprovação desta Divisão, antes da emissão do empenho.

        Forma de Entrega e Faturamento:
        Ressaltamos que o empenho será ordinário e, portanto:

        Todos os itens empenhados deverão constar em uma única nota fiscal;

        A entrega deverá ocorrer de forma integral e única, não sendo permitidas entregas parciais.

        Contamos com a colaboração e organização prévia de todos para garantir a agilidade e conformidade do processo após a autorização formal e o envio do empenho.

        Atenciosamente,
        {nome_servidor}
        {posição_servidor}
        Mat. {matrícula_servidor}
        E-mail: {email_servidor}
        Telefone: {telefone_servidor}
                    '''
    
    return(mensagem)