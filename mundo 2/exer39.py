from datetime import date
#Faça um programa que diga se o Jovem pode se alistar ou ja passou o prazo
# ou quanto tempo falta.
nasc = int(input('Digite o ano que voce nasceu? '))
anat = int(input('Digite o ano que estamos '))
idade = anat - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, anat))
if idade == 18:
    print('Parabens voce esta no prazo de alistamento')
elif idade > 18:
    sal = idade - 18
    ano = anat - idade
    print('Já passou o prazo do alistamento {} ano(s) (SERÁ MULTADO)'.format(sal))
    print('Seu alistamento será no ano de {} '.format(ano))
else:
    sal = 18 < idade
    print('Desculpa não chegou ainda sua data de alistameto falta {} ano(s)'.format(sal))
    ano = anat + idade

    print('Seu alistamento será em {} ano (s)'.format(ano))
# outra maneira

atual = date.today().year
nas = int(input(' Ano de nascimento: '))
idade = atual - nas
print('Quem nasceu em {} tem {} anos em {}'.format(nas, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente ')
elif idade > 18:
    saldo = idade - 18
    print('Você já passou do prazo de se alistar a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento será em {} ano (s)'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda n ão é templo de você se alistar a {} anos'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} ano (s)'.format(ano))