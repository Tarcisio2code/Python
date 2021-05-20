def fibo(n):
    'Determina o n-ésimo termo da sequência de Fibonacci' # declaração da docstring
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(help(fibo))