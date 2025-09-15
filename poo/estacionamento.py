# funções do programa
 
def registrar_entrada():
    nome.append (input ("Nome do cliente: "))
    placa.append (input("Placa do veículo: "))
    entrada.append (input(" Horario de entrada (hh:mm):  "))
    saida.append("")

def registrar_saida():
        temp = input("Placa do veículo: ")
        for i in range(0,len(placa)):
            if placa[i] == temp:
                saida[i] = input("Horario de saída (hh:mm): ")
                status = True 
                break
        if status == False:
            print("veículo não encontrado")

def imprimir_relatorio():
        for i in range(0,len(placa)):
            print(f"Nome: {nome[i]}, Placa: {placa[i]}, Horario de entrada: {entrada[i]},Horario de saida: {saida[i]}")

def imprimir_faturamento():
    total = 0 
    for i in range(0, len(saida)):
        if saida[i] != "":
            aux_entrada = entrada[i].split(":")
            aux_saida = saida[i].split(":")
            tarifa = (int(aux_saida[0])- int(aux_entrada[0])) * 60 + int(aux_saida[1]) - int(aux_entrada[1])
            total += tarifa * 0.30

# código principal
nome = []
placa = []
entrada = []
saida = []

while(True):
    print("Escolha uma operação:")
    print("1. Registrar entrada")
    print("2. Registrar saída")
    print("3. Imprimir relatório")
    print("4. Imprimir faturamento")
    print("5. finalizar")
    opção = int(input("Opção ==>"))
    
    if opção == 5:
        break
    
    #validar opçao de usuario
    
    if opção < 1 or opção > 5 :
        print(" Opção invalida ")
    elif opção == 1:
        registrar_entrada()
    elif opção == 2:
        registrar_saida()
    elif opção == 3:
        imprimir_relatorio()
    elif opção == 4:
        imprimir_faturamento()
        
    print("\n")
