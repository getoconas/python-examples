# Definir una función que tome como argumento dos números y devuelva el mayor de ellos

def maximo(numero1, numero2):
  if (numero1 > numero2):
    return numero1
  else:
    return numero2

print(maximo(1, 2))
print(maximo(5, 3))
print(maximo(3, 3))