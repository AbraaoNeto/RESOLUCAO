# Crie um programa que avalie se carro  é velho ou novo.
carro = str(input('Digite o modelo do seu carro'))
tempo = int(input('Digite o ano do seu carro'))
print('O seu carro é {} e ano dele é {}'.format(carro, tempo))
if tempo >= 2017:
    print('Seu carro é novinho, voce pode trabalhar na Uber')
if tempo < 2000:
        print('Ja devia ter parado de rodar')
else:
    print('Seu carro é Velho, ainda pode circular mias voce está fora da Uber')



#Media usnado condições:

nt1 = float(input('Digite a primeira nota '))
nt2 = float(input('Digite a segunda nota '))
m = (nt1+nt2)/2
print('Sua media é {}'.format(m))
print('REPROVADO se'if m < 6.0 else 'APROVADO')
