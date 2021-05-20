from modelo import Veiculo, Marca

# Função para converter os campos booleanos
def conv_bool(dado):
    return True if dado == b'1' else False

def recuperar_veiculos(conexao, cpf):
    cursor = conexao.cursor()

    comando = '''SELECT * FROM Veiculo
                JOIN Marca ON Marca.id = Veiculo.marca
                WHERE Veiculo.proprietario = ?;'''
    cursor.execute(comando, (cpf,))

    veiculos = []
    registros = cursor.fetchall()
    for registro in registros:
        marca = Marca(*registro[6:])
        veiculo = Veiculo(*registro[:5], marca)
        veiculos.append(veiculo)

    cursor.close()
    return veiculos