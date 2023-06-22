# Escribir una función multip() que multiplique todos los números de una lista

def multip(lista):
  mul = 1

  for num in lista:
    mul = num * mul

  return mul

print(multip([2,3,4]))
print(multip([6,2]))