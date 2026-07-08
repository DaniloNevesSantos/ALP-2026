def classificar_nota(nota):
    if nota >= 60:
       print("Aprovado")
    else:
        print("Reprovado")
nota= int(input("Qual é a nota? "))
classificar_nota(nota)