# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2m²
altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura
tinta = area / 2
print(f'A parede tem {area:.2f} m²')
print(f'Serão necessários {tinta:.2f} L de tinta para pintá-la')
