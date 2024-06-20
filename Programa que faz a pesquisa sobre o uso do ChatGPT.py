entrada1 = 0
entrada2 = 0
entrada3 = 0

pessoas = int(input("Quantas pessoas vão participar dessa pesquisa?    "))

for _ in range(pessoas):
    resposta = input("Você apoia o uso no ChatGPT em escolas e universidades?:   ")
    
    if resposta == "sim":
        entrada1 += 1
    elif resposta == "nao sou contra":
        entrada2 += 1
    elif resposta == "nao":
        entrada3 += 1
    else:
        print("Por favor, insira 'sim', 'nao sou contra' ou 'nao'.")

total = entrada1 + entrada2 + entrada3

if total > 0:
    positivas = (entrada1 / total) * 100
    neutras = (entrada2 / total) * 100
    negativas = (entrada3 / total) * 100
    

    print(f"Participaram dessa pesquisa: {pessoas} pessoa(s)")
    
    print("Opiniões Positivas: {:.2f}%".format(positivas))
    
    print("Opiniões Neutras: {:.2f}%".format(neutras))
    
    print("Opiniões Negativas: {:.2f}%".format(negativas))

else:

    print("Ninguem participou dessa pesquisa.")
