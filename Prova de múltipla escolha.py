def nota(aluno, gabarito):
    acertos = 0
    for i in range(len(gabarito)):
        if aluno[i] == gabarito[i]:
            acertos += 1
    return acertos / len(gabarito) * 10


quantidade_questoes = int(input("Digite a quantidade de questões da prova: "))

gabarito = [input(f"Questão {i+1}: ") for i in range(quantidade_questoes)]

quantidade_alunos = int(input("Digite a quantidade de alunos: "))

relatorio = []

for _ in range(quantidade_alunos):

    nome = input("Nome: ")
    
    respostas = [input(f"Questão {i+1}: ") for i in range(quantidade_questoes)]
    
    nota_aluno = nota(respostas, gabarito)
    
    situacao = "Aprovado" if nota_aluno >= 7 else "Reprovado"
    
    relatorio.append(f"Aluno: {nome}, Nota: {nota_aluno:.1f}, Situação: {situacao}")

print("Relatório Final:")

for aluno in relatorio:
    print(aluno)
