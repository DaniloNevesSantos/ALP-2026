#1
def verificar (vet, numero):

    for i in range(0, 10):
    
        if vet[i] == numero:
            numero = i
    return (numero)
        
#2
def soma (vet, x, y):
    s = 0
    for i in range(0, 10):
        if vet[i] > x and vet[i] < y:
            s += vet[i]
            
    return(s)
    
#3
def extremos(vet):
    maior = 0
    menor = 0
    for i in range(0, 10):
        if maior < vet[i]:
            maior = vet[i]
        if menor > vet[i]:
              menor = vet[i]
        else:
              menor = vet[i]
              
    return(maior, menor)

#4
def pares (vet):
    soma = 0
    for i in range(0, 10):
        if vet[i] % 2 == 0:
            soma += i 
            
    return(soma)