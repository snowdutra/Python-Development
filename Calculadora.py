# Funçoes sempre no início do código
def somar():
    #Corpo da função
    resultado = x + y 
    return resultado
    
    #Corpo da função
def subtrair():
    resultado = x - y
    return resultado

    #Corpo da função
def multiplicar():
    resultado = x * y
    return resultado
 
#Corpo da função
def dividir():
    resultado = x / y
    return resultado
    
#Código principal 
x = int(input("Informe o valor de x:    "))
y = int(input("Informe o valor de y:    "))

#Função Somar
resultado = somar()
print (f"Resultado Soma = {resultado}")
#Função subtrair
resultado = subtrair()
print (f"Resultado Subtração = {resultado}")
#Função multiplicar
resultado = multiplicar()
print (f"Resultado Multiplicação = {resultado}")
#Função dividir
resultado = dividir()
print (f"Resultado Divisão = {resultado}")
