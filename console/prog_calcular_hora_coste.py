# Escribir un programa que pregunte al usuario por el número de horas trabajadas
# y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde

horas = float(input('¿Cuantas horas trabajo?: '))
coste_hora = float(input('¿Cual es el coste por hora?: '))

print('El trabajo a cobrar es por $', horas * coste_hora)