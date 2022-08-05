#Faça um programa para calcular emprestimo para comprar uma casa.
# sabendo o salario e que pode comprometer 30% na pretação
casa = float(input('Valor da casa? '))
sal = float(input('Valor do salário? '))
ano = int(input('Quantos anos? '))
par = casa / (ano * 12)
minimo = sal / 100 * 30
if par <= minimo:
    print('Seu Empretimo de R${:.2f} foi APROVADO, será pago {:.0f} anos com parcelas de R${:.2f}'.format(casa,ano,par))
else:
    print('\033[0;30;45m O seu emprestimo NÃO foi Aprovado, a prestação compromete mais de 30% do seu rendimento. \033[m')