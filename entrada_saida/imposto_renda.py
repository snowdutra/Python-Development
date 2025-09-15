anual = float(input("Digite a renda anual do contribuinte em R$: "))
if anual < 0:
        print("A renda anual não pode ser negativa.")
else:
        if anual <= 10000:
            imposto = 0
        elif anual <= 25000:
            imposto = anual * 0.1035
        elif anual <= 50000:
            imposto = anual * 0.2542
        else:
            imposto = anual * 0.2975

        print("O imposto de renda devido é: R$ {:.2f}".format(imposto))
