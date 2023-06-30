# preliminares.py

# Tratá de leer el archivo entero de una en una larga cadena:

with open('camion.csv') as f:
  data = f.read()

print(data)

with open('camion.csv', 'rt') as f:
  for line in f:
    print(line, end = '')