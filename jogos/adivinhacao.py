import random

print("*********************************")
print("Bem vindo no jogo de adivinhação")
print("*********************************")

numero_secreto = round(random.randrange(1, 101))
total_de_tentativas = 0
pontos = 1000

print("Qual nivel de difiuldade?")
print("(1)- Facil")
print("(2)- Medio")
print("(3)- Dificill")

nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

print("Você tem 1000 pontos iniciais")
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
        print("** Fez {} pontos **".format(pontos))
        break
    else:
        if(maior):
            print("Você errou *-*. O seu chute foi MAIOR do que o número secreto")
        elif(menor):
            print("Você errou *-*. O seu chute foi MENOR do que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("FIM DE JOGO")
