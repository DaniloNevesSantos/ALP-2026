import datetime

pessoa1 = input("Nome da primeira pessoa:  ")
nascimento1 = (input("a primeira data deve ser digitada no formato (dd/mm/aaaa):  "))
pessoa2 = input("Nome da segunda pessoa:  ")
nascimento2 = input("a segunda data deve ser digitada no formato (dd/mm/aaaa):  ")

data1 = datetime.datetime.strptime(nascimento1, "%d/%m/%Y")
data2 = datetime.datetime.strptime(nascimento2, "%d/%m/%Y")
if data1 > data2:
    print(f'{pessoa1} é mais velha que {pessoa2}.')
else:
    print(f'{pessoa2} é mais velha que {pessoa1}.')