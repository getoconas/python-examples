# costo_camion.py

# Transformá el programa `costo_camion.py`
# en una función `costo_camion(nombre_archivo)`

def costo_camion(nombre_archivo) :

  f = open(nombre_archivo, 'rt')
  
  headers = next(f)

  total = 0.0

  for line in f:
    row = line.split(',')
    total = total + float(row[2]) * int(row[1])

  f.close()

  return total

costo = costo_camion('camion.csv')
print('Costo total: ', costo)
