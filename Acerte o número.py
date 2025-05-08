numero_secreto=10
descobriu = False

for n in range(3):
    if not descobriu:
        chute = int(input('Descubra o número secreto!\nSeu chute: '))
        if chute < numero_secreto:
            print('Chute muito baixo!')
        elif chute > numero_secreto:
            print('Chute muito alto!')
        else:
            print('Descobriu o número secreto!')
            descobriu = True

if descobriu:
    print('Parabéns, você descobriu o número secreto!')
else:
    print(f'Que pena, não foi dessa vez! O número secreto era {numero_secreto}')
