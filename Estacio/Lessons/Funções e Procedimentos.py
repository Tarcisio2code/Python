def func1(x):
    x = 10
    print(f'Função func1 - x = {x}') # não existe um retorno, o valor é apenas exibido na tela


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')
