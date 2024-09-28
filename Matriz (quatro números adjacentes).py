def produto(matriz, matriz_tamanho):
    maior_produto = 0

    for i in range(matriz_tamanho):
        for j in range(matriz_tamanho - 3):
            produto = matriz[i][j] * matriz[i][j+1] * matriz[i][j+2] * matriz[i][j+3]
            if produto > maior_produto:
                maior_produto = produto

    for i in range(matriz_tamanho - 3):
        for j in range(matriz_tamanho):
            produto = matriz[i][j] * matriz[i+1][j] * matriz[i+2][j] * matriz[i+3][j]
            if produto > maior_produto:
                maior_produto = produto

    for i in range(matriz_tamanho - 3):
        for j in range(matriz_tamanho - 3):
            produto = matriz[i][j] * matriz[i+1][j+1] * matriz[i+2][j+2] * matriz[i+3][j+3]
            if produto > maior_produto:
                maior_produto = produto

    for i in range(matriz_tamanho - 3):
        for j in range(3, matriz_tamanho):
            produto = matriz[i][j] * matriz[i+1][j-1] * matriz[i+2][j-2] * matriz[i+3][j-3]
            if produto > maior_produto:
                maior_produto = produto

    return maior_produto

tamanho = int(input("Digite o tamanho da matriz quadrada: "))

matriz = []

print("Digite os valores da matriz (sempre dando espaço de um valor para o outro):")
for i in range(tamanho):
    linha = list(map(int, input(f"Digite a linha {i+1}: ").split()))
    matriz.append(linha)

print("\nMatriz:")
for linha in matriz:
    print(linha)

resultado = produto(matriz, tamanho)

print(f"\nO maior produto de quatro números adjacentes é: {resultado}")
