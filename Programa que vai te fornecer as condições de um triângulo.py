while True:
    l1 = float(input("Digite o valor do primeiro lado do triângulo: "))
   #Condição de parada 
    if l1 == 0:
        break
    l2 = float(input("Digite o valor do segundo lado do triângulo: "))
    if l2 == 0:
        break
    l3 = float(input("Digite o valor do terceiro lado do triângulo: "))
    if l3 == 0:
        break
        #Condição para ser um triângulo
    if l1 < l2  + l3 and l2  < l1 + l3 and l3 < l1 + l2 :
        if l1 == l2  == l3:
            #Condição para ser equilátero 
            print("O triângulo é do tipo equilátero.")
        elif l1 == l2  or l1 == l3 or l2  == l3:
            #Condição para ser isósceles
            print("O triângulo é do tipo isósceles.")
        else:
            #Condição para ser escaleno
            print("O triângulo é do tipo escaleno.")
    else:
        print("Os valores não formam um triângulo.")

    print()
