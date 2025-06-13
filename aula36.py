contador = 0

while contador <= 50:
    print(contador)
    contador += 1

    if contador >= 10 and contador <= 20 :
        print(f'continue executou no {contador}')
        continue

    if contador == 40:
        print(f'break agiu no {contador} e parou')
        break