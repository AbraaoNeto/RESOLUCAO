# Criar um programa que leia a cidade que voce nasceu e diga se começa com santo.
cid = str(input('Digite a cidade que voce nasceu ')).strip()
print(cid[:5].upper() == 'SANTO')
 # quando colocamos  .upper() o nome tem que ser maisuculo para comparação
 # o usuario pode digitar o nome (santo) de qualquer forma.
