# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cant_invertir = float(input('¿Cual es la canitdad a invertir?: '))
interes_anual = float(input('¿Cual es el interes anual?: '))
cant_anios = int(input('¿Cual es la cantidad de años a invetir?: '))

total_capital = round(cant_invertir * (interes_anual / 100 + 1) ** cant_anios, 2)

print('El capital obtenido en ', cant_anios, " año/s es de ", total_capital)