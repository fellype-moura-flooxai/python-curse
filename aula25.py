"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Fellype'
preço = 1200.23525
resultado = ' o preço é de  R$ %.2f, ok %s' %(preço, nome)
print(resultado)

print('o hexadecimal de %.i é %.x' %(12, 12))