"""
Atenção, esta função cria um loop infinito, pois não foi tratada a saida da função.
"""
def regressiva(x):
    print(x)
    regressiva(x - 1)
