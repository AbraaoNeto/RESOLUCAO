# Faça um programa que leia um numero qualquer e diga sua base de conversão.
# 01 binario 02 Otal. 03 Hexadecimal.
num = int(input('Digite um numero inteiro '))
print( '''Escolha uma das bases para conversão
[ 1 ] Binario
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opcao = int(input('Digite uma opção '))
if opcao == 1:
    print('{} convertido para binario é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Numero invalido, tente outra vez.')
