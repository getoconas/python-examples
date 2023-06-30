# precio.py

# Escribí un código que abra el archivo precios.csv
# busque el precio de la naranja y lo imprima en pantalla

f = open('precios.csv', 'rt')

for line in f:
  row = line.split(',')

  if (row[0] == '"Naranja"') :
    print("El precio de la naranja es: ", row[1])

f.close()
