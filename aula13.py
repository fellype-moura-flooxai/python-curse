nome = 'Fellype Moura'
altura = 1.64
peso = 68
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# fellype tem 1.64 de altura,
# pesa 68 quilos e seu IMC é
# 25.282569898869724