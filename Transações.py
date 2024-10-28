def bubble_sort(transacoes):
    n = len(transacoes)
    for i in range(n):
        for j in range(0, n-i-1):
            if transacoes[j]['saldo'] > transacoes[j+1]['saldo']:
                transacoes[j], transacoes[j+1] = transacoes[j+1], transacoes[j]

def nome_e_saldo(transacao_bancarias):
    bubble_sort(transacao_bancarias)
    for i in range(len(transacao_bancarias)):
        print(transacao_bancarias[i]['nome'], transacao_bancarias[i]['saldo'])

trasacoes_bancarias = [
    { 'nome': 'João', 'saldo': 1000},
    { 'nome': 'Maria', 'saldo': 1500},
    { 'nome': 'Pedro', 'saldo': 2000}
]

nome_e_saldo(trasacoes_bancarias)
