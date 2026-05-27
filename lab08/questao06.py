valor = 0
v = True
while True:
    saque = int(input("Qual valor que ele deseja sacar?  "))
    if v == True:
       if saque % 20 == 0:
            valor = saque % 20
            print("Saque realizado com sucesso!!!")
            break
       else:
            v = False
        
       if saque % 50 == 0:
            valor = saque % 50 
            print("Saque realizado com sucesso!!!")
            break
       else:
            v = False
            
       if saque % 100 == 0:
            valor = saque % 100
            print("Saque realizado com sucesso!!!")
            break
       else:
            v = False
    else:
        print("Não é possivel realizar o saque...")
        continue