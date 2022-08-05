# Crie um programa aque leia a fraze e diga:
# Quantas vezes arece a letra ( a )
# Em qual posição ela aparece a primeira vez
#  Em qual posição ela aparece a ultima vez


frase = str(input('Digite uma frase ')).upper().strip()
print('A letra a aparece {} vezes na frase'.format(frase.count('A')))
print('A letra aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra aparece pela ultima vez na posição {}'.format(frase.rfind('A')))