soma = 0
while soma < 100:
    num = int(input("Escolha um número:  "))
    if num  < 0 :
        continue
    
    if num  == 0:
        print(f'Soma: {soma}')
        break
    soma += num
    print(soma)
    
print(f'Soma: {soma}')