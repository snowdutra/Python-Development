
# função para carregar os dados do arquivo para a memória do computador
def ler_dados():
    try:
        with open("aluno.txt", "r") as arquivo:
            linha = arquivo.read()
            linha = linha.replace("\n", ";")
            dados = linha.split(";")
            nome.append(dados[0])
            nota1.append(float(dados[1]))
            nota2.append(float(dados[2]))
    
    except FileNotFoundError:
        print("Arquivo não encontrado")
            
    
# função para ler os dados e armazenar nas listas --> na memória
def cadastrar():
    nome.append(input("Nome: "))
    nota1.append(float(input("Nota 1: ")))
    nota2.append(float(input("Nota 2: ")))

# função para gravar os dados em um arquivo do tipo texto
def gravar():
    with open("aluno.txt", "w") as arquivo:
        for i in range(0, len(nome)):
            dados = nome[i] + ";" + str(nota1[i]) + ";" + str(nota2[i])
            arquivo.write(dados + "\n")

# função para listar todos os alunos
def listar():
   for i in range(0, len(nome)):
       media = (nota1[i] + nota2[i]) / 2
       situacao = "APROVADO" if media >= 7 else "REPROVADO" 
       print(f"Nome: {nome[i]}")
       print(f"Média: {media}")
       print(f"Situação: {situacao}")
       print()

# função para pesquisar um aluno pelo nome
def pesquisar():
    temp = input("Nome a ser pesquisado: ")
    for i in range(0, len(nome)):
        if temp == nome[i]:
            print(f"{temp} encontrado")
            return
    print(f"{temp} não encontrado")
    
# código principal
nome = []
nota1 = []
nota2 = []

# função para ler os dados do arquivo aluno.txt e armazenar nas listas na memória

ler_dados()

while True:
    print("Escolha uma operação:")
    print("1. Cadastrar aluno")
    print("2. Listar aluno")
    print("3. Pesquisar aluno")
    print("4. Finalizar")
    opcao = int(input("Opção ====>>>>  "))
    
    if opcao == 4:
        gravar()
        break
    
    if opcao == 1: 
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        pesquisar()
        
    print()
