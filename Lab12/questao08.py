import datetime

pessoa1 = input("Nome da primeira pessoa:  ")
nascimento1 = (input("a primeira data deve ser digitada no formato (dd/mm/aaaa):  "))
pessoa2 = input("Nome da segunda pessoa:  ")
nascimento2 = input("a segunda data deve ser digitada no formato (dd/mm/aaaa):  ")

data1 = datetime.datetime.strptime(nascimento1, "%d/%m/%Y")
data2 = datetime.datetime.strptime(nascimento2, "%d/%m/%Y")

hoje = datetime.datetime.now()

aniv1 = datetime.datetime(hoje.year, data1.month, data1.day)
if aniv1 < hoje:
    aniv1 = datetime.datetime(hoje.year + 1, data1.month, data1.day)

aniv2 = datetime.datetime(hoje.year, data2.month, data2.day)
if aniv2 < hoje:
    aniv2 = datetime.datetime(hoje.year + 1, data2.month, data2.day)

falta1 = (aniv1 - hoje)
falta2 = (aniv2 - hoje)

if falta1 < falta2:
    print(f"O aniversário mais próximo é o de {pessoa1}: {aniv1}")
elif falta2 < falta1:
    print(f"O aniversário mais próximo é o de {pessoa2}: {aniv2}")