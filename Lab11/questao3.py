import random # inclui os comandos de aleatoriedade
import time # inclui os comandos de tempo

while True:
    des = input("deseja fazer uma pergunta? (S/N)  ")
    if des =="N":
        break
    if des =="S":
        pergunta = input("Qual é a pergunta:  ")
        prob = random.randint(1, 10) # gera número aleatório 1-10
    if prob <=5: 
        resposta ='SIM'
        time.sleep(2) # pausa a execução por 2 segundos
        print(f'{pergunta} = {resposta}.')
    else: 
        resposta ='NÃO'
        time.sleep(2) # pausa a execução por 2 segundos
        print(f' {pergunta} = {resposta}.')