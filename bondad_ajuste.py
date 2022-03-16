import funciones
import numpy as np
import scipy.stats as st
from fitter import Fitter, get_common_distributions, get_distributions
from math import log

# se observa y se anotan los tiempos en segundos en los que tarda un programa en ejecutarse
# la distribucion normal seria la mas apropiada para estos tiempos?
tiempos = [
	(2.1, 16),
	(2.11, 28),
	(2.12, 41),
	(2.13, 74),
	(2.14, 149),
	(2.15, 256),
	(2.16, 137),
	(2.17, 82),
	(2.18, 40),
	(2.19, 19),
	(2.2, 11),
]
tiempos = funciones.desagrupar_datos(tiempos)

n = len(tiempos)
minimo = min(tiempos)
maximo = max(tiempos)
rango = maximo - minimo
media = sum(tiempos) / n
mediana = np.median(tiempos)
moda = (st.mode(tiempos)).mode[0]
varianza = np.var(tiempos, ddof = 1)
desv = np.std(tiempos, ddof = 1)
sesgo = st.skew(np.array(tiempos))
curtosis = st.kurtosis(tiempos)
error_tipico = desv / (n ** 0.5)
sturges = int(round(1 + 3.322 * log(n, 10), 0))

print(f"n: {n}\tmin: {minimo}\tmax: {maximo}\trango: {round(rango, 1)}")
print(f"media: {round(media, 2)}\tmediana: {mediana}\tmoda: {moda}")
print(f"varianza: {round(varianza, 4)}\tdesviacion: {round(desv, 4)}")
print(f"sesgo: {round(float(sesgo), 4)}\tcurtosis: {round(curtosis, 4)}")

"""
print('Mostrando histograma')
funciones.histograma(
	tiempos,
	sturges,
	'Segundos en los que tarda en correr un programa',
	'Segundos',
	linea = True
)
"""

# normalizar los datos
# z = [(x - media) / desv for x in tiempos]
# print(z)

print('Ajustando datos a distribuciones')
f = Fitter(tiempos, distributions = get_common_distributions())
f.fit()
print(f.summary())

best = f.get_best(method = 'sumsquare_error')
best_name = list(best.keys())[0]
print('Distribucion mejor ajustada:', best_name)
print(f.fitted_param[best_name])
