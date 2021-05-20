try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except NameError:
    print("Entre com o valor numérico e não letras")