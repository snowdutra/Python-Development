#Função para rotacionar um texto a partir de um valor 
# Inteiro --> Cifra de César 
def rotacionar(texto, deslocamento):
    resultado = []
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            novo_char = ((ord(char) - base + deslocamento) % 26 + base)
            resultado.append(chr(novo_char))
        else:
            resultado.append(char)
    return ''.join(resultado)

#Programa principal
texto = input("Informe uma palavra: ")
deslocamento = int(input("Deslocamento: "))
print(rotacionar(texto, deslocamento))
