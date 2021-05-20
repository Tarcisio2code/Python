import sqlite3 as conector

#Cria um banco de dados somente na memória
#conexaoMemory = conector.connect(':memory:')

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("banco_de_dados.db")

except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)

finally:
    #fechamento das conexões e cursores
    if conexao:
        conexao.close()
