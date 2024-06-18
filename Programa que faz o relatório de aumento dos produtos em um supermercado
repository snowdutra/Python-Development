produtos = int(input("Digite a quantidade de produtos: "))

valor = {}

for i in range(produtos):
    nome = input("Digite o nome do produto: ")
    anterior = float(input(f"Digite o valor anterior do produto {nome}: "))
    atual = float(input(f"Digite o valor atual do produto {nome}: "))

    absoluto = atual - anterior
    percentual = (absoluto / anterior) * 100
    valor[nome] = percentual

print("Relatório de aumento de produtos:")

for produto in valor:
    aumento = valor[produto]
    print(f"O Produto {produto} teve um aumento de: {aumento:.2f}%")
