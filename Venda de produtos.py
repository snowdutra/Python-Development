from random import randint

# Variáveis globais
categoria = ["Eletrônico", "Roupa", "Alimento"]
mes = ["Janeiro", "Fevereiro", "Março", "Abril"]
venda = [[0 for _ in range(len(mes))] for _ in range(len(categoria))]


# Função para entrada dos dados das vendas
def ler_dados():
    for i in range(len(categoria)):
        for j in range(len(mes)):
            venda[i][j] = randint(0, 15)


# Função para imprimir os dados das vendas
def imprimir():
    print("Dados das vendas")
    for i in range(len(categoria)):
        for j in range(len(mes)):
            print(venda[i][j], end="\t")
        print()

# Função para somar o toltal de vendas por categoria 
def total_de_vendas_por_categoria():
    print("\n### Total por categoria ###")
    for i in range(len(categoria)):
        print(f'{categoria[i]} = {sum(venda[i])}')


# Função principal
def main():
    ler_dados()
    imprimir()
    total_de_vendas_por_categoria()

# Chamada da função função principal
if __name__ == '__main__':
    main()
