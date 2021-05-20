# Programa para calcular o indice de massa corporia

# Recebendo o peso e a altura do usuário
peso = eval(input("Informe o seu peso: "))
altura = eval(input("Informe a sua altura: "))

# Calculando o IMC
imc = peso / altura**2

# Retornando o IMC
# print("Seu IMC é " , imc)
# Melhorando o codigo de saida com 'f'
print(f'Seu IMC é {imc}')
