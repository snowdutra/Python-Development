class Proprietario:
    def __init__(self, nome, cpf):
        if not self.validar_cpf(cpf):
            print("CPF inválido. Digite o CPF com 11 dígitos numéricos.")
            raise ValueError("CPF inválido")
        self.nome = nome
        self.cpf = cpf

    def validar_cpf(self, cpf):
        if len(cpf) != 11:
            return False
        for c in cpf:
            if c not in "0123456789":
                return False
        return True


class Veiculo:
    def __init__(self, placa, marca, modelo, proprietario):
        if not self.validar_placa(placa):
            print("Placa inválida. Digite no formato Mercosul (ABC1D23) com letras maiúsculas.")
            raise ValueError("Placa inválida")
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.proprietario = proprietario

    def validar_placa(self, placa):
        if len(placa) != 7:
            return False
        letras = placa[:3]
        numeros = placa[3:]
        for c in letras:
            if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                return False
        if numeros[0] not in "0123456789":
            return False
        if numeros[1] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            return False
        for c in numeros[2:]:
            if c not in "0123456789":
                return False
        return True


class Hora:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"

    def calcular_minutos(self):
        return self.hora * 60 + self.minuto


class Controle:
    def __init__(self):
        self.usuarios = []
        self.veiculos = []
        self.veiculos_estacionados = []
        self.veiculos_saida = []

    def cpf_existe(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return True
        return False

    def placa_existe(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                return True
        return False

    def cadastrar_veiculo(self, proprietario, veiculo):
        if self.placa_existe(veiculo.placa):
            print("Placa já cadastrada, digite uma nova placa.")
            return
        self.usuarios.append(proprietario)
        self.veiculos.append(veiculo)
        print("Veículo cadastrado com sucesso!")

    def registrar_entrada(self, placa, hora, minuto):
        if not self.placa_existe(placa):
            print("Placa não cadastrada, registre o veículo.")
            return 

        veiculo = None
        for v in self.veiculos:
            if v.placa == placa:
                veiculo = v
                break

        self.veiculos_estacionados.append({"veiculo": veiculo, "entrada": Hora(hora, minuto)})
        print("Entrada registrada!")

    def registrar_saida(self, placa, hora, minuto):
        veiculo_estacionado = None
        for v in self.veiculos_estacionados:
            if v["veiculo"].placa == placa:
                veiculo_estacionado = v
                break
        
        if veiculo_estacionado is None:
            print("Veículo não encontrado no estacionamento!")
            return

        entrada = veiculo_estacionado["entrada"]
        saida = Hora(hora, minuto)
        tempo_minutos = saida.calcular_minutos() - entrada.calcular_minutos()
        valor = tempo_minutos * 0.20
        self.veiculos_saida.append({
            "veiculo": veiculo_estacionado["veiculo"],
            "entrada": entrada,
            "saida": saida,
            "valor": valor
        })
        self.veiculos_estacionados.remove(veiculo_estacionado)
        print(f"Saída registrada com sucesso! Valor a pagar: R$ {valor:.2f}")

    def listagem(self):
        print("\nVeículos Estacionados:")
        for veiculo in self.veiculos_estacionados:
            print(f"Proprietário: {veiculo['veiculo'].proprietario.nome}, Placa: {veiculo['veiculo'].placa}, Entrada: {veiculo['entrada']}")

        print("\nVeículos que Saíram:")
        for veiculo in self.veiculos_saida:
            print(f"Proprietário: {veiculo['veiculo'].proprietario.nome}, Placa: {veiculo['veiculo'].placa}, Entrada: {veiculo['entrada']}, Saída: {veiculo['saida']}, Valor: R$ {veiculo['valor']:.2f}")


def menu():
    controle = Controle()
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar veículo")
        print("2. Registrar entrada")
        print("3. Registrar saída")
        print("4. Listagem")
        print("5. Finalizar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                nome = input("Nome do proprietário: ")
                cpf = input("CPF do proprietário (11 dígitos): ")
                
                if controle.cpf_existe(cpf):
                    print("CPF já cadastrado! O cadastro será interrompido.")
                    continue  
                
                proprietario = Proprietario(nome, cpf)
                
                placa = input("Placa do veículo (ABC1D23 - letras maiúsculas): ")
                if controle.placa_existe(placa):
                    print("Placa já cadastrada, digite a placa novamente.")
                    continue 
                
                veiculo = Veiculo(placa, None, None, proprietario)
                
                marca = input("Marca do veículo: ")
                modelo = input("Modelo do veículo: ")
                veiculo.marca = marca
                veiculo.modelo = modelo
                
                controle.cadastrar_veiculo(proprietario, veiculo)
            except ValueError:
                continue
        
        elif opcao == "2":
            placa = input("Placa do veículo (ABC1D23 - letras maiúsculas): ")
            
            if not controle.placa_existe(placa):
                print("Placa não cadastrada, realize o cadastro do veículo.")
                continue  
            
            hora = int(input("Hora de entrada (hh): "))
            minuto = int(input("Minuto de entrada (mm): "))
            controle.registrar_entrada(placa, hora, minuto)
        
        elif opcao == "3":
            placa = input("Placa do veículo (ABC1D23 - letras maiúsculas): ")
            if not controle.placa_existe(placa):
                print("Placa não cadastrada, realize o cadastro do veículo.")
                continue

            hora = int(input("Hora de saída (hh): "))
            minuto = int(input("Minuto de saída (mm): "))
            controle.registrar_saida(placa, hora, minuto)
        
        elif opcao == "4":
            controle.listagem()
        
        elif opcao == "5":
            print("Finalizando...")
            break
        
        else:
            print("Opção inválida!")

menu()
