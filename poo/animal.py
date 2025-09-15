valor1 = input("Digite a primeira entrada: ")
valor2 = input("Digite a segunda entrada:  ")
valor3 = input("Digite a terceira entrada: ")

animal = ""
if valor1 == "vertebrado":
    if valor2 == "ave":
        if valor3 == "carnivoro":
            animal = "aguia"
        elif valor3 == "onivoro":
            animal = "pomba"

    elif valor2 == "mamifero":
        if valor3 == "onivoro":
            animal = "homem"

        elif valor3 == "herbivoro":
            animal = "vaca"

elif valor1 == "invertebrado":
    if valor2 == "inseto":
        if valor3 == "hematofago":
            animal = "pulga"

        elif valor3 == "herbivoro":
            animal = "lagarta"

    elif valor2 == "anelideo":
        if valor3 == "hematofago":
            animal = "sanguessuga"

        elif valor3 == "onivoro":
            animal = "minhoca"

if animal:
    print("O animal correspondente é:", animal)
else:
    print("Animal não reconhecido")

print()
