import random

for i in range(5):
    dado1 = random.randint(1,6) # escolhe um número aléatorio de 1 a 6. biblioteca
    dado2 = random.randint(1,6)# escolhe um número aléatorio de 1 a 6. biblioteca
    diferenca = abs(dado2-dado1)# colocar os número abosolutos. nativa
    if diferenca == 0:
        break