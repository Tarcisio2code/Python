from datetime import datetime

print("***> Exemplos do método STRIP <***\n")
with open("dados.txt", "r") as arquivo:
    print(f"Conteudo original do arquivo {arquivo.name}")
    for linha in arquivo:
        print(repr(linha))

# Metodo strip remove espaços e caracteres de final de linha
with open("dados.txt", "r") as arquivo:
    print(f"\nConteudo do arquivo {arquivo.name} após utilizar o método strip")
    for linha in arquivo:
        print(repr(linha.strip()))

# Identificando as linhas com cont
with open("dados.txt", "r") as arquivo:
    cont = 0
    for linha in arquivo:
        if linha:
            cont += 1
    print("\nTotal de linhas no arquivo = ", cont)

with open("dados.txt", "r") as arquivo:
    cont = 0
    for linha in arquivo:
        if linha.strip():
            cont += 1
    print("\nTotal de linhas COM conteúdo no arquivo = ", cont)

## Método count
print("***> Exemplos do método COUNT <***")
with open("dados.txt") as arquivo:
    conteudo = arquivo.read()
    contador = conteudo.count("Ola")
    print("\nTotal de Olas = ", contador)

## Método split
print("***> Exemplos do método SPLIT <***\n")
# sem parametro, separador padrão é espaço
frase1 = "\nEu amo comer amoras no café da manhã"
lista_termos1 = frase1.split()
print(lista_termos1)

frase2 = "Amora  abacaxi    abacate     banana"
lista_termos2 = frase2.split()
print(lista_termos2)

# parametro de divisão como separador ','
frase3 = "Carro, moto, avião"
lista_termos3 = frase3.split(',')
print(lista_termos3)

# Melhorando a contagem de strings
frase = "\nEu amo comer amoras no café da manhã"
print(frase)
print("Contagem da palavra 'amo' sem quebra da frase = ", frase.count("amo"))

contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == "amo":
        contador += 1
print("Contagem da palavra 'amo' com quebra da frase = ", contador)

# Método count direto no objeto com a lista de strings, despeça a utilização do For
print("Contagem da palavra 'amo' com quebra da frase = ", lista_termos.count("amo"))

## Método Join
print("***> Exemplos do método JOIN <***\n")

minha_lista =['Arroz', 'Feijao', 'Macarrao']

#utilizando a ',' como conector
texto1 = ','.join(minha_lista)
with open('texto1.txt', 'w') as arquivo:
    arquivo.write(texto1)

#utilizando '\n' como conector
texto2 = '\n'.join(minha_lista)
with open('texto2.txt', 'w') as arquivo:
    arquivo.write(texto2)

## Método fString
print("***> Exemplos do método fSTRING <***\n")

nome = 'Bianca'

string0 = "Ola, " + nome + "."
#aplicando o fString...
string1 = f"Ola, {nome}."
string2 = f"Ola, {nome.upper()}."
string3 = f"{nome} tem {5 + 5} anos."
string4 = f"\nO numero 2 é maior que 1? {2 > 1}."
string5 = f"O numero 2 esta na lista [4, 5, 6]? {2 in [4, 5, 6]}."

print(string0)
print(string1)
print(string2)
print(string3)
print(string4)
print(string5)

#fString com formatação,float e datas
frutas = ['Jabuticaba', 'Laranja', 'Uva', 'Banana']
for fruta in frutas:
    minha_fruta = f"Nome: {fruta:12} - Número de letras: {len(fruta):3}"
    print(minha_fruta)

pi = 3.1415
meu_numero = f"\nO número PI é {pi:.1f}"
meu_numero_deslocado = f"O número PI deslocado é: {pi:6.1f}"
meu_numero_preciso = f"O Número PI mais preciso é: {pi:.4f}"
print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

data = datetime.now()
minha_data = f"\nA data de hoje é {data}"
minha_data_formatada = f"A data de hoje formatada é {data:%d/%m/%Y}"
print(minha_data)
print(minha_data_formatada)