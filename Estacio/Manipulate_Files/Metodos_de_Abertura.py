import os

## Exemplo da funcão Open
arquivo = open("dados1.txt")
print(f'Arquivo {arquivo.name} aberto com sucesso!\n')

## Exemplo de tipos de caminho de arquivo
# Caminho relativo
arquivo1 = open("dados1.txt")

# Caminho absoluto
#arquivo2 = open("C:\Users\Tarcisio\Documents\Estacio\Phyton\Manipulacao_de_Arquivos\dados1.txt")

# Caminho relativo
#arquivo3 = open("documentos\dados2.txt")

# Caminho absoluto
#arquivo4 = open("C:\Users\Tarcisio\Documents\Estacio\Phyton\Manipulacao_de_Arquivos\documentos\dados2.txt")
print("Exemplos de exibição de caminhos de arquivo...\n")
print(f' Caminho relativo do arquivo {arquivo1.name} : {os.path.relpath(arquivo1.name)}')
print(f' Caminho absoluto do arquivo {arquivo1.name} : {os.path.abspath(arquivo1.name)}\n')
print(f'Representação do objeto {arquivo1.name} ; \n {arquivo1}')
print(" /                 /                 /         |______")
print(" |tipo do objeto,  |nome do arquivo, |modo de acesso, |codificação\n")

#Exibindo atributos do objeto
print("Nome do arquivo", arquivo1.name)
print("Modo do arquivo", arquivo1.mode)
print(f'Arquivo fechado ?, {arquivo1.closed} \n')

#Fechado um arquivo
arquivo1.close()
print("Arquivo fechado ?", arquivo1.closed, "\n\n")
