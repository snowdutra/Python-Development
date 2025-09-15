def soma(numero):

    if numero < 10:
        return numero
   
    return numero % 10 + soma(numero // 10)

numero = int(input("Informe um número inteiro: "))

resultado = soma(numero)

print(f'A soma dos dígitos de {numero} é {resultado}')
