def fatorial(valor):
    # Caso base da recursão --> quando devo parar?
    if valor == 0: return 1
    # Caso recursivo --> quando devo chamar a função novamente?
    return valor * fatorial(valor - 1)

valor = int(input("Valor inteiro e positivo:    "))
fat = fatorial(valor)
print(fat)
