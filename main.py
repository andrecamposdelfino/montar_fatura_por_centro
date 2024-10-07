from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import  QMessageBox


# importacao do banco
import database
import locale
import pandas as pd

conn = database.conexao
cursor = conn.cursor()

# importacao dos modelos
from modelo import Cartao, Centro, Credor, Lancamento

# dia, mes e ano

# mensagens do sistema
def msgSucesso(msg):
    QMessageBox.information(None, "Sucesso!!", msg)

def msgErro(msg):
    QMessageBox.warning(None, "Error!!", msg)

# cria o aplicativo
app = QtWidgets.QApplication([])

# criar os formularios
form_dash = uic.loadUi("./forms/dashboard.ui")
form_cad_cartao = uic.loadUi("./forms/cad_cartao.ui")
form_cad_centro = uic.loadUi("./forms/cad_centro.ui")
form_cad_credor = uic.loadUi("./forms/cad_credor.ui")
form_cad_lancamento = uic.loadUi("./forms/cad_lancamento.ui")
form_lista_credor = uic.loadUi("./forms/form_lista_credor.ui")
form_lista_classificacao = uic.loadUi("./forms/form_lista_classificacao.ui")
form_lista_lancamento = uic.loadUi("./forms/form_lista_lancamento.ui")

# função para atualizar a dashboard
def atuliza_dashboard():
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    soma_oficina = database.soma_oficina()
    soma_loc_jaiba = database.soma_jaiba()
    soma_alpha = database.soma_alpha()
    soma_loc_maq = database.soma_loc_maq()
    soma_adm = database.soma_adm()
    soma_maq_equip = database.soma_maq_equip()


    if soma_adm[0][0] == None:
        soma_adm = f"R$ 0,00"
        form_dash.lblValorAdm.setText(soma_adm)
    else:
        form_dash.lblValorAdm.setText(locale.currency(soma_adm[0][0]))

    if soma_oficina[0][0] == None:
        soma_oficina = f"R$ 0,00"
        form_dash.lblValorOficina.setText(soma_oficina)
    else:
        form_dash.lblValorOficina.setText(locale.currency(soma_oficina[0][0]))

    if soma_loc_jaiba[0][0] == None:
        soma_loc_jaiba = f"R$ 0,00"
        form_dash.lblValorLocJaiba.setText(soma_loc_jaiba)
    else:
        form_dash.lblValorLocJaiba.setText(locale.currency(soma_loc_jaiba[0][0]))

    if soma_alpha[0][0] == None:
        soma_alpha = f"R$ 0,00"
        form_dash.lblValorAlpha.setText(soma_alpha)
    else:
        form_dash.lblValorAlpha.setText(locale.currency(soma_alpha[0][0]))

    if soma_loc_maq[0][0] == None:
        soma_loc_maq = f"R$ 0,00"
        form_dash.lblValorLocMaq.setText(soma_loc_maq)
    else:
        form_dash.lblValorLocMaq.setText(locale.currency(soma_loc_maq[0][0]))
    
    if soma_maq_equip[0][0] == None:
        soma_maq_equip = f"R$ 0,00"
        form_dash.lblValorMaqEquip.setText(soma_maq_equip)
    else:
        form_dash.lblValorMaqEquip.setText(locale.currency(soma_maq_equip[0][0]))


# inicio das funcoes de gravar, atualizar, excluir os dados nas tabelas
def gravar_cartao():
    numero = form_cad_cartao.txtNumeroCartao.text()
    cartao = Cartao(None, numero)
    if numero != "":
        database.gravar_cartao(cartao)
        form_cad_cartao.txtNumeroCartao.setText("")
        msgSucesso("Cartão gravado com sucesso!!")
    else:
        msgErro("Error não foi possivel gravar o cartão!!")

def gravar_compra():
    data_compra = form_cad_lancamento.txtDataCompra.text()
    data_vencimento = form_cad_lancamento.txtVencimento.text()
    credor = form_cad_lancamento.txtCredor.text()
    documento = form_cad_lancamento.txtDocumento.currentText()
    ano = form_cad_lancamento.txtAno.text()
    parcela = form_cad_lancamento.txtParcela.text()
    valor = form_cad_lancamento.txtValor.text()
    classificacao = form_cad_lancamento.txtClassificacao.text()
    centro = form_cad_lancamento.txtCentro.currentText()
    cartao = form_cad_lancamento.txtCartao.currentText()

    if data_compra != "" and data_vencimento != "" and credor != "" and documento != "" and ano != "" and parcela != "" and valor != "" and classificacao != "" and centro != "" and cartao !="":
        lancamento = Lancamento(None, data_compra, data_vencimento, credor, documento, parcela, valor, classificacao, centro, cartao)
        database.cadastrar_lancamentos(lancamento)
        msgSucesso("Compra cadastrada")
        atuliza_dashboard()
    else:
        msgErro("Erro, por favor preencher todos os campos!")

   

