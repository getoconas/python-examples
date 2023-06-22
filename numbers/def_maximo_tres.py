# Definir una función que tome tres números como argumentos y devuelva el mayor de ellos.

def maximo(numero1, numero2):
  if (numero1 > numero2):
    return numero1
  else:
    return numero2

print(maximo(11, maximo(2, 3)))
print(maximo(5, maximo(33, 2)))
print(maximo(3, maximo(2, 44)))
print(maximo(1, maximo(1, 1)))
print(maximo(2, maximo(2, 1)))
print(maximo(1, maximo(2, 2)))
print(maximo(2, maximo(1, 2)))
