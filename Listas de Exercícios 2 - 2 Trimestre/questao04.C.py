import datetime
hoje = datetime.datetime.now()  #mostra quanto tempo se passou desde 1970. biblioteca
resposta = input("Incluir anos? (S/N)") # espera um comando do usuario. nativa
if resposta == "S":
    print(f"{hoje.day}/{hoje.month}/{hoje.year}")#mostra alguma informação na tela. nativa
else:
    print(f"{hoje.day}/{hoje.month}")#mostra alguma informação na tela. nativa