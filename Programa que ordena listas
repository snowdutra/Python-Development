import random 

# Funçõo
def preencher_vetor():
    i = 0
    while (i < 10):
        aux = random.randint(1, 8)
        if aux not in lista:
            lista.append(aux)
            i += 1

def ordenar():
    for _ in range(len(lista)):
        for i in range(len(lista - 1)):
            if lista[i] > lista[i + 1]:
                aux  = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux


#Código Pronto
lista = []

preencher_vetor()
print(lista)

ordenar() 
print(lista)

