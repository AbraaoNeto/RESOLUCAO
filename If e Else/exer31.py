# crie um programa que calcule o valor da passagem conforme o km.
# acima de 200 0.40, abaixo 0.50
distancia = float(input('Qual a distancia da sua viagem ?'))
print('A sua viagem é de {}km'.format(distancia))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor =  distancia * 0.40
print('O preço das sua viagem será R${:.2f}'.format(valor))
