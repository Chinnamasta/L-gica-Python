valores = [10, 30, -8, 0, -2, 4]

soma = 0
for valor in valores:
    soma += valor

media = soma / len(valores)

print(f'A soma dos valores é {valores}: {soma}')
print(f'A media dos valores é {valores}: {media}')

print('\n\n\n')

valores = [10, 30, -8, 0, -2, 4]

maximo = valores[0]
for valor in valores:
    if valor > maximo:
        maximo = valor

print(f'O valor maximo dos {valores}: {maximo}')

print('\n\n\n')

palavras = ['oi', 'Python', 'programação', 'xxx']
for palavra in palavras:
    if len(palavra) >= 5:
        print(f'Encontrada palavra com 5+ caractere: {palavra}')
