def triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Triângulo equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "Não é um triângulo"


def resultado():
    a = float(input("Digite o primeiro lado do triângulo:   "))
    b = float(input("Digite o segundo lado do triângulo:    "))
    c = float(input("Digite o terceiro lado do triângulo:   "))

    resultado = triangulo(a, b, c)
    print(resultado)

resultado()  
