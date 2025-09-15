entrada = input("Digite os elementos do vetor: ")

vetor = []  
for elemento in entrada.split():  
    vetor.append(int(elemento))

sem_duplicatas = []
for elemento in vetor:
    if elemento not in sem_duplicatas:
        sem_duplicatas.append(elemento)

print("Vetor sem duplicatas:", sem_duplicatas)
