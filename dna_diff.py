def contagem(saudavel, contaminado):
    insercao = []
    i, j = 0 ,0 

    while j < len(contaminado):
        if i < len(saudavel) and saudavel[i] == contaminado[j]:
            i += 1 
        else:
            insercao.append(contaminado[j])
        j += 1
    return len(insercao), insercao

saudavel = input("Digite o DNA saudavel: ")
contaminado = input("Digite o DNA contaminado: ")

numero, nucleotideos = contagem(saudavel, contaminado)
print(f"O numero nucleotídeos é: {numero}")
print(f"Os nucleotídeos que foram inseridos no DNA saudável é:", nucleotideos)
