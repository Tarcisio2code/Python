# Biblioteca para manipulação de planilhas
import pandas

import principal

variaveis = principal.extrair_variaveis("dados/dicionario_pessoas.xls")

# Cria uma lista com cada tipo de variável
colunas = [str(variavel) for variavel in variaveis]
# for linha in colunas:
#     print(linha)
linhas = []
with open("dados/pessoas_2015.txt") as microdados:
    for idx, linha in enumerate(microdados):
        # print("++++++++++++++++++++++++++++ NOVA LINHA ++++++++++++++++++++++++++++")
        nova_linha = []
        for variavel in variaveis:
            # print(variavel)
            # print(variavel.categoria)
            #Aplicado o metodo strip para recortar o conetudo da celula
            valor = linha[variavel.posicao_inicial:variavel.posicao_inicial + variavel.tamanho].strip()
            if valor:
                valor = int(valor)
            # print('\t', valor, '-', variavel.categoria.get(valor))
            valor_final = variavel.categoria.get(valor) if variavel.categoria.get(valor) else valor
            nova_linha.append(valor_final)

        linhas.append(nova_linha)

        #limita o número de linhas lidas
        if idx > 1000:
            break
#
df = pandas.DataFrame(linhas, columns=colunas)
print(f'total de linhas, colunas gerados = {df.shape}')
df.to_csv('resultado/microdados.csv', sep=';')
