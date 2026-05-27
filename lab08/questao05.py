print("Cardápio")
print("1. Açaí 300ml - R$ 12")
print("2. Mousse - R$ 6,50")
print("3. Salada de frutas - R$ 10")
print("4. Fechar a conta")
saldo = 0

while True:  # loop infinito
   opcao = float(input("Escolha uma opção:  "))
   
   if opcao > 4:
       print("opção fora do caerdápio! ")
       continue
   
   if opcao < 0:
       print("opção fora do caerdápio! ")
       continue
   
   if opcao == 1:
        print("Açaí 300ml - R$ 12")
        saldo += 12
        
   if opcao == 2:
       print("Mousse - R$ 6,50")
       saldo += 6.50
       
   if opcao == 3:
        print("Salada de frutas - R$ 10")
        saldo += 10
        
   if opcao == 4:
        print("Fechar a conta...")
        print(f'Saldo TOTAL: {saldo}')
        break