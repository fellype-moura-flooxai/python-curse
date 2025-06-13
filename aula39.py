while True:

    primeiro = input('digite um numero: ')
    operador = input('digite o operador: ')
    segundo = input('digite o outro numero: ')
    primeiro_float = 0
    segundo_float = 0
    numerosvalidos = None


    try: 
        primeiro_float = float(primeiro)
        segundo_float = float(segundo)
        numerosvalidos = True
    except:
        numerosvalidos = None

    if numerosvalidos is None:
        print('o numero digitado é invalido')
        continue

    operadoresvalidos = '+-/*'

    if len(operador) > 1:
        print('digite só um operador')
        continue

    if operador not in operadoresvalidos:
        print('operador invalido')
        continue

    if operador == '+':
        print (f'O resultado de {primeiro} + {segundo} é: {primeiro_float + segundo_float}')
    elif operador == '-':
        print (f'O resultado de {primeiro} - {segundo} é: {primeiro_float - segundo_float}')
    elif operador == '*':
        print (f'O resultado de {primeiro} * {segundo} é: {primeiro_float * segundo_float}')
    elif operador == '/':
        print (f'O resultado de {primeiro} / {segundo} é: {primeiro_float / segundo_float}')
    else :
        print('n era pra chegar aqui')

    sair = input('Deseja sair? sim: ').lower()

    if sair.startswith('s'):
        print('afafafa')
        break




