import datetime

hoje = datetime.datetime.now()

data_prova = datetime.datetime(2026, 7, 14)

diferenca = abs(hoje - data_prova)

print(f'faltam {diferenca.days} dias para a prova')