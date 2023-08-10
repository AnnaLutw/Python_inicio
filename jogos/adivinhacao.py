print("*********************************")
print("Bem vindo no jogo de adivinhação")
print("*********************************")

numero_secreto = 43
total_de_tentativas = 3
rodada = 1

for rodada in range (1, total_de_tentativas + 1):
    print("*********************************")
    print("Tentativa:  {}  de  {}  ".format(rodada, total_de_tentativas ))
    chute_str = input("Digite o seu numero entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("VOCÊ ACERTOU, PARABENS!!")
        break
    else:
        if(maior):
            print("Você errou *-*. O seu chute foi MAIOR do que o número secreto")
        elif(menor):
            print("Você errou *-*. O seu chute foi MENOR do que o número secreto")

print("FIM DE JOGO")


