### Faça um programa que leia algo pelo teclado e mostre na tela
### o seu tipo primitivo e todas as informações possíveis sobre ele
x = input('Digite algo: ')
tipo = type(x)
print(f'O tipo primitivo desse valor é {tipo}')
print(f'Só tem espaços? {x.isspace()}')
print(f'É um número? {x.isnumeric()}')
print(f'É alfabético? {x.isalpha()}')
print(f'É alfanumérico? {x.isalnum()}')
print(f'Está em maiúsculas? {x.isupper()}')
print(f'Está em minúsculas? {x.islower()}')
print(f'Está capitalizada? {x.istitle()}')