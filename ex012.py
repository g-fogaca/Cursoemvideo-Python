# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto
p = float(input('Qual o preço do produto? R$'))
print(f'O produto que custava R${p:.2f}, na promoção com desconto de 5% vai custar R${0.95*p:.2f}')
