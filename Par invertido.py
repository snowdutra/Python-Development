def encontrar_pares_inversos(palavras):
    pares_inversos = []
    
    for i in range(len(palavras)):
        for j in range(i + 1, len(palavras)):
            if palavras[i] == palavras[j][::-1]:  
                pares_inversos.append((palavras[i], palavras[j]))
    
    return pares_inversos


entrada = int(input("Quantas palavras: "))
pares_inversos =[]
for i in range(entrada):
    pares_inversos.append(input("Palavra: "))
print(encontrar_pares_inversos(pares_inversos))


