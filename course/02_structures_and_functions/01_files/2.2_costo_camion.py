# costo_camion.py

# Escribí un programa llamado costo_camion.py que abra
# el archivo, lea las líneas, y calcule el precio pagado
# por los cajones cargados en el camión.

f = open('camion.csv', 'rt')

headers = next(f)

total = 0.0

for line in f:
  row = line.split(',')
  total = total + float(row[2]) * int(row[1])

print('Costo total ', total)

f.close()