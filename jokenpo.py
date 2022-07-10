
print('--------------------------------------------------------------------')
print('|  Bem vindo ao jogo "Pedra, Papel e Tesoura"! [ Você x Máquina ]  |')
print('--------------------------------------------------------------------')

pedra, papel, tesoura = 1, 2, 3
ponto_voce = 0
ponto_maquina = 0
empate = 0

while True:

    print('--------------------------------------------------------------------')
    jogador = input(f'>>>>> Escolha "1" para Pedra, "2" para papel e "3" para Tesoura: ')
    print('--------------------------------------------------------------------')



    if not jogador.isnumeric():
        print('ERRO! É nescessário digitar um número de 1 a 3 para jogar.')
        continue
    else:
        jogador = int(jogador)
        if jogador > 3 or jogador < 1:
            print('POR FAVOR, digite um número de 1 a 3 para jogar.')
            continue


        if jogador == 1:
            jogador1 = pedra
            jogador1 = '1 para Pedra'
        elif jogador == 2:
            jogador1 = papel
            jogador1 = '2 para papel'
        elif jogador == 3:
            jogador1 = tesoura
            jogador1 = '3 para Tesoura'

        from random import randint
        maquina = (randint(1, 3))

        if maquina == 1:
            maquina1 = pedra
            maquina1 = '1 para Pedra'
        elif maquina == 2:
            maquina1 = papel
            maquina1 = '2 para Papel'
        elif maquina == 3:
            maquina1 = tesoura
            maquina1 = '3 para Tesoura'

        print(f'>>>>> Você digitou: "{jogador1}"!')
        print('--------------------------------------------------------------------')

        print(f'>>>>> A Máquina digitou: "{maquina1}"!')
        print('--------------------------------------------------------------------')

        if jogador == pedra and maquina == papel or jogador == tesoura and maquina == pedra \
                or jogador == papel and maquina == tesoura:
            ponto_maquina += 1
            print(f'>>>>> VOCÊ PERDEU! Ponto para a "Máquina".')
            print('--------------------------------------------------------------------')
            print()
            print(f'##################')
            print(f'Placar atualizado:')
            print(f'Você = {ponto_voce}')
            print(f'Máquina = {ponto_maquina}')
            print(f'Empate = {empate}')
            print(f'##################')
        elif jogador == maquina:
            empate += 1
            print('>>>>> EMPATE')
            print('--------------------------------------------------------------------')
            print()
            print(f'##################')
            print(f'Placar atualizado:')
            print(f'Você = {ponto_voce}')
            print(f'Máquina = {ponto_maquina}')
            print(f'Empate = {empate}')
            print(f'##################')
        else:
            ponto_voce += 1
            print('>>>>> VOCÊ VENCEU! uhuuuu')
            print('--------------------------------------------------------------------')
            print()
            print(f'##################')
            print(f'Placar atualizado:')
            print(f'Você = {ponto_voce}')
            print(f'Máquina = {ponto_maquina}')
            print(f'Empate = {empate}')
            print(f'##################')
        print()

        jogar = input('Jogar de novo? Digite S (sim) ou N (não): ')
        jogar = jogar.upper()

        if jogar == 'S':
            import os
            os.system('cls') # or None
            print(f'###############')
            print(f'Placar atual:')
            print(f'Você = {ponto_voce}')
            print(f'Máquina = {ponto_maquina}')
            print(f'Empate = {empate}')
            print(f'###############')
            continue
        else:

            import os
            os.system('cls') # or None
            print('Obrigado por jogar!')
            print()
            print(f'###############')
            print(f'Placar Final:')
            print(f'Você = {ponto_voce}')
            print(f'Máquina = {ponto_maquina}')
            print(f'Empate = {empate}')
            print(f'###############')

            from time import sleep

            sleep(3)
            break

