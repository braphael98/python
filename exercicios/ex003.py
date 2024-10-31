idade = int(input('Digite sua idade: '))
if idade <= 12:
    print (f'Você tem {idade} anos - Criança')
elif idade <= 18:
    print (f'Você tem {idade} anos - Adolescente')
else:
    print (f'Você tem {idade} anos - Adulto')