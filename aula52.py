"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
lista = ['maça', 'limão', 'pera', 'banana', 'uva']

while True:

    opcoes = input('Digite uma opção: \n[a] para adcionar um item \n[b] para apagar um item \n[c] para listar \n[s] para sair \n ->: ')
        
    if opcoes not in ['a', 'b', 'c', 's']:

        print('Voce precisa digitar uma opção valida')
        continue
        

    if opcoes == 'a': 
        itemadd = input('escreve oque deseja adcionar: ')
        lista.append(itemadd)
        print(f'{itemadd} adcionado a lista sua lista atualizada esta assim: \n{lista}')
        continue

    if opcoes == 'b':
        if not lista:
            print('A lista está vazia. Nada para apagar.')
            continue

        try:
            itemdel = int(input('coloque o numero do item que vc deseja excluir: '))

            if 0 <= itemdel < len(lista):
                print('voce excluiu ', lista[itemdel])
                del(lista[itemdel])
                print('sua lista esta assim: ', lista)
            else:
                print('Só é possível apagar itens que estão na lista (índice inválido).')
            
        except:
            print('Você precisa digitar um número válido.')

    if opcoes == 'c':
        print(f'essa é a lista: {lista}')
        continue

    if opcoes == 's':
        break



