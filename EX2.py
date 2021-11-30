'''

Inserction Sort


2) Altere o algoritmo de ordenação por inserção para que ele utilize a busca binária para encontrar 
a posição de inserção de um elemento no vetor destino. 
'''



import random

#primeiro inserimos a função de busca binária 
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

lista = [] 
for n in range(100):
  lista.append(random.randint(0,100))


print('\n\nLista Ordenada por InserctionSort com busca binária:\n\n',binaryInserctionSortSearch(lista),'\n\n\n')
