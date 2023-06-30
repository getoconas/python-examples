# buscar_precios.py

# Escribir una función `buscar_precio(fruta)` que busque
# en archivo `precios.csv` el precio de determinada fruta
# (o verdura) y lo imprima en pantalla
# Si la fruta no figura en el listado de precios
# debe imprimir un mensaje que lo indique

def buscar_precio(fruta):

  f = open('precios.csv', 'rt')

  precio = ''
  existeFruta = False
  noExisteFruta = False

  for line in f:
    row = line.split(',')

    if (row[0] == fruta) :
      existeFruta = True
      precio = row[1]
    else :
      noExisteFruta = True

  if (existeFruta):
    print("El precio de un cajon de ", fruta," es: ", precio)

  if (noExisteFruta and not existeFruta) :
    print(fruta, " no figura en el listado de precios")

  f.close()

  return 0

buscar_precio('Frambuesa')
buscar_precio('Kale')