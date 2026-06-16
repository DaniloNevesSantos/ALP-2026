
while True:
    resposta=input("Você quer saber como manter uma pessoa ingênua ocupada por horas? S/N     ")
    if resposta == "S" or resposta == "s" or resposta == "SIM" or resposta == "sim":
        continue
    elif resposta == "N" or resposta == "n" or resposta == "NÃO" or resposta == "não":
        print("Obrigada. Tenha um bom dia!")
        break
    else:
        print(f''{resposta}'   não é uma resposta válida de sim/não. ')
    
