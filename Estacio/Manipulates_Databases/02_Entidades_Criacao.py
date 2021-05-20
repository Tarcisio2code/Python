import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("banco_de_dados.db")
    cursor = conexao.cursor()

    # Execução dos comandos de manipulação do banco de dados
    comando1 = '''CREATE TABlE Pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
                    );'''

    comando2 = '''CREATE TABlE Marca (
                    id INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    sigla CHARACTER(2) NOT NULL,
                    PRIMARY KEY (id)
                    );'''

    comando3 = '''CREATE TABlE Veiculo (
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa)
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) REFERENCES Marca(id)
                    );'''

    cursor.execute(comando1)
    cursor.execute(comando2)
    cursor.execute(comando3)

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)

finally:
    #fechamento das conexões e cursores
    if conexao:
        cursor.close()
        conexao.close()