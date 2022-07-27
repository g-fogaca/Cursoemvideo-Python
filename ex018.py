# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan
theta_degrees = float(input('Digite um ângulo : '))
theta_rad = radians(theta_degrees)
print(f'''sin({theta_degrees}º) = {sin(theta_rad):.2f}
cos({theta_degrees}º) = {cos(theta_rad):.2f}
tan({theta_degrees}º) = {tan(theta_rad):.2f}''')
