from time import sleep

print('=' * 30)
print('      MINI CTF v1.0')
print('=' * 30)

print('PERGUNTA 1:')
r = int(input('Quanto é 15 x 3? '))

print('PROCESSANDO...')
sleep(3)

if r == 45:
    print('Correto!')

    print('=' * 10)
    sleep(3)

    print('PERGUNTA 2:')
    sleep(2)
    r2 = int(input('Qual a raiz quadrada de 81? '))

    print('PROCESSANDO...')
    sleep(3)

    if r2 == 9:
        print('Correto!')
        sleep(2)
        print('FLAG: CTF{FIRST_PYTHON_CHALLENGE}')
    else:
        print('Resposta errada!\nTente novamente!')

else:
    print('Resposta errada!\nTente novamente...')
