jogos = int(input("Número de jogos do Atlético MG:  "))
vitorias = 0
derrota = 0
empate = 0
pontuação = 0
for n in range(jogos):
    gols_galo = int(input("Números de gols do galo:  "))
    gols_f = int(input("Número de gols tomados:  "))
    if gols_galo > gols_f:
        vitorias += 1
        pontuação += 3
    if gols_galo < gols_f:
        derrota += 1
    if gols_galo == gols_f:
        empate += 1
        pontuação += 1
        
    print(f'vitorias: {vitorias}')
    print(f'derrota: {derrota}')
    print(f'empate: {empate}')
    print(f'pontuação: {pontuação}')