numero = int(input("Digite um número inteiro e positivo: "))

if numero > 0:
    print("Divisores Positivos e negativos:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i, -i)
else:
    print("O número deve ser positivo.")
