import random as rm
import numpy as np
import funciones

tiempos = []
for i in range(0, 853):
	x = round(rm.uniform(2.1, 2.2), 2)
	tiempos.append(x)

n = len(tiempos)
x = np.mean(tiempos)
dv = np.std(tiempos)
minimo = min(tiempos)
maximo = max(tiempos)

print('n:', n)
print('x:', x)
print('dv:', dv)
print('min:', minimo)
print('max:', maximo)
print(funciones.freq_table2(tiempos))