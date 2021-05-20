def calculaDelta(coef1,coef2,coef3):
    #formula da equação de 2º é b^2 - 4.a.c
    delta = coef2*coef2 - 4*coef1*coef3
    return delta

a = eval(input("Entre com o coeficiente A da equação: "))
b = eval(input("Entre com o coeficiente B da equação: "))
c = eval(input("Entre com o coeficiente C da equação: "))

delta = calculaDelta(a,b,c)

print(f'O valor calculado do Delta foi {delta}')

"""
Se delta > 0 : a equação tem 2 raizes reais
Se delta = 0 : a equação tem 1 raiz real
Se delta < 0 : a equação não tem raiz real
"""
if delta > 0:
    print("A equação tem 2 raizes reais.")
elif delta == 0:
    print("A equação tem 1 raiz real.")
else:
    print("A equação não tem raiz real.")

