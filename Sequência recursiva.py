import random


#Função para pesquisa binária
def pesquisar(lista, valor, index = 0):
    if index >= len(lista):
        return -1
    if lista[index] == valor:
        return index
    else:
        return pesquisar(lista, valor, index + 1)
 

#Programa principal
lista = []
for i in range(20):
    lista.append(random.randint(1, 15))

indice = pesquisar(lista, 10)
print(indice)
