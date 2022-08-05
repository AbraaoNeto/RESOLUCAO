# Crie um programa que leia qual numero é o maior e o menor.
a = int(input('Digite oprimeiro numero '))
b = int(input('Digite o segundo numero '))
c = int(input('Digite o terceiro numero '))
menor = a
if b<a and b<c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a or c > b:
    maior = c
print('O menor numero é {}'.format(menor))
print('O maior numero é {}'.format(maior))

