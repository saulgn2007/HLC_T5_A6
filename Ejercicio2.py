# Crea una función que genere una contraseña aleatoria de longitud especificada, incluyendo 
# letras, números y caracteres especiales.

import random

def Contraseña(longitud):
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    caracteres_especiales = '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
    caracteres = letras + numeros + caracteres_especiales
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

print(Contraseña(random.randint(1, 10)))