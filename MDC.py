def mdc(m, n):
    if n > m:
        return mdc(n, m)
    
    if n == 0:
        return m
    
    return mdc(n, m % n)


m = int(input("Insira o número da variavel M:  "))
n = int(input("Insira o número da variavel N: "))


resultado = mdc(m, n)
print(f'O MDC entre {m} e {n} é {resultado}')

