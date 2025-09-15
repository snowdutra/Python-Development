from timeit import timeit

# Função recursiva para calcular o número de fibonacci
def fibo(index):
    x, y = 1, 1
    if index == 1 or index == 1:
        return 1
    
    for i in range(3, index + 1):
        z = y + x
        x = y
        y = z
    
    return z


tempo = timeit("fibo(40)", globals=globals(), number=1000)
#/index = int(input("Informe a posição:    "))
#numero = fibo(index)
#print(numero)
print(tempo)
