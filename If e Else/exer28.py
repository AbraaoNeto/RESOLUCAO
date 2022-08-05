from random import randint
from time import sleep
# Jogo de adivinhação.
num = int(input('Digite um numero '))
print('----Processando----')
sleep(3)
computador = randint(0, 5)
print('Pensei num numero {} '.format(computador))
print('\033;0;30;41m Você Ganhou'if num == computador else 'Perdeu Baitola')