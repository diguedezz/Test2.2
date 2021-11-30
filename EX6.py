'''

QuickSort


6) Mostre as etapas de execução do QuickSort para ordenar o array: Q U I C K S O R T, considere como elemento do meio, v[(esq+dir)/2]

'''

def quickSort(lista, esq, dir):
    
    if esq >= dir: 
        return lista 

    i = esq 
    j = dir
    pivo = lista[(esq+dir)//2]

    print(lista,'\n')
    
    while i <= j:
        while lista[i] < pivo: 
            i += 1
        while lista[j] > pivo: 
            j -= 1
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
            print(f'Trocando {lista[i]} por {lista[j]}\n')
            i = i + 1
            j = j - 1
            
    quickSort(lista, esq, j)
    quickSort(lista, i, dir)

lista2 = ['Q','U','I','C','K','S','O','R','T']
print('\n\nComeço da lista:\n')
quickSort(lista2,0,len(lista2)-1)