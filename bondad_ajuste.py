import funciones
from fitter import Fitter, get_common_distributions

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
resumen = funciones.estadistica_descriptiva(tiempos)

print(f"n: {resumen['n']}\tmin: {resumen['minimo']}\tmax: {resumen['maximo']}\trango: {resumen['rango']}")
print(f"media: {round(resumen['media'], 2)}\tmediana: {resumen['mediana']}\tmoda: {resumen['moda']}")
print(f"varianza: {round(resumen['varianza'], 4)}\tdesviacion: {round(resumen['desv'], 4)}")
print(f"sesgo: {round(resumen['sesgo'], 4)}\tcurtosis: {round(resumen['curtosis'], 4)}")

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
f.plot_pdf()

best = f.get_best(method = 'sumsquare_error')
best_name = list(best.keys())[0]
print('Distribucion mejor ajustada:', best_name)
print(f.fitted_param[best_name])
