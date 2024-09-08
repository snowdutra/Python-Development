def potencia(x, n):
    if n == 0:
        return 1

    return x * potencia(x, n - 1)


x = int(input("Insira o valor de X: "))

n = int(input("Insira o valor de N: "))

resultado = potencia(x, n)

print(f'{x}^{n} = {resultado}')
