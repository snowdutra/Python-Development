equilatero = 0
escaleno =   0
isosceles =  0

triangulos = int(input("Digite o número de triângulos:   "))

for _ in range(triangulos):
    a = float(input("Digite o primeiro lado:    "))
    b = float(input("Digite o segundo lado:     "))
    c = float(input("Digite o terceiro lado:    "))

    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            equilatero += 1
        elif a != b != c != a:
            escaleno += 1
        else:
            isosceles += 1
    else:
        print("Os números não formam um triângulo lados não formam um triângulo")


print(f"Equiláteros:    {equilatero}")
print(f"Escalenos:      {escaleno}")
print(f"Isósceles:      {isosceles}")
