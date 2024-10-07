import pandas as pd
import database

conn = database.conexao
cursor = conn.cursor()

def tab2df(conn):
    query = """
        select * from lancamento
    """
    cursor.execute(query)
    df = pd.read_sql_query(query, conn)
    return df
    

df1 = tab2df(conn)
df1.to_excel("lancamentos.xlsx")
    

    
