"""
Cria uma lista
Lê cada item da lista e determina se o número é par e calcula a média de numeros pares
"""
soma_pares = 0 # cria uma variavel para armazenar os numeros pares
cont_pares = 0 # cria uma variavel para armazenar o total de numeros pares encontrados

for numero in range(1,11,1): # cria uma range do 1 ao 10 com incremento 1
    if numero%2 == 0: # verifica se o resto da divisão por 2 é 0
        print(f'{numero} é par')
        soma_pares = soma_pares + numero
        cont_pares += 1 # incrementa o contador de numeros pares
    else:
        continue # função auxiliar que pula a interação do for para o próximo contador

print(f'A soma dos números pares foi {soma_pares}')
print(f'A quantidade de números pares foi {cont_pares}')
print(f'A média dos números pares foi {soma_pares/cont_pares}')