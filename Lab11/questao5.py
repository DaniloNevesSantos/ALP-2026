chances = 10
for a in  range (0, 9):
    print(a)
for b in range (0, 9):
    print(b)
for c in  range(0, 9):
    print(c)

while chances > 0:
    palpite_a = int(input("Qual é o seu palpite para o primeiro digito:  "))
    palpite_b = int(input("Qual é o seu segundo para o primeiro digito:  "))
    palpite_c = int(input("Qual é o seu terceiro para o primeiro digito:  "))

    chances -= 1

    if  palpite_a == a and palpite_b == b and palpite_c == c:
        print("+ + +")
        print("Parabéns! Você acertou!")
        break
    else:
        print("_ _ _")
        print(f'chances: {chances}')

    if  palpite_a == a and palpite_b != b and palpite_c != c:
        print("+ _ _")
        print(f'chances: {chances}')
    
    if palpite_a != a and palpite_b == b and palpite_c != c:
        print("_ + _")
        print(f'chances: {chances}')

    if palpite_a != a and palpite_b != b and palpite_c == c:
        print("_ _ +")
        print(f'chances: {chances}')
