import sqlite3 as conector

#Classe para utilização dos parametros dinamicos
from modelo import Pessoa
from modelo import Marca
from modelo import Veiculo

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    # Ativa a restição de chave estrangeira
    conexao.execute("PRAGMA foreign_keys = on")

    # Execução dos comandos de manipulação do banco de dados

    # Limpa tabela pessoa para evitar erro
    comando0 = '''DELETE FROM Pessoa;'''
    cursor.execute(comando0)
    conexao.commit()

    comando1 = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                    VALUES (12345678900, 'João', '2000-01-31', 1);'''
    cursor.execute(comando1)

    ## Utilizando parâmetros dinâmicos
    pessoa = Pessoa(10000000099, 'Maria', '1990-01-31', 0)
    comando2 = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                    VALUES (?, ?, ?, ?);'''
    cursor.execute(comando2, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

    ## Utilizando Argumentos nomeados
    ## As colunas podem ser suprimidas caso todos os atributos sejam informados
    pessoa = Pessoa(20000000099, 'José', '1990-02-28', False)
    comando3 = '''INSERT INTO Pessoa
                    VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
    cursor.execute(comando3, {"cpf": pessoa.cpf,
                              "nome": pessoa.nome,
                              "data_nascimento": pessoa.data_nascimento,
                              "usa_oculos": pessoa.usa_oculos})

    ## Utilizando a função vars para converter objeto em dicionáro
    pessoa = Pessoa(30000000099, 'Silva', '1990-03-30', True)
    comando4 = '''INSERT INTO Pessoa
                    VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
    cursor.execute(comando4, vars(pessoa))

    ## Povoando as demais tabelas
    comando5 = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''
    marca1 = Marca("Marca A", "MA")
    cursor.execute(comando5, vars(marca1))
    marca1.id = cursor.lastrowid

    marca2 = Marca("Marca B", "MB")
    cursor.execute(comando5, vars(marca2))
    marca2.id = cursor.lastrowid

    comando6 = '''INSERT INTO Veiculo
                    VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''
    veiculo1 = Veiculo('AAA0001', 2001, 'Prata', 1.0, 10000000099, marca1.id)
    veiculo2 = Veiculo('BAA0002', 2002, 'Preto', 1.4, 10000000099, marca1.id)
    veiculo3 = Veiculo('CAA0003', 2003, 'Branco', 2.0, 20000000099, marca2.id)
    veiculo4 = Veiculo('DAA0004', 2004, 'Azul', 2.2, 30000000099, marca2.id)
    cursor.execute(comando6, vars(veiculo1))
    cursor.execute(comando6, vars(veiculo2))
    cursor.execute(comando6, vars(veiculo3))
    cursor.execute(comando6, vars(veiculo4))

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as erro:
    print("Erro de banco de dados", erro)

finally:
    # fechamento das conexões e cursores
    if conexao:
        cursor.close()
        conexao.close()