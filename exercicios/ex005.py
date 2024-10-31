eixo_x = int(input('Digite o eixo X: '))
eixo_y= int(input('Digite o eixo y: '))

if eixo_x and eixo_y > 0:
    print('Primeiro quadrante do plano cartesiano')
elif eixo_x < 0 and eixo_y > 0:
    print('Segundo Quadrante do plano cartesiano')
elif eixo_x and eixo_y < 0:
    print('Terceiro quadrante do plano cartesiano') 
elif eixo_x > 0 and eixo_y < 0:
    print('Quarto Quadrante do plano cartesiano')
else:
 print('o ponto está localizado no eixo ou origem')  




