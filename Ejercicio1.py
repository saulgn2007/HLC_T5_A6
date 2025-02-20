# Crea una función que reciba una lista de números enteros y devuelva la suma de todos los números pares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Pares(numeros):
    suma_pares = 0
    for i in numeros:
        if i % 2 == 0:
            suma_pares += i
    return suma_pares

print(Pares(numeros))