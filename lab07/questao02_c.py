#Imprimir o maior número digitado pelo usuário
maior = float('-inf')
soma = int(input("Quantos números quer digitar?  "))
soma1 = 0
contador = 0
while contador <= soma: #não existe variavel soma #o while nunca vai acabar.
    soma1 = int(input("Digite um número: "))
    contador += 1 
    if soma1 > maior:
       maior = soma1
print('O maior número é', maior)