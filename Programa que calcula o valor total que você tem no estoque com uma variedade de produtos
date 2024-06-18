produto = []
estoque = []
valor_unitario = []

total = int(input("Tipos de produtos:   "))
maior = 0

for i in range(0, total):
        produto.append(input("Nome do produto:  "))
        estoque.append(int(input("Quantidade em estoque:    ")))
        valor_unitario.append(float(input("Valor:     ")))
        if valor_unitario[i] > maior:
                maior = valor_unitario[i]


# item a --> Produtos que tem o maior valor 

for i in range (0, total):
        if valor_unitario[i] == maior:
                print(produto[i])

# item b --> Valor total de cada produto

valorTotal = 0
for i in range (0, total):
    print(f"{produto[i]} = R$ {estoque[i] * valor_unitario[i]}")
    valorTotal += estoque[i] * valor_unitario[i]

# item c 
print(f"Valor total do estoque = R$ {valorTotal}")
