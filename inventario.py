def carregar():
    produtos = {}
    try:
        with open("produtos.txt", "r") as file:
            for linha in file:
                nome = ""
                preco = ""
                quantidade = ""
                i = 0

                
                while i < len(linha) and linha[i] != ';':
                    nome += linha[i]
                    i += 1
                i += 1  

                while i < len(linha) and linha[i] != ';':
                    preco += linha[i]
                    i += 1
                i += 1 
                
                while i < len(linha) and linha[i] != '\n':
                    quantidade += linha[i]
                    i += 1

                produtos[nome] = (float(preco), int(quantidade))
    except FileNotFoundError:
        print("Arquivo produtos.txt não encontrado.")
    return produtos

def salvar(produtos):
    with open("produtos.txt", "w") as file:
        for nome in produtos:
            preco, quantidade = produtos[nome]
            file.write(f"{nome};{preco};{quantidade}\n")

def ordenar(produtos):
    produtos_lista = [(nome, produtos[nome][0], produtos[nome][1]) for nome in produtos]

    
    n = len(produtos_lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if produtos_lista[j][1] < produtos_lista[j + 1][1]:
                produtos_lista[j], produtos_lista[j + 1] = produtos_lista[j + 1], produtos_lista[j]
            elif produtos_lista[j][1] == produtos_lista[j + 1][1]:
                if produtos_lista[j][0] > produtos_lista[j + 1][0]:
                    produtos_lista[j], produtos_lista[j + 1] = produtos_lista[j + 1], produtos_lista[j]

    return produtos_lista

def buscar(nome, produtos):
    if nome in produtos:
        preco, quantidade = produtos[nome]
        print(f"Produto encontrado: Preço = {preco}, Quantidade em estoque = {quantidade}")
    else:
        print("Produto não encontrado.")

def exibir(produtos):
    produtos_ordenados = ordenar(produtos)
    print("Os 5 produtos mais caros são:")
    for nome, preco, quantidade in produtos_ordenados[:5]:
        print(f"Produto: {nome}, Preço: {preco}, Quantidade: {quantidade}")

def atualizar(nome, quantidade, produtos):
    if nome in produtos:
        preco, quantidade_atual = produtos[nome]
        produtos[nome] = (preco, quantidade_atual + quantidade)
        print(f"Estoque atualizado: {nome} agora tem {produtos[nome][1]} unidades.")
    else:
        print("Produto não encontrado.")

def cadastrar(produtos):
    nome = input("Insira o nome do produto: ")
    if nome in produtos:
        print("Produto já existe no inventário.")
        return

    try:
        preco = float(input("Insira o preço do produto: "))
        quantidade = int(input("Insira a quantidade do produto: "))
        produtos[nome] = (preco, quantidade)
        print(f"Produto '{nome}' cadastrado com sucesso.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um preço e uma quantidade válidos.")

def remover(produtos):
    nome = input("Insira o nome do produto a ser removido: ")
    if nome in produtos:
        del produtos[nome]
        print(f"Produto '{nome}' removido com sucesso.")
    else:
        print("Produto não encontrado.")

def menu():
    produtos = carregar()
    
    while True:
        print("\nMenu de opções:")
        print("1. Cadastrar um novo produto")
        print("2. Classificar produtos por preço")
        print("3. Buscar um produto pelo nome")
        print("4. Exibir os 5 produtos mais caros")
        print("5. Atualizar o estoque de um produto")
        print("6. Remover um produto")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar(produtos)
        
        elif opcao == '2':
            produtos_ordenados = ordenar(produtos)
            print("Produtos classificados por preço:")
            for nome, preco, quantidade in produtos_ordenados:
                print(f"Produto: {nome}, Preço: {preco}, Quantidade: {quantidade}")
        
        elif opcao == '3':
            nome = input("Insira o nome do produto: ")
            buscar(nome, produtos)
        
        elif opcao == '4':
            exibir(produtos)
        
        elif opcao == '5':
            nome = input("Insira o nome do produto: ")
            quantidade = int(input("Insira a quantidade comprada: "))
            atualizar(nome, quantidade, produtos)
        
        elif opcao == '6':
            remover(produtos)
        
        elif opcao == '7':
            salvar(produtos)
            print("Saindo e salvando os dados.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

menu()
