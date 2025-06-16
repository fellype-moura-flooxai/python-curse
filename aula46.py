"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavrasecreta = 'computador'
letras_certas = ''
tentativas = 0

while True:

    letra_digitada = input('digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('digite apenas uma letra !')
        continue

    if letra_digitada not in palavrasecreta: 
        print('essa letra não tem está na palavra')
        continue

    if letra_digitada in palavrasecreta:
        letras_certas += letra_digitada

    palavraformando = ''
    for letra_secreta in palavrasecreta:
        if letra_secreta in letras_certas:
            palavraformando += letra_secreta
        else:
            palavraformando += '*'
            
    print ('Palavra formada: ', palavraformando)

    if palavraformando == palavrasecreta:
        print('Parabens voce ganhou com ', tentativas, ' tentativas')
        print('a palavra secre era', palavrasecreta)


