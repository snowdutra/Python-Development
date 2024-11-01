def tempo(horaio):
    horas = int(horaio[:2])
    minutos = int(horaio[3:])
    return horas * 60 + minutos

def estadia(dados):
    entrada = tempo(dados["entrada"])
    saida = tempo(dados["saida"])
    permanencia = saida - entrada
    valor =  permanencia * 0.75
    return valor

veiculos = [{"nome": "João", "entrada": "08:15", "saida": "10:45"},
            {"nome": "Maria", "entrada": "09:30", "saida": "11:00"},
            {"nome": "Carlos", "entrada": "07:00", "saida": "12:15"}]

for veiculo in veiculos:
    valor_estadia = estadia(veiculo)
    print(f"O valor da estadia de {veiculo['nome']} foi de R${valor_estadia:.2f}")
