# Implementa el algoritmo de Bubble Sort para ordenar una lista de números de menor a mayor.

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
             
lista_ordenada = bubble_sort([8, 6, 1, 4, 9, 2, 5, 7, 3])
print(lista_ordenada)