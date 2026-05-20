import random # essa deve ser a primeira linha do código
chance = 5
numero=(random.randint(1, 10))
while chance > 0:
    n=int(input(f"Qual número? Você tem {chance} chances"))
    chance -= 1
    if n == numero:
        print("Você acertou o número")