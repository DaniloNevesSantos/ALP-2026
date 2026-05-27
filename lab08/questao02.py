cont = 5
while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0: 
        continue
    print(f'{num} é um número ímpar')
#quando um número par é digitado o código pula ele sem sair do loop.
#qundo ele e ímpar o código faz um print falando que ele e um ímpar.