senha = '1234'
user  = 'bruno123'
user_in = input('Digite o nome de usuario:')
if user_in == user:
    password_in = input('Digite a senha: ')
    if password_in == senha:
        print ('Acesso permitido')
    else:
        print ('Acesso negado')
else:
    print('Usuario não encontrado')