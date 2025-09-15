# Função recursiva para calcular o número de fibonacci
def fibo(index):
    # Caso base da recurão
    if index <= 2:
        return 1
    return fibo(index - 1) + fibo(index - 2 )

index = int(input("Informe a posição:    "))
numero = fibo(index)
print(numero)
