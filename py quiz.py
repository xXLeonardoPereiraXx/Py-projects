import time
print('seja bem vindo ao seu primeiro jogo de quiz')
ent =input("para continuar escreva \"pronto\":")

if ent == "pronto":
    score = 0
    print("Ótimo, vamos começar!")
    print("este quiz possuirá um sistema de pontos...")
    print('quanto mais perguntas você acertar, maior será seu score...')
    print("no final do quiz você verá quantas perguntas acertou e quantas errou.")
    print("Começando em...")
    for i in range(3):
        print(i)
        time.sleep(1)
    resp = input("qual é o maior osso do corpo humano?")
    if resp == "femur":
        score+=1

    resp = input("quantas gramas de creatina uma pessoa de 60kg precisa tomar todos os dias?")
    if resp == "3":
        score += 1

    resp = input("qual a cor do cavalo branco de napoleão?")
    if resp == "branco":
        score += 1

    for i in range(3):
        print(i)
        time.sleep(1)
    print('parabéns, seu total de acertos foi '+str(score))
    if score <=0:
        print("infelizmente você não acertou nenhuma, mais sorte da próxima vez!")
        print("sua pontuação foi "+str(score))



else:
    print("vai trabalhar então ótario")
