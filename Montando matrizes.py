
matriz = []

ordem = int(input("Insira a ordem da matriz: "))

print("Insir o valor da matriz:")

for i in range(ordem):
    linha = []
    for k in range(ordem):
        valor = int(input(f"Digite o valor da posição {k}: "))
        linha.append(valor)
    matriz.append(linha)


print("\n Matriz:")
for linha in matriz:
    print(linha)

diagonal_principal = 0
for i in range(ordem):
    diagonal_principal += matriz[i][i]

diagonal_secundaria = 0
for i in range(ordem):
    diagonal_secundaria += matriz[i][ordem - 1 - i]

print(f"\n A Soma dos elementos da diagonal principal é igual a: {diagonal_principal}")
print(f"\n A Soma dos elementos da diagonal secundária é igual a: {diagonal_secundaria}")
