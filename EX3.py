'''

Inserction Sort


3) Faça uma comparação entre essa nova versão do algoritmo de inserção com a versão sem 
a busca binária em termos da quantidade de comparações  e trocas efetuadas.
'''

import random
compa = 0

def binarySearch(lista, val, começo, fim):

    global compa

    if começo == fim:
        if lista[começo] > val:
            return começo
        else:
            return começo+1
 
    if começo > fim:
        return começo
 
    meio = (começo+fim)//2
    if lista[meio] < val:
        compa += 1
        return binarySearch(lista, val, meio+1, fim)
    elif lista[meio] > val:
        compa += 2
        return binarySearch(lista, val, começo, meio-1)
    else:
        compa += 3
        return meio

lista = [] 
for n in range(1000):
  lista.append(random.randint(0,1000))

def contadorInserctionSort(lista):
    trocas = 0
    comparacoes = 0
    for f in range(len(lista)):
        val = lista[f]
        i = f
        comparacoes += 1
        while i > 0 and val < lista[i-1]:
            lista[i] = lista[i-1]
            i -= 1
            comparacoes += 1
            trocas += 1
        lista[i] = val
    print(f"\nInserctionSort em 1000 itens aleatórios\n\nTrocas: {trocas} \nComparações: {comparacoes}")

contadorInserctionSort(lista)
   
trocas = 0

def contadorBinaryInserction(lista):
    
    global trocas
    global compa

    for i in range(0, len(lista)):
        val = lista[i]
        compa += 1
        # Inserindo a função de busca binária dentro do ordenador por inserção
        j = binarySearch(lista, val, 0, i-1)
        lista = lista[:j] + [val] + lista[j:i] + lista[i+1:]
        trocas += 1
    return lista

contadorBinaryInserction(lista)
print(f"\n\nInserctionSort binário em 1000 itens aleatórios\n\nTrocas: {trocas} \nComparações: {compa}")


