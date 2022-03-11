import numpy as np
from scipy.stats import norm, t, chi2, f

# Generar numeros aleatorios con distribucion normal
x = np.random.normal(size = 100)

print('--------------------------------------------------')
print('\033[96mPrueba de hipotesis para medias con sigma conocida\033[0m')
print('--------------------------------------------------')

# Obtener parametros
alfa = 0.05
n = len(x)
m = x.mean()
v = x.std()
print(f'alfa: {alfa}\nn: {n}\tmedia: {round(m, 2)}\tdesv p: {round(v, 2)}\n')

# Plantear la hipotesis
m0 = int(round(m, 0))
print('Hipotesis\033[33m')
print(f'H0: m = {m0}\tH0: m = {m0}\tH0: m = {m0}')
print(f'H1: m < {m0}\tH1: m != {m0}\tH1: m > {m0}')
print(f'\033[0m')

# Sacar estadistico de prueba
# con la distribucion normal estandar
# Z calculada = media - media propuesta / (desv / raiz de n)
z_calc = (m - m0) / (v / np.sqrt(n))
print(f'Z calculada: {round(z_calc, 4)}')

# Sacar Z critica
# La funcion que saca la distribucion inversa acumulada is ppf
# Se aplica valor absoluto porque la distribucion acumulada
# trabaja con el lado izquierdo, entonces saldria negativo
z_crit_i = norm.ppf(alfa)
z_crit_m = abs(norm.ppf(alfa / 2))
z_crit_d = norm.ppf(1 - alfa)
print(
	f'Z criticas\n'
	f'izq: {round(z_crit_i, 4)}\t'
	f'medio: {round(z_crit_m, 4)}\t'
	f'der: {round(z_crit_d, 4)}\n'
)

# H0 se rechaza si
h0_i = 'H0 rechazada' if z_calc <= z_crit_i else 'H0 NO rechazada'
h0_m = 'H0 rechazada' if abs(z_calc) >= z_crit_m else 'H0 NO rechazada'
h0_d = 'H0 rechazada' if z_calc >= z_crit_d else 'H0 NO rechazada'
print(f'\033[92m{h0_i}\t{h0_m}\t{h0_d}\033[0m\n')

# Sacar P valores
p_valor_i = norm.cdf(z_calc)
p_valor_m = norm.sf(abs(z_calc)) * 2
p_valor_d = 1 - norm.cdf(z_calc)
print(
	f'\033[94m'
	f'P-valores\n'
	f'izq: {round(p_valor_i, 4)}\t'
	f'medio: {round(p_valor_m, 4)}\t'
	f'der: {round(p_valor_d, 4)}\n'
	f'\033[0m'
)

# Los intervalos de confianza ofrecen una vision muy util
# Proporcionan un margen de error muy preciso
# y si se usan correctamente, pueden ayudarnos a extraer
# la mayor cantidad de información posible de nuestros datos

print('Intervalo de confianza')
# Calcular limites de confianza
# limites = media +- z critica de enmedio * (desv / raiz de n)
lic = m - z_crit_m * (v / np.sqrt(n))
lsc = m + z_crit_m * (v / np.sqrt(n))
print(f'\033[92mP({round(lic, 4)} <= m <= {round(lsc, 4)}) = {(1 - alfa)}\033[0m')

# Sabemos que esta bien porque la distribucion normal de la muestra tiene promedio de 0
# pero como no sabemos nada de su poblacion, se puede decir que
# al 95% de confianza, existe suficiente evidencia estadistica
# que permite decir que el promedio de la poblacion esta entre -0.14 y 0.26

del alfa, n, m, m0, v, z_calc, z_crit_i, z_crit_m, z_crit_d, h0_i, h0_m, h0_d, p_valor_i, p_valor_m, p_valor_d, lic, lsc
