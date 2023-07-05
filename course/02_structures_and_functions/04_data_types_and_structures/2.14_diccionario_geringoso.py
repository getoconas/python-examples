# geringoso.py

# Construí una función que, a partir de una lista de palabras
# devuelva un diccionario geringoso

# Las claves del diccionario deben ser las palabras de la lista
# y los valores deben ser sus traducciones al geringoso

def geringoso(lista):

  s = { }

  for l in lista:
    cadena = l
    cadena_geringoso = ''

    for c in cadena:
      if c == 'a':
        cadena_geringoso = cadena_geringoso + c + 'pa'
      elif c == 'e':
        cadena_geringoso = cadena_geringoso + c + 'pe'
      elif c == 'i':
        cadena_geringoso = cadena_geringoso + c + 'pi'
      elif c == 'o':
        cadena_geringoso = cadena_geringoso + c + 'po'
      elif c == 'u':
        cadena_geringoso = cadena_geringoso + c + 'pu'
      else:
        cadena_geringoso = cadena_geringoso + c

    s[cadena] = cadena_geringoso
  
  return s

diccionario = geringoso(['banana', 'manzana', 'mandarina'])

print(diccionario)
