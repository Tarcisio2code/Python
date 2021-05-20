"""
Uso das instuções Try e Except para evitar um erro de execução caso
o usuário entre com um texto no lugar de um número.
"""

try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except:
    print("Entre com o valor numérico e não letras")