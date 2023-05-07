import string, random

caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + '!@#$%*()_-=+`[]{}~^.,;?:/'
tamanho = int(input('Digite o tamanho da senha (1-87): '))
continuar = 'S'

while continuar == 'S':
    senha = ''.join(random.sample(caracteres, tamanho))
    print(f'Senha gerada: {senha}')
    continuar = str(input('Deseja gerar outra? S/N: ').upper())