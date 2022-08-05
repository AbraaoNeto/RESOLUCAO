#Faça um programa que compare dois numeros e diga qual é o maior.
num1 = int(input('Digite um numero'))
num2 = int(input('Digite outro numero'))
if num1 > num2:
    print('\033[2;30;41m {} é maior\033[m'.format(num1))
elif num2 > num1:
    print('\033[2;30;41m {} é maior\033[m'.format(num2))
else:
    print('Essee numeros são iguais !!!')

