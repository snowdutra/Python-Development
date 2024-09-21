#Função para agrupar as palavras por tamanho
def agrupar(agrupamento, lista):
    for palavra in lista:
        tamanho = len(palavra)
        if tamanho not in agrupamento:
            agrupamento[tamanho] = []
        agrupamento[tamanho].append(palavra)
    print(agrupamento)


#Programa principal
agrupamento = {}
lista = []
for i in range(5):
    lista.append(input("Palavra"))


agrupar(agrupamento, lista)
