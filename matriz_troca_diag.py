from random import randint

# Ordem da matriz -- > matriz quadrada (total de linhas = total de colunas)
ordem = 3

# Geração da matriz 
matriz = []
for i in range(ordem):
    linha = []
    for j in range(ordem):
        linha.append(randint(0,50))
    matriz.append(linha)

# Impressão da matriz em formato tabular
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end='\t')
    print()

# Troca das diagonais
j = len(matriz) - 1
for i in range(len(matriz)):
    temp = matriz[i][i]
    matriz[i][i] = matriz[i][j]
    matriz[i][j] = temp
    j = j - 1  #j -= 1 

# Impressão da matriz em formato tabular
print()
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end='\t')
    print()
