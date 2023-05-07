import string
import random

minusculas = string.ascii_lowercase
maiusculas = string.ascii_uppercase
numeros = string.digits
especiais = '@#$%^&*()!'

all = minusculas + maiusculas + numeros + especiais
tamanho = 12
continuar = 'S'

while continuar == 'S':
    senha = ''.join(random.sample(all, tamanho))
    print(f'Senha gerada: {senha}')
    continuar = str(input('Deseja gerar outra? S/N: ').upper())