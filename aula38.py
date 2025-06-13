#iterando strings com while


nome = 'fellype' 
num_letra_nome = 0
novo_nome = ''

while num_letra_nome < len(nome):
    letra = nome[num_letra_nome]
    novo_nome += f'*{letra}'
    num_letra_nome += 1

    print(f'{novo_nome}*')

