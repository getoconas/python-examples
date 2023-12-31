# tablas.py

# Modifica tu programa para que imprima una tabla mostrando el mes,
# el total pagado hasta el momento y el saldo restante

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
total_mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000.0

while saldo > 0:

  if (total_mes >= pago_extra_mes_comienzo and total_mes <= pago_extra_mes_fin) :
    saldo = saldo * (1 + tasa / 12) - pago_mensual - pago_extra
    total_pagado = total_pagado + pago_mensual + pago_extra
  else:
    saldo = saldo * (1 + tasa / 12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
  
  total_mes += 1

  print(total_mes, ' ', round(total_pagado, 2), ' ', round(saldo, 2))

print('Total pagado: ', round(total_pagado, 2))
print('Meses: ', total_mes)