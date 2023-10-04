#Biblioteca utilizada para limpar o terminal
import os

#Caso o símbolo não o agrade, dá pra mudar
x="✕"
o="◯"

while True:
    os.system('cls')#Comando que limpa o terminal
    v=[0,"1","2","3","4","5","6","7","8","9"]#Vetor usado para as 9 posições do jogo, desconsiderei o 0 para não ficar confuso durante a criação do código
    player=1#O jogo sempre começará no player 1 e lá pra frente trocará pro outro
    escolha=str(input(f"Player 1: {x} ou {o} ? "))#Variável responsável pela x e o

    #Caso digite os sinais de outras maneiras:
    if escolha=="x" or escolha=="X":
        escolha=x
    if escolha=="o" or escolha=="O" or escolha=="0":
        escolha=o

    while True:
        os.system('cls')
        print(f"Player {player}, {escolha} : Escolha o lugar")#Desenhar como está indo o caminhar do jogo
        print("",v[1]," │",v[2]," │",v[3],"")
        print("────┼────┼────")
        print("",v[4]," │",v[5]," │",v[6],"")
        print("────┼────┼────")
        print("",v[7]," │",v[8]," │",v[9],"")

        n=int(input())#Inserir o número da posição no tabuleiro
        while (v[n]==x or v[n]==o):#Enquanto se digitar o N da posição já preenchida, o código não deixa avançar
            n=int(input(""))
        v[n]=escolha#Coloca o x ou o, dependendo de quem for a vez na posição do vetor correspondente ao N digitado

        #Quantidade de opções de vitória
        if (v[1]==escolha and v[2]==escolha and v[3]==escolha) or (v[4]==escolha and v[5]==escolha and v[6]==escolha) or (v[7]==escolha and v[8]==escolha and v[9]==escolha) or (v[1]==escolha and v[4]==escolha and v[7]==escolha) or (v[2]==escolha and v[5]==escolha and v[8]==escolha) or (v[3]==escolha and v[6]==escolha and v[9]==escolha) or (v[1]==escolha and v[5]==escolha and v[9]==escolha) or (v[3]==escolha and v[5]==escolha and v[7]==escolha):
            os.system('cls')
            print(f"Player {player}: {escolha}  Ganhou ")
            print("",v[1]," │",v[2]," │",v[3],"")
            print("────┼────┼────")
            print("",v[4]," │",v[5]," │",v[6],"")
            print("────┼────┼────")
            print("",v[7]," │",v[8]," │",v[9],"")
            print("Pressione qualquer tecla para recomeçar")
            again=str(input())
            break

        #Caso todos forem preenchidos e não caiu no if anterior, então deu velha
        if v[1]!="1" and v[2]!="2" and v[3]!="3" and v[4]!="4" and v[5]!="5" and v[6]!="6" and v[7]!="7" and v[8]!="8" and v[9]!="9":
            grandma=str(input("Vish deu Velha"))
            break

        #Onde se troca para o próximo player
        if escolha==o:
            escolha=x
        else:
            escolha=o

        if player==1:
            player=2
        else:
            player=1
