from random import randint
import math

# Função para calcular a distância do ponto até a origem
def calcular_distancia(x, y):
    distancia = math.sqrt(x ** 2 + y ** 2)
    return distancia

# Função calcular
def calcular(lista):
    if not lista: # Verfica se a lista está vazia 
            return
    
    # Calcula a distância para cada ponto
    distancia = [(ponto, calcular_distancia(ponto[0], ponto[1])) for ponto in lista]
    print(distancia)

    # Obtém o ponto mais distante da origem 
    mais_distante = max(distancia, key=lambda x : x[1])
    print(f"Ponto mais distante da origem: {mais_distante}")

    # Obtém o ponto mais próximo da origem 
    mais_proximo = min(distancia, key=lambda x : x[1])
    print(f"Ponto mais proximo da origem: {mais_proximo}")

    # Obtém a média de todas as distâncias
    soma = sum([d[1] for d in distancia])
    media = soma / len(distancia)
    print(f"Media das distâncias: {media}")

# Programa principal
lista = []
for i in range(5):
    x = randint(-10, 10)
    y = randint(-10, 10)
    lista.append((x, y))

print("Pontos:", lista)
calcular(lista)
