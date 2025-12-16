from .dependencies import *

def cabecalho_form():
    return '''
<!-- CABEÇALHO INSTITUCIONAL MPPE -->
<table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:20px;">
  <tr>
    <td align="center">

      <!-- CONTEÚDO CENTRALIZADO -->
      <table width="900" cellpadding="0" cellspacing="0">
        <tr>
          <td align="center">
            <a href="https://portal.mppe.mp.br" target="_blank">
              <img src="https://drive.google.com/uc?export=download&id=145S0uM5AZGh_R8to1c-cW6hAyq2lpou9"
                   alt="MINISTÉRIO PÚBLICO DE PERNAMBUCO"
                   width="650"
                   style="display:block; border:0;">
            </a>
          </td>
        </tr>
      </table>

    </td>
  </tr>

  <!-- LINHA PRETA 100% -->
  <tr>
    <td>
      <hr style="border:none; border-top:2px solid #000; width:100%;">
    </td>
  </tr>
</table>
'''

def assinatura_html(nome_servidor, posicao_servidor, matricula_servidor, email_servidor, telefone_servidor):
  logo_mp = "https://portal.mppe.mp.br/documents/d/guest/braso_mppe_jpg-jpg-1"

  return f"""
<table width="100%" cellpadding="0" cellspacing="0" style="margin-top:30px;">
  <tr>
    <!-- LOGO -->
    <td width="120" valign="top" style="padding-right:15px;">
      <a href="https://portal.mppe.mp.br" target="_blank">
        <img src="{logo_mp}"
              width="100"
              alt="MPPE"
              style="border:0; display:block;">
      </a>
    </td>

    <!-- DADOS -->
    <td valign="top" style="font-family: Arial, sans-serif; font-size: 11pt; color:#000;">
      <b style="font-size:12pt;">{nome_servidor}</b><br>
      {posicao_servidor}<br>
      Matrícula: {matricula_servidor}<br>

      <a href="mailto:{email_servidor}"
          style="color:#0645AD; text-decoration:none;">
          {email_servidor}
      </a><br>

      Telefone: {telefone_servidor}
    </td>
  </tr>

  <!-- LINHA INFERIOR -->
  <tr>
    <td colspan="2" style="padding-top:10px;">
      <hr style="border:none; border-top:2px solid #8B0000;">
    </td>
  </tr>
</table>
"""

def text_mail(typemail, empresa, pregao, empenho, cnpj):
      
#------------------------------------------------------#
#               MENSAGEM DE INTENÇÃO
#------------------------------------------------------#

  if typemail == 'intenção':
    return f'''
<html>
<head>
<style>
  body {{
    font-family: Arial, sans-serif;
    font-size: 12pt;
    color: #000000;
  }}

  .logo {{
    text-align: center;
    margin-bottom: 20px;
  }}

  .secao {{
    font-weight: bold;
    margin-top: 18px;
  }}

  ul {{
    margin-top: 5px;
    margin-bottom: 10px;
  }}

  .assinatura {{
    margin-top: 30px;
  }}
</style>
</head>

<body>


<p><b>Aos fornecedores da empresa {empresa},</b></p>

<p>
  Por meio deste, notificamos a <b>intenção de solicitação</b> dos materiais
  listados em anexo, solicitando que a empresa <b>{empresa}</b> adote, desde já,
  as providências necessárias para garantir a <b>regularidade documental</b> e
  a <b>disponibilidade dos itens</b> a serem futuramente empenhados.
</p>

<p><b>Solicitamos especial atenção aos seguintes pontos:</b></p>

<p><b>Regularidade Fiscal</b></p>

<p>
  É imprescindível que sejam providenciadas e mantidas atualizadas as certidões
  de regularidade fiscal perante os fiscos federal, estadual e municipal, bem
  como:
</p>

<ul>
  <li>Certidão de Regularidade do FGTS;</li>
  <li>Certidão Negativa de Débitos Trabalhistas (CNDT).</li>
</ul>

<p>
  Tais documentos serão exigidos conforme previsto no Termo de Referência e no
  Edital correspondente.
</p>

<p><b>Preparação dos Materiais</b></p>

<p>
  Solicitamos que seja verificada previamente a viabilidade de fornecimento dos
  itens relacionados, a fim de evitar atrasos na entrega após a emissão do
  empenho.
</p>

<p>
  Caso haja impossibilidade de fornecimento de algum item ou marca específica,
  a empresa deverá:
</p>

<ul>
  <li>Propor alternativa equivalente;</li>
  <li>
    Encaminhar catálogo e/ou amostra para análise e aprovação desta Divisão,
    antes da emissão do empenho.
  </li>
</ul>

<p><b>Forma de Entrega e Faturamento</b></p>

<p>
  Ressaltamos que o empenho será <b>ordinário</b> e, portanto:
</p>

<ul>
  <li>Todos os itens empenhados deverão constar em <b>uma única nota fiscal</b>;</li>
  <li>
    A entrega deverá ocorrer de forma <b>integral e única</b>, não sendo
    permitidas entregas parciais.
  </li>
</ul>

<p>
  Contamos com a colaboração e organização prévia de todos para garantir a
  agilidade e a conformidade do processo após a autorização formal e o envio do
  empenho.
</p>

  </body>
</html>
    '''

