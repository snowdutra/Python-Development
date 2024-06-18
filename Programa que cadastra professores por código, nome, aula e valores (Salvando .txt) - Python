
## Cadastrar Professores

def cadastrar_professor():

    while True:

        codigo_professor = input("Insira o código do professor: ")
        codigo = False
        
        for professor in professores:
            if professor['código'] == codigo_professor:
                codigo = True

                break

        if codigo:

            print("Código já cadastrado. Insira um código único.")
        else:

            break
    
    nome = input("Insira o nome do professor:                  ")
    total_aulas = int(input("Insira o total de aulas semanais: "))
    valor_aula = float(input("Insira o valor da aula:          "))  
    
    salario = total_aulas * 4.5 * valor_aula

    adicional = salario * 0.05

    descanso = (salario + adicional) / 6
    
    salario_mes = salario + adicional + descanso

    professor = {'código': codigo_professor,'nome': nome,'total_aulas': total_aulas,'valor_aula': valor_aula,'salario_mes': salario_mes}
    professores.append(professor)
    print("Professor cadastrado com sucesso!")
    
## Encerrar Programa (Salvando)

def gravar():

    with open('professor.txt', 'r') as arquivo:

        for linha in arquivo:

            codigo_professor, nome, total_aulas, valor_aula = linha.split(';')  
            professor = {'código': codigo_professor,'nome': nome, 'total_aulas': int(total_aulas),'valor_aula': float(valor_aula)}
            
            professores.append(professor)

def finalizar():

    with open('professor.txt', 'w') as arquivo:

        for professor in professores:
            
            arquivo.write(f"{professor['código']};{professor['nome']};{professor['total_aulas']};{professor['valor_aula']:.2f}\n")

## Pesquisar Professor 
def pesquisar_professor():

    codigo_professor = input("Insira o código do professor:       ")

    for professor in professores:

        if professor['código'] == codigo_professor:

            print(f"Nome: {professor['nome']}")
            print(f"Salário Mensal: R$ {professor['salario_mes']:.2f}")
            return
        
    print("Professor não encontrado.")

## Remover Professor 

def remover_professor():

    codigo_professor = input("Informe o código do professor: ")

    for i in range(len(professores)):

        if professores[i]['código'] == codigo_professor:

            professores.pop(i)
            print("Professor removido.")

            return
        
    print("Professor não encontrado.")

## Listar Professor

def listar_professores():

    for professor in professores:
        
        print(f"Código: {professor['código']}, Nome: {professor['nome']}, Salário Mensal: R$ {professor['salario_mes']:.2f}")

## Código Principal

professores = []

nome = []

total_aulas = []

valor_aula = []

while True:

    print("Escolha uma opção:     ")
    print("1. Cadastrar professor")
    print("2. Pesquisar professor")
    print("3. Remover professor")
    print("4. Listar professores")
    print("5. Finalizar")

    opcao = input("Opção:        ")

    if opcao == '1':
        cadastrar_professor()
    elif opcao == '2':
        pesquisar_professor()
    elif opcao == '3':
        remover_professor()
    elif opcao == '4':
        listar_professores()
    elif opcao == '5':
        finalizar()
        break

    else:

        print("Digite outra opção. Opção inválida.")
