# Escribir una función sum() que sume todos los números de una lista

def sum(lista):
  suma = 0

  for num in lista:
    suma = num + suma

  return suma

print(sum([1,3,4,5]))
print(sum([10,2,3,99,4,5]))
