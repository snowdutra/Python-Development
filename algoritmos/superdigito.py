def digito(y):

    while y >= 10:  

        soma_digitos = 0
        for digito in str(y):  
            soma_digitos += int(digito)  
        y = soma_digitos  

    return y


y = int(input("Digite um número inteiro:     "))

superdigito = digito(y)

print(f"O superdígito de {y} é {superdigito}")

