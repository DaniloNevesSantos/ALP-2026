from funcoes import soma

vet = [14, 2, 63, 27, 3, 49, 52, 10, 77, 1]

maior = int(input("Qual será o maior numero: "))
menor = int(input("qual será o menor número: "))

somado = soma(vet, menor, maior)
print(somado)