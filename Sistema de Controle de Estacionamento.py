class Proprietario:
    def __init__(self, nome, cpf):
        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
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
            raise ValueError("Placa inválida. O formato correto é Mercosul (ABC1D23), com letras maiúsculas.")
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

    def minutos(self):
        return self.hora * 60 + self.minuto


class Controle:
    def __init__(self):
        self.usuarios = []
        self.veiculos = []
        self.veiculos_estacionados = []
        self.veiculos_saida = []

    def cpf_existente(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return True
        return False

    def placa_existente(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                return True
        return False

    def cadastrar_veiculo(self, proprietario, veiculo):
        if self.placa_existente(veiculo.placa):
            print("Erro: Placa já cadastrada no sistema. Por favor, forneça uma nova placa.")
            return
        self.usuarios.append(proprietario)
        self.veiculos.append(veiculo)
        print("Veículo cadastrado com sucesso!")

    def entrada(self, placa, hora, minuto):
        veiculo = None
        for v in self.veiculos:
            if v.placa == placa:
                veiculo = v
                break

        if veiculo:
            self.veiculos_estacionados.append({"veiculo": veiculo, "entrada": Hora(hora, minuto)})
            print("Entrada registrada!")

    def registrar_saida(self, placa):
        veiculo_estacionado = None
        for v in self.veiculos_estacionados:
            if v["veiculo"].placa == placa:
                veiculo_estacionado = v
                break

        if veiculo_estacionado is None:
            print("Veículo não encontrado no estacionamento.")
            return

        hora = int(input("Hora de saída (hora): "))
        minuto = int(input("Minuto de saída (minutos): "))
        entrada = veiculo_estacionado["entrada"]
        saida = Hora(hora, minuto)
        tempo_minutos = saida.minutos() - entrada.minutos()
        valor = tempo_minutos * 0.20
        self.veiculos_saida.append({
            "veiculo": veiculo_estacionado["veiculo"],
            "entrada": entrada,
            "saida": saida,
            "valor": valor
        })

        # Remoção manual do item encontrado
        self.veiculos_estacionados = [v for v in self.veiculos_estacionados if v != veiculo_estacionado]
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
                
                while True:
                    cpf = input("CPF do proprietário (11 dígitos): ")
                    if len(cpf) != 11 or any(c not in "0123456789" for c in cpf):
                        print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")
                        continue
                    if controle.cpf_existente(cpf):
                        print("CPF já cadastrado no sistema. Forneça um CPF diferente.")
                        continue
                    break
                
                proprietario = Proprietario(nome, cpf)
                
                while True:
                    placa = input("Placa do veículo (ABC1D23 - letras maiúsculas): ")
                    try:
                        veiculo = Veiculo(placa, None, None, proprietario)
                        if controle.placa_existente(placa):
                            print("Placa já cadastrada no sistema. Forneça uma nova placa.")
                            continue
                        break
                    except ValueError as e:
                        print(f"Erro: {e}")

                marca = input("Marca do veículo: ")
                modelo = input("Modelo do veículo: ")
                veiculo.marca = marca
                veiculo.modelo = modelo
                
                controle.cadastrar_veiculo(proprietario, veiculo)
            except ValueError:
                continue
        
        elif opcao == "2":
            while True:
                placa = input("Placa do veículo (ABC1D23 - letras maiúsculas): ")
                if not controle.placa_existente(placa):
                    print("Placa não cadastrada no sistema. Registre o veículo antes de registrar a entrada.")
                    continue
                break
            
            hora = int(input("Hora de entrada (hora): "))
            minuto = int(input("Minuto de entrada (minutos): "))
            controle.entrada(placa, hora, minuto)
        
        elif opcao == "3":
            placa = input("Placa do veículo (ABC1D23 - letras maiúsculas): ")
            if not controle.placa_existente(placa):
                print("Placa não cadastrada no sistema. A consulta será encerrada.")
                continue

            controle.registrar_saida(placa)
        
        elif opcao == "4":
            controle.listagem()
        
        elif opcao == "5":
            print("Finalizando...")
            break
        
        else:
            print("Erro: Opção inválida. Por favor, escolha uma das opções disponíveis no menu.")

menu()
