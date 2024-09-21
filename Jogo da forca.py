import random

#função para simular o jogo da forca
def jogar(lista):
    palavra = random.choice(lista).upper()
    letras_corretas=["_" for _ in range (len(palavra))]
    letras_incorretas=[]
    tentativas = 6
    
    while tentativas > 0 and '_' in letras_corretas:
        print('Palavra atual' ''.join(letras_corretas))
        letra=input("insira uma letra: ").upper()
        
        #verifica se aletra já foi informada
        if letra in letras_incorretas or letra in letras_incorretas:
            print("letra já foi informada")
            continue
       
        #verifica se a letra faz parte da palavra secreta
        if letra in palavra:
            for i in range (len(palavra)):
                if letra == palavra [i]:
                    letras_corretas[i] = letra 
            print(letras_corretas)
        else:
            letras_incorretas.append(letra)
            tentativas -= 1
            print(f"--- > Você errou pela {len(letras_incorretas)} a vez. Tente novamente")
        

        if '_' not in letras_corretas:
            print("Parabéns você acertou a palavra secreta!")
         
            

#lista de palavras
lista=["caps","aula","atividade","tiroteio","carlos"]

jogar(lista)
