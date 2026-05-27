
import random
secreto = random.randint(1, 10)
chances = 5
print(secreto)

while chances > 0:
    palpite = int(input("Adivinhe o número (1 a 10): "))
    # Complete aqui
    chances -= 1
    print("Seu número de chances é:")
    print(chances)
    
    if palpite > 10:
        chances += 1
        print("Número maior que 10. ")
        continue
    
    if palpite <= 0:
        chances += 1
        print("de (1 a 10)")
        continue
    
    if palpite == secreto:
        print("Você acertou!!!")
        break