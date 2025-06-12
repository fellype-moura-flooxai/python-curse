# Operadores in e not in
# Strings são iteráveisAdd commentMore actions
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Fellype'
# print(nome[4])
# resultado : y 
# print(nome[-4])

# print('lyp' in nome)
# resulta em true
# print('zero' in nome)
# print(10 * '-')
# print('lyp' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')