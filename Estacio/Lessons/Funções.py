"""
19-11-20: Tarcisio Silva
Na versão original da Estacio foi utlizado somente input para receber os dados,
o que provoca um erro de execução na linha 8.
Inclui a função eval para converter o valor de entrada em númerico, corrigindo o erro.
"""
escolha = eval(input("Escolha uma opção de função ( 1 ou 2 ) : "))
if escolha == 1:
    def func1(x):
        return x + 1
else:
    def func2(x):
        return x + 2

s = func1(10)
print(s)
