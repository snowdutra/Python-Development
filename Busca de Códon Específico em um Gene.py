def calcular(sequencia):
    comprimento = 0
    for _ in sequencia:
        comprimento += 1
    return comprimento


def converter(sequencia):
    resultado = ""
    for letra in sequencia:
        if letra == 'a':
            letra = 'A'
        elif letra == 'b':
            letra = 'B'
        elif letra == 'c':
            letra = 'C'
        elif letra == 'd':
            letra = 'D'
        elif letra == 'e':
            letra = 'E'
        elif letra == 'f':
            letra = 'F'
        elif letra == 'g':
            letra = 'G'
        elif letra == 'h':
            letra = 'H'
        elif letra == 'i':
            letra = 'I'
        elif letra == 'j':
            letra = 'J'
        elif letra == 'k':
            letra = 'K'
        elif letra == 'l':
            letra = 'L'
        elif letra == 'm':
            letra = 'M'
        elif letra == 'n':
            letra = 'N'
        elif letra == 'o':
            letra = 'O'
        elif letra == 'p':
            letra = 'P'
        elif letra == 'q':
            letra = 'Q'
        elif letra == 'r':
            letra = 'R'
        elif letra == 's':
            letra = 'S'
        elif letra == 't':
            letra = 'T'
        elif letra == 'u':
            letra = 'U'
        elif letra == 'v':
            letra = 'V'
        elif letra == 'w':
            letra = 'W'
        elif letra == 'x':
            letra = 'X'
        elif letra == 'y':
            letra = 'Y'
        elif letra == 'z':
            letra = 'Z'
        resultado += letra
    return resultado


def dividir(sequencia):
    codons = []
    comprimento = calcular(sequencia)
    i = 0
    while i < comprimento:
        codon = (sequencia[i], sequencia[i+1], sequencia[i+2])
        codons.append(codon)
        i += 3
    return codons

def buscar(codons, busca):
    for i in range(calcular(codons)):
        if codons[i] == busca:
            return i
    return -1

def main():
    sequencia = input("Digite a sequência de DNA (múltiplo de três nucleotídeos): ")
    busca = input("Digite o códon a ser buscado (três letras): ")


    sequencia = converter(sequencia)
    busca = (
        converter(busca[0]),
        converter(busca[1]),
        converter(busca[2])
    )

   
    codons = dividir(sequencia)
    print("Lista de códons:", codons)
    

    posicao = buscar(codons, busca)
    
    if posicao != -1:
        print(f"Códon {busca} encontrado na posição {posicao}.")
    else:
        print(f"Códon {busca} não encontrado na sequência de DNA.")


main()
