usuario_correto = 'Padma'
senha_correta = 'senha secreta'

usuario = input('Nome de usuário: ')
senha = input('Senha: ')

usuario_esta_correto = usuario == usuario_correto
senha_esta_correta = senha == senha_correta

if usuario_esta_correto and senha_esta_correta:
    print(f'Acesso liberado, seja bem-vindo {usuario}!')

if usuario_esta_correto and not senha_esta_correta:
    print(f'Senha incorreta, usuário {usuario}!')

if not usuario_esta_correto:
    print(f'Usuário {usuario} não cadastrado no sistema')


