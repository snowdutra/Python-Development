while True:
    numero = int(input("Digite um número inteiro: "))
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")
    break
print("Aqui está a sua tabuada!")