# fim das funcoes de gravar, atualizar, excluir os dados nas tabelas

# fecha o form cadastro de cartao
def close_cad_cartao():
    form_cad_cartao.close()

# executa o form cadastro de cartao
def cad_cartao():
    form_cad_cartao.show()
    form_cad_cartao.btnGravar.clicked.connect(gravar_cartao)
    form_cad_cartao.btnCancelar.clicked.connect(close_cad_cartao)
 
 #  fecha o form cadastro de credor
def close_cad_credor():
    form_cad_credor.close()
    

#  executa o form cadastro de credor
def cad_credor():
    form_cad_credor.show()
    form_cad_credor.btnGravar.clicked.connect(gravar_cartao)
    form_cad_credor.btnCancelar.clicked.connect(close_cad_credor)

# fecha o form cadastro de centro de custo
def close_cad_centro():
    form_cad_centro.close()

# executa  form cadastro de centro de custo
def cad_centro():
    form_cad_centro.show()
    form_cad_centro.btnGravar.clicked.connect(gravar_cartao)
    form_cad_centro.btnCancelar.clicked.connect(close_cad_centro)

#  fecha o form dashoboard
def close_form_dash():
    form_dash.close()

# formulario lista credores
def lista_credores():
    form_lista_credor.show()
    dados = database.listar_credores()   
    form_lista_credor.dgvCredores.setRowCount(len(dados))
    form_lista_credor.dgvCredores.setColumnCount(2)

    for l in range(0, len(dados)):
        for c in range(0, 2):
            form_lista_credor.dgvCredores.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))
    
    form_lista_credor.dgvCredores.setColumnWidth(1, 280)
    form_lista_credor.dgvCredores.cellClicked.connect(pega_dados_credor)

def lista_credores_por_nome():
    nome = form_lista_credor.txtPesquisarCredor.text()
    dados = database.listar_credores_por_nome(nome)   
    form_lista_credor.dgvCredores.setRowCount(len(dados))
    form_lista_credor.dgvCredores.setColumnCount(2)

    for l in range(0, len(dados)):
        for c in range(0, 2):
            form_lista_credor.dgvCredores.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))
    
    form_lista_credor.dgvCredores.setColumnWidth(1, 280)
    form_lista_credor.dgvCredores.cellClicked.connect(pega_dados_credor)

def pega_dados_credor(row, column):
    item = form_lista_credor.dgvCredores.item(row, column)
    form_cad_lancamento.txtCredor.setText(item.text())
    msgSucesso("O Campo credor foi preenchido")
    
# fim formulario lista credores

# lista classificacao
def lista_classificacao():
    form_lista_classificacao.show()
    dados = database.listar_classificacao()
    form_lista_classificacao.dgvClassificacao.setRowCount(len(dados))
    form_lista_classificacao.dgvClassificacao.setColumnCount(2)

    for l in range(0, len(dados)):
        for c in range(0, 2):
            form_lista_classificacao.dgvClassificacao.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))
    
    form_lista_classificacao.dgvClassificacao.setColumnWidth(1, 250)
    form_lista_classificacao.dgvClassificacao.cellClicked.connect(pega_dados_classificacao)

def lista_classificacao_por_nome():
    nome = form_lista_classificacao.txtPesquisarClassificacao.text()
    dados = database.listar_classificacao_por_nome(nome)
    form_lista_classificacao.dgvClassificacao.setRowCount(len(dados))
    form_lista_classificacao.dgvClassificacao.setColumnCount(2)

    for l in range(0, len(dados)):
        for c in range(0, 2):
            form_lista_classificacao.dgvClassificacao.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))
    
    form_lista_classificacao.dgvClassificacao.setColumnWidth(1, 250)
    form_lista_classificacao.dgvClassificacao.cellClicked.connect(pega_dados_classificacao)

