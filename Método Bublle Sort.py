def bolha(v):
    totalderepeticao = 0
    totaldetroca = 0
    for j in range(len(v)):
        for i in range(len(v) - 1):
            totalderepeticao += 1
            if v[i] > v[i + 1]:
                totaldetroca += 1
                aux = v[i]
                v[i] = v[i + 1] 
                v[i + 1] = aux
    print(f"total de repeticoes: {totalderepeticao}")
    print(f"total de trocas: {totaldetroca }")

  

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bolha(lista)

