# adelantos.py

# Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
# Modifica el programa para incorporar estos pagos extra y que imprima el monto total
# pagado junto con la cantidad de meses requeridos

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto = 1000.0
total_mes = 0
mes = 0

while saldo > 0:

  if (mes < 12):
    saldo = saldo * (1 + tasa / 12) - pago_mensual - adelanto
    total_pagado = total_pagado + pago_mensual + adelanto
    mes += 1
  else:
    saldo = saldo * (1 + tasa / 12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
  
  total_mes += 1

print('Total pagado', round(total_pagado, 2), ' en ', total_mes, ' meses')