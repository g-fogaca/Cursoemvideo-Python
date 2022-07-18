# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
brl = float(input('Quantos reais você tem na carteira? R$'))
usd_brl = 5.42
eur_brl = 5.50
gbp_brl = 6.49
jpy_brl = 0.039
print('Com esse dinheiro você pode comprar:')
print(f'USD {brl/usd_brl:.2f}')
print(f'EUR {brl/eur_brl:.2f}')
print(f'GBP {brl/gbp_brl:.2f}')
print(f'JPY {brl/jpy_brl:.2f}')
