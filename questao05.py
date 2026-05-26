print("Cardápio 1. Açaí 300ml - R$ 12 2. Mousse - R$ 6 3. Salada de frutas - R$ 10 4. Fechar a conta")
print("Cardápio de bebidas 5. café 200ml - R$ 4 6. Suco 300ml - R$ 5 ")
saldo = 0
num = 0
while num != 4: # loop infinito
    num = int(input(('Digite um número: ')))
    if num == 0:
        break
    if num == 1:
        saldo += 12
        print("Valor: ")
        print(saldo)
    if num == 2:
        saldo += 6
        print("Valor: ")
        print(saldo)
    if num == 3:
        saldo += 10
        print("Valor: ")
        print(saldo)
    if num == 5:
        saldo += 4
        print(saldo)
    if num == 6:
        saldo += 5
        print("saldo")
else:
    print("TOTAL: R$ ")
    print(saldo)