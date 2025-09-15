# Ordenação pelo método mergesort

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i, j = 0, 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado




lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
lista_ordenada = merge_sort(lista)
print(lista_ordenada)
