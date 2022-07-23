# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km.
t = int(input('Por quantos dias o carro foi alugado? '))
d = float(input('Quantos Km o carro percorreu? '))
c = t * 60 + d * 0.15
print(f'VALOR A PAGAR: R${c:.2f}')
