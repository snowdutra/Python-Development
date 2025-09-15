#método bubble sort
#   - para pequenas quantidades de dados

def bolha(v):
    totalDeRepeticao = 0
    totalDeTroca = 0
    for j in range(len(v)):
        for i in range(len(v) - 1):
            totalDeRepeticao += 1
            if v[i] > v[i + 1]:
                totalDeTroca += 1
                aux = v[i]
                v[i] = v[i + 1]
                v[i + 1] = aux
    print('Bolha')
    print(f'Total de repetições: {totalDeRepeticao}')
    print(f'Total de trocas: {totalDeTroca}')

'''
método selection
   - busca do menor elemento armazenado, e a ideia é de 2 vetores [ordenado] e [desrodenado]
'''
def selecao(x):
    totalDeRepeticao = 0
    totalDeTroca = 0
    n = len(x)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            totalDeRepeticao += 1
            if x[j] < x[menor]:
                menor = j
                totalDeTroca += 1
                
        # Troca os elementos (essa linha precisa estar dentro do laço externo)
        x[i], x[menor] = x[menor], x[i]
    print('Seleção')
    print(f'Total de repetições: {totalDeRepeticao}')
    print(f'Total de trocas: {totalDeTroca}')

# método de insert
#   - tende a ser o melhor método

def insercao(x):
    totalDeRepeticao = 0
    totalDeTroca = 0
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
            totalDeRepeticao += 1
            # a troca ta no mesmo lugar
        
    x[i + 1] = valor
    
    print('Inserção')
    print(f'Total de repetições: {totalDeRepeticao}')
    print(f'Total de trocas: {totalDeTroca}')
    

lista = []
for i in range(1000, 0, -1):
    lista.append(i)

bolha(lista.copy())
insercao(lista.copy())
selecao(lista.copy())
