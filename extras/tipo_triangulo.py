l1 = float(input("Digite o comprimento do primeiro lado: "))
l2 = float(input("Digite o comprimento do segundo lado: "))
l3 = float(input("Digite o comprimento do terceiro lado: "))

if l1 <= 0 or l2 <= 0 or l3 <= 0:
        print("Os lados do triângulo devem ser números positivos maiores que zero.")
elif l1 == l2 == l3:
        print("O triângulo é classificado como: Equilátero")
elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O triângulo é classificado como: Isósceles")
else:
        print("Os valores não formam um triângulo")
