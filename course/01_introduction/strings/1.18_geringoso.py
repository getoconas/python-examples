# geringoso.py

# Usá una iteración sobre el string cadena para agregar la sílaba 
# 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal

cadena = 'Geringoso'
capadepenapa = ''

for c in cadena:
  if c == 'a':
    capadepenapa = capadepenapa + c + 'pa'
  elif c == 'e':
    capadepenapa = capadepenapa + c + 'pe'
  elif c == 'i':
    capadepenapa = capadepenapa + c + 'pi'
  elif c == 'o':
    capadepenapa = capadepenapa + c + 'po'
  elif c == 'u':
    capadepenapa = capadepenapa + c + 'pu'
  else:
    capadepenapa = capadepenapa + c

print(capadepenapa)
