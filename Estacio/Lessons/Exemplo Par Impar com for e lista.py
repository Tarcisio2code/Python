"""
Cria uma lista
Lê cada item da lista e determina se o número é par ou impar
"""
for numero in range(1,11,1): # cria uma range do 1 ao 10 com incremento 1
    if numero%2 == 0: # verifica se o resto da divisão por 2 é 0
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')