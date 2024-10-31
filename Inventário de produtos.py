def carregar():
    produtos = []
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

                produtos.append((nome, float(preco), int(quantidade)))
    except FileNotFoundError:
        print("Arquivo produtos.txt não encontrado.")
    return produtos

def salvar(produtos):
    with open("produtos.txt", "w") as file:
        for produto in produtos:
            file.write(f"{produto[0]};{produto[1]};{produto[2]}\n")

def ordenar(produtos):
    for i in range(len(produtos) - 1):
        for j in range(i + 1, len(produtos)):
            if produtos[i][1] < produtos[j][1]:
                produtos[i], produtos[j] = produtos[j], produtos[i]
            elif produtos[i][1] == produtos[j][1]:
                if produtos[i][0] > produtos[j][0]:
                    produtos[i], produtos[j] = produtos[j], produtos[i]
    return produtos

def buscar(nome, produtos):
    for produto in produtos:
        if produto[0] == nome:
            print(f"Produto encontrado: Preço = {produto[1]}, Quantidade em estoque = {produto[2]}")
            return
    print("Produto não encontrado.")

def exibir(produtos):
    produtos_ordenados = ordenar(produtos)
    print("Os 5 produtos mais caros são:")
    for produto in produtos_ordenados[:5]:
        print(f"Produto: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}")

def atualizar(nome, quantidade, produtos):
    for i in range(len(produtos)):
        if produtos[i][0] == nome:
            produto_atualizado = (produtos[i][0], produtos[i][1], produtos[i][2] + quantidade)
            produtos[i] = produto_atualizado
            print(f"Estoque atualizado: {produto_atualizado[0]} agora tem {produto_atualizado[2]} unidades.")
            return
    print("Produto não encontrado.")

def cadatrar(produtos):
    nome = input("Insira o nome do produto: ")
    for produto in produtos:
        if produto[0] == nome:
            print("Produto já existe no inventário.")
            return

    try:
        preco = float(input("Insira o preço do produto: "))
        quantidade = int(input("Insira a quantidade do produto: "))
        novo_produto = (nome, preco, quantidade)
        produtos.append(novo_produto)
        print(f"Produto '{nome}' cadastrado com sucesso.")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um preço e uma quantidade válidos.")

def remover(produtos):
    nome = input("Insira o nome do produto a ser removido: ")
    for i in range(len(produtos)):
        if produtos[i][0] == nome:
            produtos.pop(i)
            print(f"Produto '{nome}' removido com sucesso.")
            return
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
            cadatrar(produtos)
        
        elif opcao == '2':
            produtos = ordenar(produtos)
            print("Produtos classificados por preço:")
            for produto in produtos:
                print(f"Produto: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}")
        
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
