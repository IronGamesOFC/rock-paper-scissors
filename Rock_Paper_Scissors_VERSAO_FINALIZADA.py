import random

placar = 0
placar_dois = 0
empate = 0

while True:
    computador = random.randint(1, 3)
    escolha = int(input('\nEscolha entre 1, 2 e 3: '))

    # ESCOLHA DO PLAYER
    if escolha == 1:
        player = 'Pedra'
    elif escolha == 2:
        player = 'Papel'
    elif escolha == 3:
        player = 'Tesoura'
    else:
        print('Escolha inválida! Escolha apenas 1, 2 ou 3.')
        continue

    # ESCOLHA DO COMPUTADOR
    if computador == 1:
        computador_nome = 'Pedra'
    elif computador == 2:
        computador_nome = 'Papel'
    else:
        computador_nome = 'Tesoura'

    print(f'\nVocê escolheu: {player}')
    print(f'Computador escolheu: {computador_nome}')

    # PLAYER GANHA
    if escolha == 1 and computador == 3:
        placar += 1
        print('Player ganhou!')

    elif escolha == 2 and computador == 1:
        placar += 1
        print('Player ganhou!')

    elif escolha == 3 and computador == 2:
        placar += 1
        print('Player ganhou!')

    # COMPUTADOR GANHA
    elif escolha == 1 and computador == 2:
        placar_dois += 1
        print('Computador ganhou!')

    elif escolha == 2 and computador == 3:
        placar_dois += 1
        print('Computador ganhou!')

    elif escolha == 3 and computador == 1:
        placar_dois += 1
        print('Computador ganhou!')

    # EMPATE
    else:
        empate += 1
        print('Empate!')

    # PLACAR
    print(f'\nPlacar Player: {placar}')
    print(f'Placar Computador: {placar_dois}')
    print(f'Empates: {empate}')

    continuar = input('\nDeseja continuar? s/n: ')

    if continuar == 'n':
        print('\nJogo encerrado!')
        break
