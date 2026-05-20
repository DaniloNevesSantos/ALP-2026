N = int(input("Quantos números quer digitar?  "))   
N1 = int(input("Pode repetir Quantos números quer digitar.  ")) #criei uma nova variavel para não confundir com N.
contador = 0
impares = 0

while contador <= N1: #coloquei N1 para diminuir.
    N1 -= 1
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1

print(f"Quantidade de ímpares entre 1 e {N}: {impares}") #é o N ser para guardar o total pois o N seria -1 pois ele seria diminuido