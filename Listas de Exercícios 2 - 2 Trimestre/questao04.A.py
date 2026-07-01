import random
import time

inicio = time.time()  #marca o tempo apos ser lida. biblioteca
print("Preparando envio...")  #mostra alguma informação na tela. nativa
time.sleep(random.randint(1, 3))  # coloca um tempo para ler a próxima linha. biblioteca
print("Mensagem enviada!")#mostra alguma informação na tela.nativa
fim = time.time()#marca o tempo apos ser lida.biblioteca
print("enviou demorou", int(inicio-fim), "segundos")#mostra alguma informação na tela. nativa