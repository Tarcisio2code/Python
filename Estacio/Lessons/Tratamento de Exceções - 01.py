try:
    numerador = eval(input("Entre com o numerador da fração: "))
    denominador = eval(input("Entre com o denominador da fração: "))
    print(f'A divisão vale {numerador/denominador}') # se o denomidador for 0 será retornado erro

except ZeroDivisionError:
    print("O valor do denominador não pode ser igual à 0")
except NameError:
    print("Os valores informados não são números")
except:
    print("Não foi possivel executar a operação")