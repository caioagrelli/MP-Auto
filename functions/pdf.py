from .dependencies import *


def pdf(empresa, bens, departamento, cnpj, typemail):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    logo = "./pdfs/logo.png"
    bens = bens.split(",")
    diretorio = './pdfs/'

    # Separar os bens e a quantidade
    list_bens = []
    for c in bens:
        c = c.strip()  # remover espaços extras

        partes = c.split(maxsplit=1)

        if len(partes) == 2:
            quantidade = int(partes[0])
            bem = partes[1].strip()

            # Criar dicionário e adicionar à lista
            list_bens.append({"quantidade": quantidade, "item": bem})
    bens = list_bens    
    
    if os.path.exists(logo):
        largura_logo = 75
        x_centro = (pdf.w - largura_logo) / 2
        pdf.image(logo, x=x_centro, y=3, w=largura_logo)
        pdf.ln(30) 
        
    else:
        print("Aviso: Logo não encontrada.")
        pdf.ln(10)
    
    # Informações Departamento
    pdf.set_font("Arial", style='B' ,size=10)
    pdf.cell(0, 5, "MINISTÉRIO PÚBLICO DO ESTADO DE PERNAMBUCO", ln=1, align="C")
    pdf.cell(0, 5, "PROCURADORIA GERAL DE JUSTIÇA", ln=1, align="C")
    pdf.cell(0, 5, "DEPARTAMENTO MINISTERIAL DE PATRIMÔNIO E MATERIAL", ln=1, align="C")
    pdf.cell(0, 5, f"{departamento}", ln=1, align="C")

    # --- Cabeçalho ---
    pdf.set_font("Arial", style="BU", size=15)
    pdf.cell(0, 20, f"{typemail}", ln=1, align="C")
    pdf.ln(1) 

    # --- Informações da Empresa ---
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, f"{empresa}", ln=1)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 5, f"CNPJ: {cnpj}", ln=1)
    pdf.ln(10)

    # --- Mensagem do motivo--
    

    # Dados da tabela
    pdf.set_fill_color(200, 200, 200)
    pdf.set_font('arial', style='B', size=9)
    pdf.cell(12, 10, 'QNTD°', border=1, align='C', fill=True)
    pdf.multi_cell(152, 10, 'DESCRIÇÃO', border=1, fill=True)
    pdf.cell(24, 10, 'EFISCO', border=1, align='C', fill=True)
    pdf.ln(0)
    
    
    for item in bens:
        pdf.set_font("Arial", size=12)
        pdf.cell(12, 10, f"{item['quantidade']}", border=1, align='C')
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(163, 10, f"{item['item']}", border=1)
        pdf.ln(0)


    # --- Salva o arquivo ---
    os.makedirs(diretorio, exist_ok=True)
    nome_arquivo = f"{diretorio}{empresa}.pdf"
    pdf.output(nome_arquivo)

    
    try:
        pdf.output(nome_arquivo)
        print(f"✅ SUCESSO! PDF '{nome_arquivo}' CRIADO")
    except PermissionError:
        print(f"❌ ERRO:'{nome_arquivo}' não pode ser salvo!")
    
    return(pdf)

pdf('TESTE','8 MES, 9 DADO', 'DIMMIS', '1234567', 'autorizacao')