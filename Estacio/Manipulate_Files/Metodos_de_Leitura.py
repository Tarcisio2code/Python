## Métodos para leitura de arquivos
# especifiando o modo de leitura (r = read)
arquivo = open("dados1.txt", "r")

#método Read
conteudo = arquivo.read()
print("Exibindo conteudo do arquivo", arquivo.name)
print("Tipo do conteúdo:", type(conteudo))
print("Conteúdo retornado pelo read:")
print(repr(conteudo), "\n")
# Fechando o arquivo para reposicionar o cursor na linha 0 na próxima abertura
arquivo.close()

#Método Readline
arquivo = open("dados1.txt", "r")
primeiraLinha = arquivo.readline()
segundaLinha = arquivo.readline()

print("Conteúdo retornado pelo readline:")
print(repr(primeiraLinha))

print("Próximo conteúdo retornado:")
print(repr(segundaLinha), "\n")

#Método Readlines
#reposicionado o cursor na primeira linha do arquivo
arquivo.seek(0)
conteudo = arquivo.readlines()
print("Exibindo conteudo do arquivo", arquivo.name)
print("**Tipo do conteúdo:", type(conteudo))
print("Conteúdo retornado pelo readlines:")
print(repr(conteudo), "\n")

#Exibindo uma quantidade especifica de bytes
arquivo.seek(0)
arquivo = open("dados1.txt")
primeirosBytes = arquivo.read(3)
print("Arquivo : ", arquivo.name)
print("Exibindo os 3 primeiros caracteres lidos:")
print(primeirosBytes)
arquivo.close()
