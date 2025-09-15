valor = []


for i in range(0, 5):
    x = int(input("Digite o valor para a posição: "))
    valor.append(x)

pares = 0
impares = 0

for x in valor:
    if x % 2 == 0:
        pares += 1
    else:
        impares += 1

total = len(valor)
pa = (pares / total) * 100
pi = (impares / total) * 100

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Porcentagem de números pares: {pa:.2f}%")
print(f"Porcentagem de números ímpares: {pi:.2f}%")

