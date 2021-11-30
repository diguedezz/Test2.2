'''
Exercício 0 da Avaliação: 
Faça um programa que leia de um arquivo o codigo de matrícula dos dois integrantes da dupla, 
adicione os digitos em uma única matriz. 
(se Voce fizer a prova sozinho ou em duplas complete as linhas da matriz com o valor 1, até completar 3 linhas), 
ao final todos devem ter uma matriz 8x3. 

'''
#gerando a primeira matriz 8x3



matrix = [

    [3,2,1,4,8,1,2,7],

    [3,2,1,1,6,2,5,1],

    [3,2,1,5,2,2,8,0],

]

# import random
# #inserindo uma função para calcular a determinante da matriz 8x8

# def completer():
#   # vamos criar o complemento da matriz
#   Complemento = []
#   for n in range(8):
#     Complemento.append(random.randint(0,9))
#   return Complemento


# for i in range (5):
#   matrix.append(completer())
# for j in matrix:
#   print(j)


#RESERVAMOS A PRIMEIRA MATRIZ GERADA COM O CODIGO ACIMA:
matrix = [
  [3, 2, 1, 4, 8, 1, 2, 7],
  [3, 2, 1, 1, 6, 2, 5, 1],
  [3, 2, 1, 5, 2, 2, 8, 0],
  [4, 7, 4, 5, 7, 6, 1, 1],
  [3, 3, 7, 2, 4, 7, 7, 6],
  [4, 0, 7, 2, 8, 4, 9, 5],
  [9, 5, 3, 8, 1, 1, 0, 9],
  [0, 4, 5, 7, 6, 9, 3, 5]
  ]
   
  # calcula o determinante usando a Regra de Sarrus
y = 0
for x in range (0,8):
  det = (matrix[x][y])
  y+=1
s1=s2=s3=s4=s5=s6=s7=s8 = 0
d1=d2=d3=d4=d5=d6=d7=d8 = 0


#multiplicando as diagonais e adicionando às variaveis
x = 0
pos = x+1
for y in range(0,7):
  if x > 7:
    pos = 0
  s1 += matrix[x][y] * matrix[pos][y+1] 
  x=1
  s2 += matrix[x][y] * matrix[pos][y+1] 
  x=2
  s3 += matrix[x][y] * matrix[pos][y+1]
  x=3
  s4 += matrix[x][y] * matrix[pos][y+1] 
  x=4
  s5 += matrix[x][y] * matrix[pos][y+1] 
  x=5
  s6 += matrix[x][y] * matrix[pos][y+1] 
  x=6
  s7 += matrix[x][y] * matrix[pos][y+1] 
  x=7
  s8 += matrix[x][y] * matrix[pos][y+1] 

x = 0
pos = x+1
for y in range (7,0,-1):
  if x > 7:
    pos = 0
  d1 += matrix[x][y] * matrix[pos][y-1] 
  x=1
  d2 += matrix[x][y] * matrix[pos][y-1] 
  x=2
  d3 += matrix[x][y] * matrix[pos][y-1]
  x=3
  d4 += matrix[x][y] * matrix[pos][y-1] 
  x=4
  d5 += matrix[x][y] * matrix[pos][y-1] 
  x=5
  d6 += matrix[x][y] * matrix[pos][y-1] 
  x=6
  d7 += matrix[x][y] * matrix[pos][y-1] 
  x=7
  d8 += matrix[x][y] * matrix[pos][y-1] 
     


det = (s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8) - (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8)

resultado = det%2

if resultado == 0:

  print('\n')
  for i in matrix:
    print(i)
  print(f"\nDeterminante: {det}\nsua prova sera a prova 1\n\n") #P2-AP2-1

elif resultado == 1:

  print('\n')
  for i in matrix:
    print(i)
  print(f"\nDeterminante: {det}\nsua prova sera a prova 2\n\n") #P2-AP2-2