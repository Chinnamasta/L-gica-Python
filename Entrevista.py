Nome=input("Qual o seu nome?\nDigite aqui: ")
Idade=input("Qual a sua idade?\nDigite aqui: ")

print('-----')
print(f'Olá, {Nome}')

n_letras=len(Nome)
n_letra_str=str(n_letras)
print(f'Seu nome tem {len(Nome)} letras.')

Idade_Futuro=int(Idade)+5
Idade_Futuro_str=str(Idade_Futuro)
print(f'Daqui 5 anos você terá {int(Idade)+5} anos.')
print('-----')
