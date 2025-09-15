
#Função para calcular a frequência de cada letra 
def calcularFrequencia(texto):
    frequencia = {}
    for letra in texto:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1
        
    print(frequencia)

        #Função para calcular a frequência de cada letra em um texto

def calcularFrequencia(texto):
    texto = texto.lower()
    frequencia = {}
    for letra in texto:
        if letra.isalpha():
            if letra in frequencia:
                frequencia[letra] += 1
            else:
                frequencia[letra] = 1
            
    print(frequencia)



#Programa Principal
texto = input("Informe um texto:    ")
calcularFrequencia(texto)
