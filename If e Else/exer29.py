# Radar de Velocidade
print('++' * 30)
vel = float(input('Digite a velocidade do seu carro ! '))
if vel >= 100:
    print('####MULTADO "Gravissima" Valor R$ 1000,00  CNH CASSADA #### ')
elif (vel > 60) and (vel <= 99):
    print('MULTADO "Valor R$ 134,00  4 pontos na CNH " ')
else:

    print('Parabens!!! Você está a {} km/h, você é excelente motorista.'.format(vel))
print('++' * 30)

# Faça um programa que calcule a velocidade e diga se excedeu 80km e a cada km
# que passar, seje cobrado 7,00 por km excedido.

velocidade = float(input('Qual a velocidade do seu carro ?'))
if velocidade > 80:
    print('Voce excedeu o limite de velocidade que é 80km/h')
    multa = (velocidade-80)*7
    print('Voce excedeu o limite de velocidade {}km/h e pagara multa no valor R${:.2f}'.format(velocidade,multa))