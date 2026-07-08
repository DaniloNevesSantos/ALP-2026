def ola(nome, genero):
    if genero == "F" or genero == "f":
        return ("Olá", nome, "Bem vinda.")
    elif genero == "M" or genero == "m":
        return ("Olá", nome, "Bem vindo.")
    else:
        return ("Olá", nome, "bem vindo (a)")
n = input("Qual é o seu nome?")
g = input("Qual é seu gênero?")
    
resultado = ola(n, g)
print(resultado)