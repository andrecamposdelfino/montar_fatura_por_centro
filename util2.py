import pandas as pd

df = pd.read_excel('mes10.xlsx')
valor = ['valor']
centro = ['centro-custo']
soma = df.groupby([valor,centro]).sum()
print(soma)