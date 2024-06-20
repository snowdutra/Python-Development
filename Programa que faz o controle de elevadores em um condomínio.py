usuario = int(input("Insira o número de usuários: "))

entrada = {'a': {'m': 0, 'v': 0, 'n': 0}, 'b': {'m': 0, 'v': 0, 'n': 0}, 'c': {'m': 0, 'v': 0, 'n': 0}}
               

for i in range(usuario):
    elevador = input(f"Qual elevador o usúario {i + 1} entrou (a, b ou c):              ")
    
    periodo = input(f"Qual periodo o usúario {i + 1} utilizou o elevador (m , v ou n):    ")

    entrada[elevador][periodo] += 1


e = ''
p = ''
contagem = 0


for elevador in entrada:
    for periodo in entrada[elevador]:
        if entrada[elevador][periodo] > contagem:
            e = elevador
            p = periodo
            contagem = entrada[elevador][periodo]


total = 0
for elevador in entrada:
    for periodo in entrada[elevador]:
        total += entrada[elevador][periodo]


mais = (contagem / total) * 100
menos = 100 - mais



print(f"O elevador mais usado é o:          {e} ")


print(f"O período com maior fluxo é o:      {p}")


print(f"A diferença percentual entre o mais usado e o menos usado é:    {menos}%")