# função para abrir o formulario de listar lançamentos
def lista_lancamentos():
    lancamentos = database.lista_lancamentos()
    form_lista_lancamento.show()

    form_lista_lancamento.dgvDadosLancamento.setRowCount(len(lancamentos))
    form_lista_lancamento.dgvDadosLancamento.setColumnCount(10)

    for l in range(0, len(lancamentos)):
        for c in range(0, 10):
            form_lista_lancamento.dgvDadosLancamento.setItem(l, c, QtWidgets.QTableWidgetItem(str(lancamentos[l][c])))
    
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(0, 50)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(3, 250)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(4, 50)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(5, 50)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(7, 250)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(9, 50)

# fim da função que abre o formulario de listar lançamento

# função para consulta por doc
def listar_por_doc():
    doc = form_lista_lancamento.txtPesquisaMes.currentText()
    dados = database.lista_lancamentos_por_doc(doc)

    form_lista_lancamento.dgvDadosLancamento.setRowCount(len(dados))
    form_lista_lancamento.dgvDadosLancamento.setColumnCount(10)

    for l in range(0, len(dados)):
        for c in range(0, 10):
            form_lista_lancamento.dgvDadosLancamento.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))
    
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(0, 50)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(3, 250)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(4, 50)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(5, 50)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(7, 250)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(9, 50)


#  função para converter os dados para excell
def converter_to_excell():
    try:
        doc = form_lista_lancamento.txtPesquisaMes.currentText()
        query = f"""
            select * from lancamento where documento = {doc}
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        if dados == []:
            msgErro("Não foi possivel converter para Excell, pois a consulta não retornou nenhum dado nessa consulta")
            return
        df = pd.read_sql_query(query, conn)
        df.to_excel(f'FT - MES{doc}.xlsx')

        msgSucesso("Arquivo gerado com sucesso!!")
    except Exception as error:
        msgErro(f"Não foi possivel converter para Excell : {error}")
 # fim função para converter os dados para excell   

# fim da função de consulta por doc

# função para consulta por do nome
def listar_por_nome():
    nome = form_lista_lancamento.txtPesquisaCredor.text()
    dados = database.lista_lancamentos_por_credor(nome)

    form_lista_lancamento.dgvDadosLancamento.setRowCount(len(dados))
    form_lista_lancamento.dgvDadosLancamento.setColumnCount(10)

    for l in range(0, len(dados)):
        for c in range(0, 10):
            form_lista_lancamento.dgvDadosLancamento.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))
    
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(0, 50)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(3, 250)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(4, 50)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(5, 50)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(7, 250)
    form_lista_lancamento.dgvDadosLancamento.setColumnWidth(9, 50)
    


# fim da função de consulta por nome

def pega_dados_classificacao(row, column):
    item = form_lista_classificacao.dgvClassificacao.item(row, column)
    form_cad_lancamento.txtClassificacao.setText(item.text())
    msgSucesso("O Campo classificação foi preenchido")
# fim lista classificacao

# abri o formulario para cadastrar uma compra
def cad_lancamento():
    form_cad_lancamento.show()
    form_cad_lancamento.btnGravar.clicked.connect(gravar_compra)
    form_cad_lancamento.btnCancelar.clicked.connect(close_cad_lancamento)
    form_cad_lancamento.btnAuxiliar2.clicked.connect(lista_credores)
    form_cad_lancamento.btnAuxiliar1.clicked.connect(lista_classificacao)

# fecha o formulario de cadastro de compra
def close_cad_lancamento():
    form_cad_lancamento.close()

# acoes para os botoes do menu
form_dash.btnCadCredores.triggered.connect(cad_credor)
form_dash.btnCadCartao.triggered.connect(cad_cartao)
form_dash.btnCadCentro.triggered.connect(cad_centro)
form_dash.btnSair.triggered.connect(close_form_dash)
form_dash.btnLancarCompra.triggered.connect(cad_lancamento)
form_dash.btnItau.triggered.connect(lista_lancamentos)
form_dash.btnBrasil.triggered.connect(lista_lancamentos)
form_dash.btnBradesco.triggered.connect(lista_lancamentos)
form_lista_credor.btnPesquisarCredor.clicked.connect(lista_credores_por_nome)
form_lista_classificacao.btnPesquisarClassificacao.clicked.connect(lista_classificacao_por_nome)
form_lista_lancamento.btnPesquisarData.clicked.connect(listar_por_doc)
form_lista_lancamento.btnExcell.clicked.connect(converter_to_excell)

# executa o form dashboard
form_dash.show()
atuliza_dashboard()
# executa o aplicativo
app.exec()