import numpy as np
import scipy.stats as st
from scipy.stats import norm, t, chi2, f

# Generar numeros aleatorios con distribucion normal
x = np.random.normal(size = 100)

# Intervalos de confianza para medias con sigma conocida
# con la distribucion normal estandar
print('\033[96mIntervalo de confianza para medias con sigma conocida\033[0m')

alfa = 0.05
n = len(x)
m = x.mean()
m0 = 50
v = x.std()
print(f"alfa: {alfa}\tn: {n}\tmedia: {round(m, 2)}\tdesv: {round(v, 2)}\n")

# Sacar Z calculada
# z calculada = media - media propuesta / (desv / raiz de n)
z_calc = (m - m0) / (v / np.sqrt(n))

# Sacar Z critica
# La funcion que saca la distribucion inversa acumulada is ppf
# Se aplica valor absoluto porque la distribucion acumulada
# trabaja con el lado izquierdo, entonces saldria negativo
z_crit_i = norm.ppf(alfa)
z_crit_m = abs(norm.ppf(alfa / 2))
z_crit_d = norm.ppf(1 - alfa)

print('Hipotesis')
print(f'H0: m = {m0}\tH0: m = {m0}\tH0: m = {m0}')
print(f'H1: m < {m0}\tH1: m != {m0}\tH1: m > {m0}\n')

print(f'Z calculada: {round(z_calc, 4)}')
print(
	f'Z criticas\n'
	f'izq: {round(z_crit_i, 4)} medio: {round(z_crit_m, 4)} der: {round(z_crit_d, 4)}\n'
)

# H0 se rechaza si
h0_i = 'H0 rechazada' if z_calc <= z_crit_i else 'H0 NO rechazada'
h0_m = 'H0 rechazada' if abs(z_calc) >= z_crit_m else 'H0 NO rechazada'
h0_d = 'H0 rechazada' if z_calc >= z_crit_d else 'H0 NO rechazada'

print(f'{h0_i}\t{h0_m}\t{h0_d}\n')

print(
	f'\033[94m'
	f"P-valores\n"
	f"izq: {round(norm.cdf(z_calc), 4)} medio {round(norm.sf(abs(z_calc)) * 2, 4)} der: {round(1 - norm.cdf(z_calc), 4)}\n"
	f'\033[0m'
)

# Los intervalos de confianza ofrecen una vision muy util
# Proporcionan un margen de error muy preciso
# y si se usan correctamente, pueden ayudarnos a extraer
# la mayor cantidad de información posible de nuestros datos

# Calcular limites de confianza
# limites = media +- z critica * (desv / raiz de n)
lic = m - z_crit_m * (v / np.sqrt(n))
lsc = m + z_crit_m * (v / np.sqrt(n))

print('Intervalo de confianza')
print(f"P({round(lic, 4)} <= m <= {round(lsc, 4)}) = {(1 - alfa)}\n")

# Sabemos que esta bien porque la distribucion normal de la muestra tiene promedio de 0
# pero como no sabemos nada de la poblacion, se puede decir que
# al 95% de confianza, existe suficiente evidencia estadistica
# que permite decir que el promedio de la poblacion esta entre -0.14 and 0.26.

del alfa, n, m, m0, v, z_calc, z_crit_i, z_crit_m, z_crit_d, lic, lsc

# Intervalos de confianza para medias con sigma desconocida
# con la distribucion T-Student
print('--------------------------------------------------------')
print('\033[96mIntervalo de confianza para medias con sigma desconocida\033[0m')

alfa = 0.05
n = len(x)
m = x.mean()
m0 = 50
s = x.std(ddof = 1)
print(f"alfa: {alfa}\tn: {n}\tmedia: {round(m, 2)}\tdesv: {round(s, 2)}\n")

# Sacar T calculada
# t calculada = media - media propuesta / (desv / raiz de n)
t_calc = (m - m0) / (s / np.sqrt(n))

# Sacar T critica
t_crit_i = t.ppf(alfa, (n - 1))
t_crit_m = abs(t.ppf(alfa / 2, (n - 1)))
t_crit_d = t.ppf(1 - alfa, (n - 1))

print('Hipotesis')
print(f'H0: m = {m0}\tH0: m = {m0}\tH0: m = {m0}')
print(f'H1: m < {m0}\tH1: m != {m0}\tH1: m > {m0}\n')

print(f'T calculada: {round(t_calc, 4)}')
print(
	f'T criticas\n'
	f'izq: {round(t_crit_i, 4)} medio: {round(t_crit_m, 4)} der: {round(t_crit_d, 4)}\n'
)

# H0 se rechaza si
h0_i = 'H0 rechazada' if t_calc <= t_crit_i else 'H0 NO rechazada'
h0_m = 'H0 rechazada' if abs(t_calc) >= t_crit_m else 'H0 NO rechazada'
h0_d = 'H0 rechazada' if t_calc >= t_crit_d else 'H0 NO rechazada'

print(f'{h0_i}\t{h0_m}\t{h0_d}\n')

print(
	f'\033[94m'
	f"P-valores\n"
	f"izq: {round(t.cdf(t_calc, df = n - 1), 4)} medio {round(t.sf(abs(t_calc), df = n - 1) * 2, 4)} der: {round(1 - t.cdf(t_calc, df = n - 1), 4)}\n"
	f'\033[0m'
)

# Calcular limites de confianza
# limites = media +- t critica * (desv / raiz de n)
lic = m - t_crit_m * (s / np.sqrt(n))
lsc = m + t_crit_m * (s / np.sqrt(n))

print('Intervalo de confianza')
print(f"P({round(lic, 4)} <= m <= {round(lsc, 4)}) = {(1 - alfa)}\n")

del alfa, n, m, m0, s, t_calc, t_crit_i, t_crit_m, t_crit_d, lic, lsc
