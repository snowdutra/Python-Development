def digito(y):

    if y < 10:
        return y
    else:

        soma_digitos = sum(int(digito) for digito in str(y))
        return digito(soma_digitos)



y = int(input("Digite um número inteiro: "))

superdigito = digito(y)

print(f"O superdígito de {y} é {superdigito}")
