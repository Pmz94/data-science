import funciones
from fitter import Fitter, get_common_distributions
import numpy as np
import scipy.stats as st

# se observa y se anotan los tiempos en segundos en los que tarda un programa en ejecutarse
# la distribucion normal seria la mas apropiada para estos tiempos?
tiempos = [
	(2.10, 16),
	(2.11, 28),
	(2.12, 41),
	(2.13, 74),
	(2.14, 149),
	(2.15, 256),
	(2.16, 137),
	(2.17, 82),
	(2.18, 40),
	(2.19, 19),
	(2.20, 11),
]
tiempos = funciones.desagrupar_datos(tiempos)

resumen = funciones.estadistica_descriptiva(tiempos)
print(f"n: {resumen['n']}\tmin: {resumen['minimo']}\tmax: {resumen['maximo']}\trango: {resumen['rango']}")
print(f"media: {round(resumen['media'], 2)}\tmediana: {resumen['mediana']}\tmoda: {resumen['moda']}")
print(f"varianza: {round(resumen['varianza'], 4)}\tdesviacion: {round(resumen['desv'], 4)}")
print(f"sesgo: {round(resumen['sesgo'], 4)}\tcurtosis: {round(resumen['curtosis'], 4)}")

print('Mostrando histograma')
funciones.histograma(
	tiempos,
	titulo = 'Segundos en los que tarda en correr un programa',
	label_x = 'Segundos'
)

li = min(tiempos) - 0.005
ls = max(tiempos) + 0.005
l = np.arange(li, ls, 0.010)
print(l)

clases = 11
intervalo = []
for i in range(1, 12):
	val = st.norm.ppf(i / clases, resumen['media'], resumen['desv'])
	intervalo.append(val)
intervalo.insert(0, -np.inf)
print(intervalo)


"""
x2c = []
for x in sorted(tiempos):
	# frecuencia observada
	oi = tiempos.count(x)
	# normalizar los datos
	z = (x - resumen['media']) / resumen['desv']
	# probabilidad de z
	p = norm.cdf(z)
	# frecuencia esperada
	ei = p * resumen['n']
	# x2 calculada
	x2c.append((oi-ei) ** 2 / ei)
x2c = sum(x2c)

print('Ajustando datos a distribuciones')
f = Fitter(tiempos, distributions = get_common_distributions())
f.fit()
print(f.summary())
f.plot_pdf()

best = f.get_best(method = 'sumsquare_error')
best_name = list(best.keys())[0]
print('Distribucion mejor ajustada:', best_name)
print(f.fitted_param[best_name])
"""
