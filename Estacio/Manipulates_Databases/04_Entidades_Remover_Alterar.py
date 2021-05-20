import sqlite3 as conector

## Exclusão da tabela veiculo e para reordenar o novo atributo 'motor'

try:
    # Abertura de conexão e aquisição de cursos
    conexao = conector.connect("banco_de_dados.db")
    cursor = conexao.cursor()

    # Execução dos comandos de manipulação do banco de dados
    comando1 = '''DROP TABLE Veiculo;'''

    cursor.execute(comando1)

    comando2 = '''CREATE TABlE Veiculo (
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                motor REAL NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY (placa)
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id)
                );'''

    cursor.execute(comando2)

    # Efeticação do comando
    conexao.commit()

except conector.DatabaseError as erro:
    print("Erro de banco de dados", erro)

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
