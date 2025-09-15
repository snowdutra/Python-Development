def hexadecimal(n):
    if n == 0:
        return ""
    
    return hexadecimal(n // 16) + hex(n % 16)[-1]

def conversor():

    while True:
        try:
            valor = int(input("Digite um valor inteiro e positivo: "))
            if valor >= 0:
                break
            else:
                print("Digite um valor positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    if valor == 0:
        return "0"  
    return hexadecimal(valor)

resultado = conversor()
print(f"Conversão para hexadecimal: {resultado}")
