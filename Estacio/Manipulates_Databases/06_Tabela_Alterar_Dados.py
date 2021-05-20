import  sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    conexao.execute("PRAGMA foreign_keys = on")

    # Execução dos comandos de manipulação do banco de dados
    # comando sem argumentos
    comando1 = '''UPDATE Pessoa SET oculos=1;'''
    cursor.execute(comando1)

    # comando com argumentos não nomeados
    comando2 = '''UPDATE Pessoa SET oculos= ? WHERE cpf=30000000099;'''
    cursor.execute(comando2, (False,))

    # comando com argumentos nomeados
    comando3 = '''UPDATE Pessoa SET oculos= :usa_oculos WHERE cpf= :cpf;'''
    cursor.execute(comando3, {"usa_oculos": False, "cpf": 20000000099})

    # teste de restrição de chave estrangeira
    # retorna exceção caso o PRAGMA esteja on
    # comando4 = '''UPDATE Veiculo SET proprietario=0 WHERE proprietario=10000000099'''
    # cursor.execute(comando4)

    # Efetivação dos comandos
    conexao.commit()

except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)

finally:
    #fechamento das conexões e cursores
    if conexao:
        cursor.close()
        conexao.close()