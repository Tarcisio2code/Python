"""
Solicita um número ao usuário
Determina se o número é par ou impar
"""
numero = eval(input("Entre com um número positivo: "))

if numero%2 == 0: # verifica se o resto da divisão por 2 é 0
    print("O número informado é par")
else:
    print("O número informado é ímpar")