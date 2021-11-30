'''

Quick Sort


5) Mostre como o vetor A B A B A B A é particionado quando se escolhe o elemento do meio, v[(esq+dir)/2] como pivô
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


#Acrescentamos números aos elementos do array para faciitar a verificação da ordenação
#Porém funciona perfeitamente sem os números, para caso de teste iremos comentar o array sem os números:

#lista1 = ['A','B','A','B','A','B','A']
lista1 = ['A3','B2','A1','B1','A4','B3','A2']
print('\n\nComeço da lista:\n')
quickSort(lista1,0,len(lista1)-1)