#------------------------------------------------------#
#               MENSAGEM DE AUTORIZAÇÃO
#------------------------------------------------------#

  elif typemail == 'autorização':
    return f'''
<head>
  <style>
    body {{
      font-family: Arial, sans-serif;
      font-size: 12pt;
      color: #000000;
    }}

    .logo {{
      text-align: center;
      margin-bottom: 20px;
    }}

    ul {{
      margin-top: 5px;
      margin-bottom: 10px;
    }}

    .assinatura {{
      margin-top: 30px;
    }}
  </style>
</head>

<body>

  <p><b>Aos fornecedores da empresa {empresa},</b></p>

  <p>
    Por meio deste, comunicamos a <b>AUTORIZAÇÃO PARA FORNECIMENTO</b> dos materiais
    relacionados em anexo, devidamente autorizados no âmbito do processo
    administrativo correspondente, para atendimento a este Órgão.
  </p>

  <p>
    Dessa forma, solicitamos que a empresa <b>{empresa}</b> providencie a
    separação, organização e posterior envio dos itens autorizados,
    observando-se rigorosamente as especificações técnicas, quantitativos e
    condições estabelecidas no Termo de Referência, no Edital e nos demais
    documentos que regem o processo.
  </p>

  <p><b>Solicitamos especial atenção aos pontos a seguir:</b></p>

  <p><b>Regularidade Fiscal</b></p>

  <p>
    É imprescindível que sejam mantidas atualizadas as certidões de regularidade
    fiscal perante os fiscos federal, estadual e municipal, bem como:
  </p>

  <ul>
    <li>Certidão de Regularidade do FGTS;</li>
    <li>Certidão Negativa de Débitos Trabalhistas (CNDT).</li>
  </ul>

  <p>
    A regularidade da documentação é condição necessária para a formalização e
    continuidade do fornecimento autorizado.
  </p>

  <p><b>Manifestação da Empresa – Prazo para Resposta</b></p>

  <p>
    Solicitamos que a empresa manifeste-se formalmente, por meio de resposta a
    este e-mail, no prazo máximo de até <b>15 (quinze) dias corridos</b>, contados
    a partir do recebimento desta comunicação, confirmando:
  </p>

  <ul>
    <li>A ciência da autorização de fornecimento;</li>
    <li>A disponibilidade dos itens autorizados;</li>
    <li>A capacidade de atendimento às condições e prazos estabelecidos.</li>
  </ul>

  <p>
    A ausência de manifestação no prazo estipulado poderá ensejar a adoção das
    providências administrativas cabíveis, nos termos da legislação vigente e
    dos instrumentos que regem o processo.
  </p>

  <p><b>Preparação e Envio dos Materiais</b></p>

  <p>
    Os materiais autorizados deverão ser separados e preparados para envio, de
    forma integral e conforme as especificações constantes nos documentos do
    processo.
  </p>

  <p>
    Na hipótese de impossibilidade de fornecimento de algum item ou marca
    específica, a empresa deverá:
  </p>

  <ul>
    <li>Comunicar formalmente esta Divisão;</li>
    <li>Apresentar proposta de item equivalente;</li>
    <li>
      Encaminhar catálogo e/ou amostra para análise e aprovação, previamente à
      entrega.
    </li>
  </ul>

  <p><b>Forma de Entrega e Faturamento</b></p>

  <p>
    Ressaltamos que o empenho será <b>ordinário</b>, sendo observadas as seguintes
    condições:
  </p>

  <ul>
    <li>Todos os itens deverão constar em <b>uma única nota fiscal</b>;</li>
    <li>
      A entrega deverá ocorrer de forma <b>integral e única</b>, não sendo
      permitidas entregas parciais.
    </li>
  </ul>

  <p>
    Por fim, seguem em anexo a relação dos materiais autorizados para
    fornecimento, para ciência e adoção das providências cabíveis.
  </p>

  <p>
    Contamos com a colaboração da empresa para o fiel cumprimento das condições
    estabelecidas, de modo a assegurar a regularidade, a celeridade e a
    conformidade do fornecimento autorizado.
  </p>
</body>
</html>
  '''
  elif typemail == 'Infracao':
    return f'''em andamento'''

def message_mail(empresa, nome_servidor, matrícula_servidor, email_servidor, posição_servidor, telefone_servidor, typemail, pregao, empenho, cnpj):
  cabecalho = cabecalho_form()
  assinatura = assinatura_html(nome_servidor, posição_servidor, matrícula_servidor, email_servidor, telefone_servidor)
  corpo_mail = text_mail(typemail, empresa, pregao, empenho, cnpj)    
  
  mensagem = f'''
  {cabecalho}
  {corpo_mail}
  {assinatura}
  '''
  return(mensagem)
