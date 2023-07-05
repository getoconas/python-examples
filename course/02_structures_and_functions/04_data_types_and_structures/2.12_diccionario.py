# diccionario.py

import csv

f = open('../04_data_types_and_structures/camion.csv')
filas = csv.reader(f)
next(filas)

fila = next(filas)
print(fila)

d = {
  'nombre': fila[0],
  'cajones': int(fila[1]),
  'precio': float(fila[2])
}
print(d)

cost = d['cajones'] * d['precio']
print(cost)

d['fecha'] = (14, 8, 2020)
d['cuenta'] = 12345

print(d)

for k in d:
  print('k =', k)

for k in d:
  print(k, '=', d[k])

# Más elegante de trabajar con claves y valores simultaneamente
# es usar el metodo items()

items = d.items()
print(items)

for k, v in d.items():
  print(k, '=', v)
