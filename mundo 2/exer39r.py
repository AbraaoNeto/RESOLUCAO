
# Faça um programa que diga se o Jovem pode se alistar ou ja passou o prazo
# ou quanto tempo passou do parazo ou falta.
nome = str(input('Digite seu nome. '))
nasc = int(input('Digite o ano que voce nasceu. '))
anat = int(input('Digite o ano que estamos. '))
idade = anat - nasc
print('Sr.(a) {}, nasceu no ano de {}, e está com {} anos.'.format(nome, nasc, idade, ))
if idade == 18:
    print('Parabens voce esta no prazo de alistamento.')
elif idade > 18:
    sal = idade - 18
    print('\033[2;30;41mJá passou {} ano(s) do prazo do alistamento. Você será MULTADO )\033[m'.format(sal))
    ano = anat - sal
    print('Seu alistamento foi no ano de {} '.format(ano))
elif idade < 18:
    sal = 18 - idade
    print('Desculpa não chegou ainda sua data de alistameto falta {} ano(s)'.format(sal))
    ano = anat + sal
    print('Seu alistamento será em \033[0;30;45m{}\033[m ano (s)'.format(ano))
    # outra maneira
