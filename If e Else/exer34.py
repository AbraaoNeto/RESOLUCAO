# Crie um programa que calcule o reajuste do salarrio. se o salario for até 1250.
# 15% se mais 10%.
sal = float(input('Digite seu salario '))
if sal <= 1250:
    nsal = sal + (sal * 15 / 100)
    print('Meu salario era {:.2f} teve um ajuste de 15% e ficou {:.2f} '.format(sal,nsal))
else:
    nsal = sal + (sal * 10 / 100)
    print('Meu salario era {:.2f}, teve um ajuste de 10% e ficou {:.2f} '.format(sal,nsal))

