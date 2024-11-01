def preencher_vetor():
    vetor = []
    for i in range(5):
        vetor.append(int(input("digite um valor: ")))
    return vetor

def maior_vetor (vetor):
    return max(vetor)

def tabuada_vetor(valor):
    print(f"Tabuada de {valor}:")
    for i in range(1,11):
        print(f"{i} x {valor} = {i*valor}")

vetor = preencher_vetor()
maior = maior_vetor(vetor)
tabuada = (tabuada_vetor(maior))
print(f"O maior valor do vetor e {maior}") 
