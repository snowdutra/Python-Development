#Função para gravar os dados e armazenar nas listas -->> Memória

def registrar_aluno():
nome.append (input ("Nome do aluno: "))
nota_1.append (input("Primeira nota: "))
nota_2.append (input("Segunda nota: "))

#Função para gravar os dados em um arquivo tipo texto

def gravar():
with open("aluno.txt", "w") as arquivo:
for i in range(0, len(nome)):
dados = nome[i] + ";" + str(nota_1[i]) + ";" + str(nota_2[i])
arquivo.write(dados + "\n")

#Função para gravar os dados em um ralatório

def pesquisar_aluno():
for i in range(0,len(nota_1)):
print(f"Nome: {nome[i]}, Primeira nota : {nota_1[i]}, Segunda Nota: {nota_2[i]},")

## código principal

nome = []
nota_1 = []
nota_2 = []

while(True):

print("Escolha uma operação:")
print("1. Registrar aluno")
print("2. Liste o aluno")
print("3. Pesquisar aluno")
print("4. finalizar")
opção = int(input("Opção ==>> "))

if opção == 4:
    gravar()
    break

if opção == 1:
    registrar_aluno();

print()
