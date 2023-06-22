# Definir una función invertir_cadena() que calcule la inversión de una cadena

def invertir_cadena(cadena):
  cadena_invertida = ""

  for x in cadena:
    cadena_invertida = x + cadena_invertida

  return cadena_invertida

print(invertir_cadena("hola"))
print(invertir_cadena("probando cadena"))