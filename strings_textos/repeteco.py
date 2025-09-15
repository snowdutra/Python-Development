# Função para verificar se tem palavra repetida na lista
def achar_repeteco(lista):
    aux ={}
    for p in lista:
        if p in aux:
            return True
        aux[p] = 1

# Programa principal
lista = ['aula', 'desespero', 'doritos', 'martech', 'caps'] 
print (achar_repeteco(lista))
