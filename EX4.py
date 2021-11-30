'''

Inserction Sort


4) Faça um comparativo calculando o tempo de execução de cada versão do algoritmo de ordenação 
por inserção para Array ordenado, aleatório, ordem inversa.
'''

#Inserindo um InserctionSort básico

import time
import random

def binarySearch(lista, val, começo, fim):

    if começo == fim:
        if lista[começo] > val:
            return começo
        else:
            return começo+1
 
    if começo > fim:
        return começo
 
    meio = (começo+fim)//2
    if lista[meio] < val:
        return binarySearch(lista, val, meio+1, fim)
    elif lista[meio] > val:
        return binarySearch(lista, val, começo, meio-1)
    else:
        return meio



def binaryInserctionSortSearch(lista):

    for i in range(1, len(lista)):
        val = lista[i]
        # Inserindo a função de busca binária dentro do ordenador por inserção
        j = binarySearch(lista, val, 0, i-1)
        lista = lista[:j] + [val] + lista[j:i] + lista[i+1:]
    return lista



def inserctionSort(lista):

    for i in range(1, len(lista)):
        val = lista[i]
 
        j = i-1
        while j >= 0 and val < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = val


#inserindo a lista aleatoria
listaAleatoria = [] 
for n in range(1000):
  listaAleatoria.append(random.randint(0,1000))

#inserindo a lista ordenada
listaOrdenada = []
for n in range(0,2000,2):
    listaOrdenada.append(n)
#inserindo a lista de ordem inversa
listaInversa = []
for n in range(2000,0,-2):
    listaInversa.append(n)


print('\n\nTESTES FEITOS COM LISTAS DE 1000 ITENS\n\n')
inicio = time.time()
binaryInserctionSortSearch(listaAleatoria)
print('Tempo para lista aleatoria por binaryInserctionSort:\n',time.time() - inicio,'segundos')
inicio = time.time()
inserctionSort(listaAleatoria)
print('Tempo para lista aleatoria por InserctionSort:\n',time.time() - inicio,'segundos\n\n')

inicio = time.time()
binaryInserctionSortSearch(listaOrdenada)
print('Tempo para lista ordenada por binaryInserctionSort:\n',time.time() - inicio,'segundos')
inicio = time.time()
inserctionSort(listaOrdenada)
print('Tempo para lista ordenada por InserctionSort:\n',time.time() - inicio,'segundos\n\n')

inicio = time.time()
binaryInserctionSortSearch(listaInversa)
print('Tempo para lista de ordem inversa por binaryInserctionSort:\n',time.time() - inicio,'segundos')
inicio = time.time()
inserctionSort(listaInversa)
print('Tempo para lista de ordem inversa por InserctionSort:\n',time.time() - inicio,'segundos\n\n')