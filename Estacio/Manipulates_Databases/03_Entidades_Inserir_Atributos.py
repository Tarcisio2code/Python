import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursos
    conexao = conector.connect("banco_de_dados.db")
    cursor = conexao.cursor()

    # Execução dos comandos de manipulação do banco de dados
    comando = '''ALTER TABLE Veiculo
                    ADD motor REAL;'''

    cursor.execute(comando)

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as erro:
    print("Erro de banco de dados", erro)

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
