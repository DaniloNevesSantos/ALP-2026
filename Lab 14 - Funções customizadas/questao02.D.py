def calculadora(n1, n2, operador):
    if operador == "+":
        soma = n1 + n2
        return soma
    if operador == "-":
        if n1 > n2:
            soma = n1 - n2
            return soma
        else:
            soma = n2 - n1
            return soma
    if operador == "*":
        soma = n1 * n2
        return soma
    if operador == "/":
        soma = n1 / n2
        return soma

n1 = int(input("Qual é o primeiro número? "))
n2 = int(input("Qual é o segundo número? "))
operador = input("Qual é a operação? ")
print(calculadora(n1, n2, operador))