def tabuada(numero):

    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

while True:
    numero = int(input("Digite um número inteiro: "))
    tabuada(numero)
    break

print("Aqui está a sua tabuada!")
