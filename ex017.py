# Faça um programa que leia o comprimento dos catetos de um triângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hip = hypot(co, ca)
print(f'A hipotenusa mede {hip}')
