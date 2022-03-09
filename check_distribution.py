import funciones
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
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
desv_m = funciones.desv_m(tiempos)
error_tipico = desv_m / (n ** 0.5)
sturges = int(round(1 + 3.322 * log(len(tiempos), 10), 0))

# funciones.crappyhist(tiempos)

plt.hist(
	tiempos,
	density = False,
	bins = sturges,
	label = 'Segundos'
)
mn, mx = plt.xlim()
plt.xlim(mn, mx)
kde_xs = np.linspace(mn, mx)
kde = st.gaussian_kde(tiempos)
plt.plot(kde_xs, kde.pdf(kde_xs), label = 'Tendencia')
plt.legend(loc = 'upper left')
plt.xlabel('Segundos')
plt.ylabel('Freq')
plt.title('Segundos en los que tarda en correr un programa')
plt.show()

# normalizar los datos
z = []
for x in tiempos:
	z.append((x - media)/desv_m)

f = Fitter(z, distributions = get_common_distributions())
f.fit()
print(f.summary())

best = f.get_best(method = 'sumsquare_error')
print(best)
best_name = list(best.keys())[0]
print(f.fitted_param[best_name])

# data = np.random.normal(0, 0.1, 10000)