def validarEmail(email):
    if "@" in email [1:-1]:
        return True
    else:
        return False



email = input("Digite um email: ")

if validarEmail(email):
    print("Email Valido")
else:
    print("Email Invalido")
    

    
