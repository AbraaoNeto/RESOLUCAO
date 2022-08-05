# Crie um programa que leia o primeio e o ultimo nome.

n = str(input('Digite seu nome !'))
nome = n.split()
print('Muito prazer em te conhecer ')
print('Seu primeiro nome é {}'.format(nome[0]))
print('O seu ultimo nome é {}'.format(nome[len(nome)-1]))
