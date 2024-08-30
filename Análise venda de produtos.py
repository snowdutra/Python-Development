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

# Função para identificar o mês com o maior total de vendas
def melhor_mes():
    total = 0 
    maior = 0
    mes_maior_venda = ""
    for j in range(len(mes)):
        total = 0
        for i in  range (len(categoria)):
            total = total + venda[i][j]
        if(total > maior):
            maior = total
            mes_maior_venda = mes[j]
    print (f"### mês com maior toltal de vendas -->  {mes_maior_venda}")

# Função para calcular a média de vendas mensais por categoria 
def media_por_categoria():
        print()
        for i in range(len(categoria)):
            print(f"{categoria[i]}) = {sum(venda[i])/len(venda[i])}")

# Função principal
def main():
    ler_dados()
    imprimir()
    total_de_vendas_por_categoria()
    melhor_mes()
    media_por_categoria()
    
# Chamada da função função principal
if __name__ == '__main__':
    main()
