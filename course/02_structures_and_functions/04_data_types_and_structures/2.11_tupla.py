# tupla.py

import csv

f = open('../04_data_types_and_structures/camion.csv')
filas = csv.reader(f)
next(filas)

fila = next(filas)
print(fila)

t = (fila[0], int(fila[1]), float(fila[2]))
print(t)

cost = t[1] * t[2]
print(f'{cost:0.2f}')

nombre, cajones, precio = t
print(nombre, cajones, precio)
