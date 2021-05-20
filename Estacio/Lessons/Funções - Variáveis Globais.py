def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')


def func2():
    global x
    x = 20                              # este será sempre o ultimo valor de x, pois é a ultima função chamada.
    print(f'Função func2 - x = {x}')


x = 0 # mesmo definindo um valor para x, por ser global, o valor será o informada na ultima função executada
func1()
func2()
print(f'Programa principal - x = {x}')
