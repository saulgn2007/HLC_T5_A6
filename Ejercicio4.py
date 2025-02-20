# Escribe una función recursiva que reciba una cadena y devuelva True si es un palíndromo y False 
# en caso contrario. Una palabra es palíndroma si se lee igual de un lado que de otro.

def es_palindromo(cadena):

    if len(cadena) <= 1:
        return True

    if cadena[0] != cadena[-1]:
        return False

    return es_palindromo(cadena[1:-1])

print(es_palindromo('reconocer'))
print(es_palindromo('arpa'))