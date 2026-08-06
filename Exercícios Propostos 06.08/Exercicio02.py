def temperatura (c):
    fahrenheit = (c*1.8)+32
    return fahrenheit

celsius = float(input("Qual é a temperatura a ser convertida: "))
temp = temperatura (celsius)
print(f"A temperatura em celsius: {celsius} em fahrenheit é: {temp}")
