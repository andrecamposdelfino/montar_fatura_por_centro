import sqlite3

conexao = sqlite3.connect("fatura.db")
cursor = conexao.cursor()

def criar_tabela_centro():
    try:
        query = """
            create table if not exists centro(
                codigo integer primary key autoincrement,
                nome text not null            
            )
        """
        cursor.execute(query)
        conexao.commit()
        print(f"Tabela criada com sucesso")
    except Exception as error:
        print(f"Erro ao tentar criar a tabela : {error}")

# inicio gravar cartão
def gravar_cartao(cartao):
    try:
        query = """
            insert into cartao values(:codigo, :numero)
        """
        cursor.execute(query, vars(cartao))
        conexao.commit()
        print(f"GRAVOU com sucesso")
    except Exception as error:
        print(f"Erro ao tentar criar a tabela : {error}")

#  fim gravar cartão

#  incio lista dados cartao
def listar_cartao():
    try:
        query = "select * from cartao"
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
        # return dados
    except Exception as error:
        print(f"Erro ao tentar listar os dados : {error}")

# fim lista dados cartão

# inicio atualiza cartao
def atualiza_cartao(codigo, numero):
    try:
        query = f"""
            update cartao set codigo = ?, numero = ? where codigo = {codigo}
        """
        cursor.execute(query, (codigo, numero))
        conexao.commit()
    except Exception as error:
        print(f"Erro ao tentar atualizar os dados : {error}")


# fim atualiza cartão

# inicio da funçao deletar dado cartão
def deletar_cartao(codigo):
    try:
        query = f"""
            delete from cartao where codigo = {codigo}
        """
        cursor.execute(query, (codigo))
        conexao.commit()
        print("Cartão excluido com sucesso!!")
    except Exception as error:
        print(f"Erro ao tentar excluir cartão : {error}")

# fim da função deletar dado cartão

# cadastrar lançamentos
def cadastrar_lancamentos(lancamento):
    try:
        query = """
            insert into lancamento values(:codigo_lancamento, :data_compra, :vencimento, :credor, :documento, :ano, :parcela, :valor, :classificacao, :centro_custo, :cartao)
        """
        cursor.execute(query, vars(lancamento))
        conexao.commit()
        print("Lançamento feito com sucesso!")
    except Exception as error:
        print(f"Erro ao tentar cadastrar : {error}")
    
def cadastrar_classificacao(classificacao):
    try:
        query = """
            insert into classificacao values(:codigo, :classificacao)
        """
        cursor.execute(query, vars(classificacao))
        conexao.commit()
        print("Lançamento feito com sucesso!")
    except Exception as error:
        print(f"Erro ao tentar cadastrar : {error}")
# fim cadastrar lançamentos

# listagem dos credores
def listar_credores():
    try:
        query = "select codigo_lancamento, credor from lancamento"
        cursor.execute(query)
        dados = cursor.fetchall()
        # for dado in dados:
        #     print(dado)
        return dados
    except Exception as error:
        print(f"Erro ao tentar listar os dados : {error}")

def listar_credores_por_nome(nome):
    try:
        query = f"select codigo_lancamento, credor from lancamento where credor like '%{nome}%'"
        cursor.execute(query)
        dados = cursor.fetchall()
        # for dado in dados:
        #     print(dado)
        return dados
    except Exception as error:
        print(f"Erro ao tentar listar os dados : {error}")
    

# fim listagem dos creores

# listagem de classificacao
def listar_classificacao():
    try:
        query = "select codigo_lancamento, classificacao from lancamento"
        cursor.execute(query)
        dados = cursor.fetchall()
        # for dado in dados:
        #     print(dado)
        return dados
    except Exception as error:
        print(f"Erro ao tentar listar os dados : {error}")

def listar_classificacao_por_nome(nome):
    try:
        query = f"select codigo_lancamento, classificacao from lancamento where classificacao like '%{nome}%'"
        cursor.execute(query)
        dados = cursor.fetchall()
        # for dado in dados:
        #     print(dado)
        return dados
    except Exception as error:
        print(f"Erro ao tentar listar os dados : {error}")

# fim listagem de classificacao

# soma dos valores por centro de custo
def soma_oficina():
    try:
        query = """
            select sum(valor) from lancamento where centro_custo = "ETS - OFICINA"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Erro ao tentar somar os dados {error}")

def soma_jaiba():
    try:
        query = """
            select sum(valor) from lancamento where centro_custo = "ETS - LOC JAIBA"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        # for dado in dados:
        #     print(dado[0])
        return dados
    except Exception as error:
        print(f"Erro ao tentar somar os dados {error}")

def soma_adm():
    try:
        query = """
            select sum(valor) from lancamento where centro_custo = "ETS - ADM"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        # for dado in dados:
        #     print(dado[0])
        return dados
    except Exception as error:
        print(f"Erro ao tentar somar os dados {error}")

def soma_alpha():
    try:
        query = """
            select sum(valor) from lancamento where centro_custo = "ETS - ALPHA"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        # for dado in dados:
        #     print(dado[0])
        return dados
    except Exception as error:
        print(f"Erro ao tentar somar os dados {error}")


def soma_maq_equip():
    try:
        query = """
            select sum(valor) from lancamento where centro_custo = "ETS - MAQ E EQUIP"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        # for dado in dados:
        #     print(dado[0])
        return dados
    except Exception as error:
        print(f"Erro ao tentar somar os dados {error}")
        

def soma_loc_maq():
    try:
        query = """
            select sum(valor) from lancamento where centro_custo = "ETS - LOC MAQ"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        # for dado in dados:
        #     print(dado[0])
        return dados
    except Exception as error:
        print(f"Erro ao tentar somar os dados {error}")


# fim soma dos valores por centro de custo

# lista todos os lançamentos
def lista_lancamentos():
    try:
        query = """
            select * from lancamento 
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        # for dado in dados:
        #     print(dado)
        return dados
    except Exception as error:
        print(f"Erro ao tentar listar os dados {error}")


def lista_lancamentos_por_doc(documento):
    try:
        query = f"select * from lancamento where documento = {documento}"
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Erro ao tentar listar por data : {error}")

def lista_lancamentos_por_credor(nome):
    try:
        query = f"select * from lancamento where credor like '%{nome}%'"
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Erro ao tentar listar por data : {error}")


# fim lista lançamentos