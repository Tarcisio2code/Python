import os
#Biblioteca de erros do Ptyhon
import errno

## Tratamento para o erro: arquivo não existe
print('Abrindo um arquivo')
try:
    open("teste.txt", "r")
    print("Arquivo Aberto")
except FileNotFoundError as erro:
    print("Arquivo não existe")
    print(" Descrição", erro)

print("Término do programa\n")

# Tratamento para o erro: arquivo esta aberto em outro programa
print("Abrindo um arquivo")
try:
    open("teste.pdf", 'w')
    print("Arquivo Aberto")
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print(" Descrição", erro)

print("Término do programa\n")

# Tratamento de erros na exclusão de arquivos
try:
    os.remove("teste.txt")
    print("Arquivo removido!")
except FileNotFoundError as erro:
    print("Arquivo não existe")
    print(" Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print(" Descrição", erro)
except IsADirectoryError as erro:
    print("Remove serve apenas para arquivos")
    print(" Descrição", erro)
print("Término do programa\n")

# Tratamento de erros ao renomear arquivos
try:
    os.rename("teste.pdf", "teste_renomeado.pdf")
    print("Arquivo renomeado!")
except FileNotFoundError as erro:
    print("Arquivo não existe")
    print(" Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print(" Descrição", erro)
except FileExistsError as erro:
    print("Arquivo destino já existe")
    print(" Descrição", erro)
print("Término do programa\n")

# Tratamento de erros ao manipular diretórios
try:
    os.mkdir("novo_diretorio")
    print("Diretório criado!")
except PermissionError as erro:
    print("Sem permissão para criar diretório")
    print(" Descrição", erro)
except FileExistsError as erro:
    print("Diretório já existe")
    print(" Descrição", erro)
print("Término do programa\n")

try:
    os.rmdir("novo_diretorio")
    print("Diretório removido!")
except FileNotFoundError as erro:
    print("Diretorio não existe")
    print(" Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para remover o diretório")
    print(" Descrição", erro)
except OSError as erro:
    print("Outro erro.")
    print("O diretório está vazio?")
    print(" Descrição", erro)
print("Término do programa\n")

#Tratamento de erros utilizando a biblioteca errno
try:
    os.rmdir("novo_diretorio")
    print("Diretório removido")
except OSError as erro:
    print(f'código errno do erro: {erro.errno}')
    if erro.errno == errno.ENOTEMPTY:
        print("O diretório não está vazio")
    else:
        print("Erro Inesperado!")
    print(" Descrição", erro)
print("Término do programa\n")

# Tratamento de erros ao verificar o conetudo de pastas
try:
    entradas = os.scandir("novo_diretorio")

    for obj in entradas:
        print(obj)
        print(f'Nome: {obj.name}')
        print(f'Caminho: {obj.path}')
        print(f'É diretório: {obj.is_dir()}')
        print(f'É arquivo: {obj.is_file()}')
        if obj.is_file():
            print(f'Tamanho: {obj.stat().st_size} B')
        print("====================================")
except FileNotFoundError:
    print("O caminho não existe.")
except NotADirectoryError:
    print("O caminho não é de um diretório.")