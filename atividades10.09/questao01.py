from funcoes import verificar
vet = [14, 2, 63, 27, 3, 49, 52, 10, 77, 1]

numero = int(input("Número a ser procurado: "))

verificado = verificar(vet, numero)
print(verificado)