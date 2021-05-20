import sqlite3 as conector
import pandas

from funcoes import recuperar_veiculos, conv_bool
from modelo import Pessoa, Veiculo
from datetime import date

conexao = None
cursor = None
try:
    # Informar o argumento PARSE_DECLTYPES para permitir a conversão de tipos
    conexao = conector.connect("banco_de_dados.db", detect_types=conector.PARSE_DECLTYPES)
    cursor = conexao.cursor()

    conector.register_converter("BOOLEAN", conv_bool)

    comando = '''SELECT nome, oculos FROM Pessoa;'''
    cursor.execute(comando)

    # Recupera todos os registros
    registros = cursor.fetchall()
    print("Tipo retornado pelo método fetchall():", type(registros))

    for registro in registros:
        print(f'Tipo: {type(registro)} - Conteúdo: {registro}')

    # Recupera apenas registros que atendem a condição
    comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''
    cursor.execute(comando, {"usa_oculos": True})
    registros = cursor.fetchall()

    print("\nPessoas que usam óculos")
    for registro in registros:
        # O operador '*' desempacota um iterável, passando cada elemento como um argumento para o construtor.
        pessoa = Pessoa(*registro)
        print("cpf:", type(pessoa.cpf), pessoa.cpf)
        print("nome:", type(pessoa.nome), pessoa.nome)
        print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
        print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)

    # Junção de Tabelas
    print()
    comando = '''SELECT
                    Veiculo.placa, Veiculo.ano, Veiculo.cor,
                    Veiculo.motor, Veiculo.proprietario,
                    Marca.nome FROM Veiculo JOIN Marca ON Marca.id = Veiculo.marca;'''

    cursor.execute(comando)
    re_veiculos = cursor.fetchall()
    for re_veiculo in re_veiculos:
        veiculo = Veiculo(*re_veiculo)
        print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)

    #
    print()
    comando = '''SELECT * FROM Pessoa;'''
    cursor.execute(comando)

    pessoas = []
    reg_pessoas = cursor.fetchall()
    for reg_pessoa in reg_pessoas:
        pessoa = Pessoa(*reg_pessoa)
        pessoa.veiculos = recuperar_veiculos(conexao, pessoa.cpf)
        pessoas.append(pessoa)

    for pessoa in pessoas:
        print(pessoa.nome)
        for veiculo in pessoa.veiculos:
            print('\t', veiculo.placa, veiculo.marca.nome)
    #
    print("\nRetorno do fetchall para uma pesquisa vazia")
    comando = '''SELECT * FROM Pessoa WHERE cpf == 0'''
    cursor.execute(comando)

    pessoas = cursor.fetchall()
    print(type(pessoas))

    # Funções da biblioteca Pandas
    print("\nDados recuperados utilizando a Bibliotéca Pandas;")
    comando = '''SELECT * FROM Pessoa;'''
    resultado = pandas.read_sql(sql=comando, con=conexao)
    print(resultado)

    # Adcionando uma coluna e efetuando cálculos
    Hoje = date.today()
    resultado['Idade'] = Hoje - resultado['nascimento']
    print("\n", resultado)


except conector.DatabaseError as erro:
    print("Erro de Banco de Dados")

finally:
    if conexao:
        cursor.close()
        conexao.close()
