import random

dist_max = input('qual a distancia maxima que você deseja?')

if dist_max.isdigit():
    num_al = random.randint(0, int(dist_max))
    num_al =str(num_al)
else:
    print('escreva um número por favor!')
    quit()
while True :
    chute = input('faça um chute')
    if chute.isdigit():
        chute = str(chute)

    if chute < num_al:
        print('o numero sorteado está acima do numero que você chutou')
    if chute > num_al:
        print('o numero sorteado está abaixo do número que você chutou')
    if chute == num_al:
        print('parabéns você acertou!')
        break



