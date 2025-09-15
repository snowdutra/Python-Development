coleta = ["1º Ponto", "2º Ponto", "3º Ponto", "4º Ponto", "5º Ponto"]


temperaturas = {ponto: [] for ponto in coleta}


for ponto in coleta:
    print(f"\nDigite as temperaturas mensais máximas para {ponto}:  ")

    for mes in range(1, 13):  
        temp = float(input(f"Temperatura máxima de {ponto} no mês {mes}:    "))
        
        temperaturas[ponto].append(temp)


def media(lista):

    soma = 0
    for item in lista:
        soma += item

    return soma / len(lista)


print("\nMédia das temperaturas de cada ponto:  ")

medias = {}

for ponto, temp in temperaturas.items():

    medias[ponto] = media(temp)

    print(f"{ponto}: {medias[ponto]:.2f} °C")


print("\nMédia semestral das temperaturas:")

for ponto, temp in temperaturas.items():
    
    primeiro_semestre = media(temp[:6])  
    segundo_semestre = media(temp[6:])  
    
    print(f"{ponto} - 1º Semestre: {primeiro_semestre:.2f} °C, 2º Semestre: {segundo_semestre:.2f} °C")


primeiro_ponto = True

for ponto, media_temperatura  in medias.items():
   
    if primeiro_ponto:
        maior_media = media_temperatura 
        ponto_maior = ponto
        primeiro_ponto = False
   
    elif media_temperatura  > maior_media:
        maior_media = media_temperatura 
        ponto_maior = ponto

print(f"\nPonto de coleta de maior média: {ponto_maior} ({maior_media:.2f} °C)")


primeiro_ponto = True

for ponto, media_temperatura in medias.items():
    
    if primeiro_ponto:
        menor_media = media_temperatura 
        ponto_menor = ponto
        primeiro_ponto = False
    
    elif media_temperatura  < menor_media:
        menor_media = media_temperatura 
        ponto_menor = ponto

print(f"Ponto de coleta de menor média: {ponto_menor} ({menor_media:.2f} °C)")
