# Método para ordenar a lista pela nota
def ordenar_por_nota(aluno):
    n = len(aluno)
    for j in range(n):
        for i in range (n - 1):
            if aluno[i]['nota'] > aluno[i + 1]['nota']:
                aluno[i], aluno[i + 1] = aluno[i + 1], aluno[i]
    return aluno

aluno = [
    {'nome': 'João', 'nota': 7.5},
    {'nome': 'Maria', 'nota': 9.2},
    {'nome': 'Pedro', 'nota': 8.8},
    {'nome': 'Ana', 'nota': 6.9},
    {'nome': 'Lucas', 'nota': 7.3}
]

print(ordenar_por_nota(aluno))
