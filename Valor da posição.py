# Dicionário global para "lembrar" dos valores calculados
cache = {0 : 0, 1 : 1 }


# Função recursiva para calcular o valode uma posicõa do fibonnaci 
def fib(n):
    # Se o valor já foi calculado, retorne o valor da cache
    if n in cache:
        return cache[n]
    # Se o valor não foi calculado, calcule-o e adicione a cache
    else:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]


# Função principal
print(fib(50))
