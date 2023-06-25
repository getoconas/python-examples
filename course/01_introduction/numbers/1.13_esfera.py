# esfera.py

# Escribí un programa que le pida al usuario que ingrese por teclado
# el radio r de una esfera y calcule e imprima el volumen de la misma
# Sugerencia: recordar que el volumen de una esfera es 4/3 πr^3

import math

radio = float(input('Ingrese el radio r de la esfera: '))

print('El volumen es de: ', 4 / 3 * math.pi * radio ** 3)
