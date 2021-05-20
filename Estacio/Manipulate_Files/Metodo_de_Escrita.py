## Métodos para escrita em arquivos

#Modo 'w' remove o conteudo do arquivo durante a abertura
#Método write
arquivo_escrita = open("documentos\dados2.txt", "w")
arquivo_escrita.write("Conteudo da primeira linha.\n")
arquivo_escrita.write("Conteudo da segunda linha.")
arquivo_escrita.close()

arquivo = open("documentos\dados2.txt")
conteudo = arquivo.read()
print(repr(conteudo), "\n")
arquivo.close()

#Método writelines
linhas = ["Conteudo da primeira linha.",
          "\nConteudo da segunda linha."]

arquivo_escrita = open("documentos\dados3.txt", "w")
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()

arquivo = open("documentos\dados3.txt")
conteudo = arquivo.read()
print(repr(conteudo), "\n")
arquivo.close()

#Modo 'a' permite adicionar conteudo em um arquivo
linhas = ["\nConteudo da terceira linha.",
          "\nConteudo da quarta linha."]

arquivo_escrita = open("documentos\dados3.txt", "a")
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()

arquivo = open("documentos\dados3.txt")
conteudo = arquivo.read()
print(repr(conteudo), "\n")
arquivo.close()

#Palavra reservada 'with' dispensa o método close
with open("documentos\dados3.txt") as arquivo:
    for linha in arquivo:
        print(linha)
    print("\nFim do arquivo", arquivo.name)
