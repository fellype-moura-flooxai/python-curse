while True:

    primeiro = input('digite um numero: ')
    operador = input('digite o operador: ')
    segundo = input('digite o outro numero: ')

    numerosvalidos = None

    try: 
        num_float = float(primeiro)
        num2_float = float(segundo)
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

    

    sair = input('Deseja sair? sim: ').lower()

    if sair.startswith('s'):
        print('afafafa')
        break




