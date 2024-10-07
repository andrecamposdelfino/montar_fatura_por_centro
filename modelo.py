class Cartao:
    def __init__(self, codigo, numero):
        self.codigo = codigo
        self.numero = numero

class Centro:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

class Credor:
    def __init__(self, codigo, credor):
        self.codigo = codigo
        self.credor = credor

class Classificacao:
    def __init__(self, codigo, classificacao):
        self.codigo = codigo
        self.classificacao = classificacao
    
class Lancamento:
    def __init__(self, codigo_lancamento, data_compra, vencimento, credor, documento, ano, parcela, valor, classificacao, centro_custo, cartao):
        self.codigo_lancamento = codigo_lancamento
        self.data_compra = data_compra
        self.vencimento = vencimento
        self.credor = credor
        self.documento = documento
        self.ano = ano
        self.parcela = parcela
        self.valor = valor
        self.classificacao = classificacao
        self.centro_custo = centro_custo
        self.cartao = cartao