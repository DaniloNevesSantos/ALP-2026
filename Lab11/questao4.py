jog1 = 0
jog2 = 0
roud = 0
import random
while jog1 <= 50 or jog2 <= 50:
    
    dado1 = int(random.randint(1, 6))
    dado2 = int(random.randint(1, 6))
    print(dado1, dado2)
    palpite1 = int(input(f'Jogador 1. {jog1} pontos: Qual o seu palpite para a soma dos dados?'  ))
    palpite2 = int(input(f'Jogador 2. {jog2} pontos: Qual o seu palpite para a soma dos dados?'  ))
    certo = dado1+dado2
    perto1 = abs(palpite1 - certo)
    perto2 = abs(palpite2 - certo)
    if perto1 > perto2:
        jog2 += 5
        print("Jogador 2 ganhou..")
    if perto2 > perto1:
        jog1 += 5
        print("Jogador 1 ganhou..")
    if perto1 == perto2:
        jog1 += 2
        jog2 += 2
        print("Empate..")
    
