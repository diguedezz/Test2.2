'''

O jogo da Velha 


1.	O Jogo da Velha é um jogo bem conhecido e pode ser implementado com base na teoria que aprendemos nesta semana. 
No Jogo da Velha, temos dois jogadores, O e X, que jogam sob um tabuleiro 3x3. 
Ganha o jogo quem preencher primeiro uma linha, uma coluna ou uma das diagonais. 

Seu objetivo neste exercício será implementar este jogo no modo texto. Para tanto:

a) Vamos representar o nosso tabuleiro como uma matriz de caracteres 3x3. 
Sua primeira função deverá devolver uma matriz de caracteres 3x3, 
com algum valor preenchido para indicar que uma posição não foi ocupada.

def initialize():
    ...
'''

#implementando a função initialize.
def initialize():
    grid = '.'
    matrix = [[grid for x in range (3)] for y in range (3)]
    return matrix


'''
b) Implemente uma função que receba uma matriz do jogo da velha, 
uma posição (linha, coluna) e o código do jogador (X ou O) e devolva a matriz com a posição 
preenchida com o código do jogador, caso esteja livre. Se a posição conseguiu ser preenchida,
step deve retornar true e, caso não puder ser preenchida, false. 

def step (M, lin, col, gamer):

    ...
'''

#implementando a função step.
def step(M, lin, col, gamer):
    passo = M[lin][col]
    if passo == '.':
        M[lin][col] = gamer
        return True
    else:
        return False

'''
c) Implemente uma função que receba uma matriz do jogo da velha e verifique o estado do jogo: 
alguém venceu, ocorreu um empate ou o jogo deve continuar. 
Vamos usar o seguinte código: -1 (o jogo pode continuar), 0 (ocorreu um empate), 1 (O venceu) e 2 (X venceu).

	
def status (M):
    ...
'''
jogadas = 0
geral = []

#implementando a funçao status.
def status(M):


    if jogadas <= 2:
        return -1
    else:
        x = geral[0][0]
        y = geral[0][1]

        if x == 0:
            posX1 = 1
            posX2 = 2
        elif x == 1:
            posX1 = 2
            posX2 = 0
        elif x == 2:
            posX1 = 0
            posX2 = 1

        if y == 0:
            posY1 = 1
            posY2 = 2
            contraY1 = 2
            contraY2 = 1
        elif y == 1:
            posY1 = 2
            posY2 = 0
            contraY1 = 0
            contraY2 = 2
        elif y == 2:
            posY1 = 0
            posY2 = 1
            contraY1 = 1
            contraY2 = 0


        #Primeiro vamos ver se alguem ganhou pelas linhas
        if (M[x][y] == 'X' or M[x][y] == 'O') and (M[x][y] == M[x][posY1]) and (M[x][y] == M[x][posY2]):
            if M[x][y] == 'X':
                return 2
            elif M[x][y] == 'O':
                return 1
        
        #Segundo vamos ver se alguem ganhou pelas colunas
        if (M[x][y] == 'X' or M[x][y] == 'O') and (M[x][y] == M[posX1][y]) and (M[x][y] == M[posX2][y]):
            if M[x][y] == 'X':
                return 2
            elif M[x][y] == 'O':
                return 1
        
        #Terceiro vamos ver se alguem ganhou pela diagonal principal
        if (M[x][y] == 'X' or M[x][y] == 'O') and (M[x][y] == M[posX1][posY1]) and (M[x][y] == M[posX2][posY2]):
            if M[x][y] == 'X':
                return 2
            elif M[x][y] == 'O':
                return 1

        # #Quarto vamos ver se alguem ganhou pela diagonal secundária
        if (M[x][y] == 'X' or M[x][y] == 'O') and (M[x][y] == M[posX1][contraY1]) and (M[x][y] == M[posX2][contraY2]):
            if M[x][y] == 'X':
                return 2
            elif M[x][y] == 'O':
                return 1

        if jogadas == 9:
            return 0
        else:
            return -1


'''
d) Implemente um procedimento para executar a lógica deste jogo. 
Suponha que o jogador O sempre começa. A cada jogada, a matriz do jogo deverá ser exibida na tela. 
Ao final do jogo, seu procedimento deve mostrar o estado a que se chegou (vitória ou empate). Teste o seu jogo. 

def game():

'''

import random
import time
import os

#implementando a função game.
def game():

    global jogadas
    global geral

    jogadorUm = input('\n*********************************************************\n\nPrimeiro nome?\n')
    jogadorDois = input('\nSegundo nome?\n')
    sorteio = random.randint(0,2)
    if sorteio == 1:
        reserva = jogadorUm
        jogadorUm = jogadorDois
        jogadorDois = reserva
    simboloUm = str.upper(input(f'\n{jogadorUm} será o primeiro a jogar!\nX ou O?\n'))
    while simboloUm != 'X' and simboloUm != 'O':
        simboloUm = str.upper(input('\nX ou O?\n'))
    if simboloUm == 'X':
        simboloDois = 'O'
    else:
        simboloDois = 'X'


    matrix = initialize()

    vez_deJogar = 0

    os.system('cls')
    status(matrix)
    while status(matrix) == -1:    

        historico = []
        geral = []
        if vez_deJogar%2 == 0:
            jogador = jogadorUm
            simbolo = simboloUm
        if vez_deJogar%2 == 1:
            jogador = jogadorDois
            simbolo = simboloDois
        
        time.sleep(1)
        print(f'\n\n*************************  vez de {jogador} jogar  *************************\n\n')
        print('\t\t\t     1    2    3')
        cont = 1
        for i in matrix:
            print('\t\t\t',cont,i)
            cont+=1
        historico.append(int(input(f'\nEm qual linha {jogador} deseja jogar?\n'))-1)
        historico.append(int(input(f'\nEm qual coluna {jogador} deseja jogar?\n'))-1)
        geral.append(historico)
        tentativa = step(matrix,geral[0][0],geral[0][1],simbolo)
                
        jogadas += 1

        while tentativa == False:

            jogadas -= 1
            historico = []
            geral = []

            print('\nA casa já está ocupada!\n')
            time.sleep(1)
            print('\t\t\t     1    2    3')
            cont = 1
            for i in matrix:
                print('\t\t\t',cont,i)
                cont+=1
            historico.append(int(input(f'\n\nEm qual linha {jogador} deseja jogar?\n'))-1)
            historico.append(int(input(f'\nEm qual coluna {jogador} deseja jogar?\n'))-1)
            geral.append(historico)
            tentativa = step(matrix,geral[0][0],geral[0][1],simbolo)
            
            print(f'\n\n*********************************************************')
        
        vez_deJogar += 1
        status(matrix)
        os.system('cls')
    
    time.sleep(1)
    print('\t\t\t     1    2    3')
    cont = 1
    for i in matrix:
        print('\t\t\t',cont,i)
        cont+=1
    time.sleep(1)
    if status(matrix) == 1:
        print(f'\n\n\n{jogador} venceu!\n\n\n')
    elif status(matrix) == 2:
        print(f'\n\n\n{jogador} venceu!\n\n\n')
    elif status(matrix) == 0:
        print('\n\n\nEmpate!\n\n\n')
        
    print(f'\n\n*********************************************************')
    



game()