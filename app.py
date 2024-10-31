import os

restaurantes = [{'nome':'Aoshi', 'categoria':'japonesa','ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza','ativo':True},
                {'nome':'Joes', 'categoria':'hamburger','ativo':False}
                ]

def exibir_nome():
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n ')

def finalizar_app():
   exibir_subtitulo('Programa Finalizado !')
   
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
    
def retorno_menu():
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opcção invalida !\n')
    retorno_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante, para cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'{nome_restaurante} Cadastrado com sucesso !\n')
    retorno_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'*{nome_restaurante} | {categoria} |{ativo}\n')

    retorno_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
                finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()       

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
