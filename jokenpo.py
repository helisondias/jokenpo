import random
from time import sleep
print('\033[33m-=\033[m'*10, '\033[31mSeja bem vindo ao pedra, papel e tesoura!\033[m', '\033[33m-=\033[m'*10)
sleep(1)
escolha=str(input('Por favor, escolha uma das opções: Pedra, Papel ou Tesoura: ')).strip().title()
lista = ('Pedra','Papel','Tesoura')
random = random.choice(lista)
print('\033[34mPedra\033[m')
sleep(0.5)
print('\033[34mPapel\033[m')
sleep(0.5)
print('\033[34mTesoooooura!\033[m')
sleep(0.5)
print(random)
print(escolha)
if escolha == 'Pedra':
    if random == 'Pedra':
        print('O jogador escolheu \033[31mPedra\033[m e o computador escolheu \033[31mPedra\033[m, os 2 empataram!')
    elif random == 'Papel':
        print('O jogador escolheu \033[31mPedra\033[m e o computador escolheu \033[36mPapel\033[m, o computador venceu!')
    elif random == 'Tesoura':
        print('O jogador escolheu \033[31mPedra\033[m e o computador escolheu \033[33mTesoura\033[m, o jogador venceu!')
if escolha == 'Papel':
    if random == 'Pedra':
        print('O jogador escolheu \033[31mPapel\033[m e o computador escolheu \033[31mPedra\033[m, o jogador venceu!')
    elif random == 'Papel':
        print('O jogador escolheu \033[31mPapel\033[m e o computador escolheu \033[36mPapel\033[m, os 2 empataram!')
    elif random == 'Tesoura':
        print('O jogador escolheu \033[31mPapel\033[m e o computador escolheu \033[33mTesoura\033[m, o computador venceu!')
if escolha == 'Tesoura':
    if random == 'Pedra':
         print('O jogador escolheu \033[31mTesoura\033[m e o computador escolheu \033[31mPedra\033[m, o computador venceu!')
    elif random == 'Papel':
        print('O jogador escolheu \033[31mTesoura\033[m e o computador escolheu \033[36mPapel\033[m, o jogador venceu!')
    elif random == 'Tesoura':
         print('O jogador escolheu \033[31mTesoura\033[m e o computador escolheu \033[33mTesoura\033[m, os 2 empataram!')
