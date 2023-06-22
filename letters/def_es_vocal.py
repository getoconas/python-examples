# Escribir una función que tome un carácter y devuelva True si es una vocal,
# de lo contrario devuelve False

def es_vocal(letra):
  if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    return True
  return False

print(es_vocal('a'))
print(es_vocal('o'))
print(es_vocal('t'))