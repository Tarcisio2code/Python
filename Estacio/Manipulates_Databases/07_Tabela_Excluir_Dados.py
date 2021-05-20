import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("banco_de_dados.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # Execução dos comandos de manipulação do banco de dados
    comando1 = '''DELETE FROM Pessoa WHERE cpf=12345678900'''
    cursor.execute(comando1)

    # Teste de restrição de chave estrangeira
    # retorna exceção caso o PRAGMA esteja on, o atributo esta vinculado em outra tabela
    # comando2 = '''DELETE FROM Pessoa WHERE cpf=10000000099'''
    # cursor.execute(comando2)

    # Efetivação dos comandos
    conexao.commit()

except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)

finally:
    #fechamento das conexões e cursores
    if conexao:
        cursor.close()
        conexao.close()