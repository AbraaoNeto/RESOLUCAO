# Crie um programa que analise se ano é bisexto.
ano = int(input('Digite o ano que quer analizar '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} Não é Bissexto'.format(ano))
