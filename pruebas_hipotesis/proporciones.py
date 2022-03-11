import numpy as np
from scipy.stats import norm, t, chi2, f

# Generar numeros aleatorios con distribucion binomial
r = np.random.binomial(10, 0.5, 100)

print('-------------------------------------')
print('\033[96mPrueba de hipotesis para proporciones\033[0m')
print('-------------------------------------')

# Obtener parametros
alfa = 0.05
n = len(r)
x = len([i for i in r if i >= 6])
p = x / n
print(f'alfa: {alfa}\nn: {n}\tx: {round(x, 2)}\tp: {round(p, 2)}\n')

# Plantear la hipotesis
p0 = 0.5
print('Hipotesis\033[33m')
print(f'H0: P = {p0}\tH0: P = {p0}\tH0: P = {p0}')
print(f'H1: P < {p0}\tH1: P != {p0}\tH1: P > {p0}')
print(f'\033[0m')

# Sacar estadistico de prueba
# con la distribucion normal estandar
# Z calculada = media - (n * p0) / raiz(n * p0 * (1 - p0))
z_calc = (x - (n * p0)) / ((n * p0) * (1 - p0)) ** 0.5
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

print('Intervalo de confianza')
# Calcular limites de confianza
# limites = p^ +- z critica de enmedio * raiz((p^ * (1 - p^)) / n)
lic = p - z_crit_m * ((p * (1 - p)) / n) ** 0.5
lsc = p + z_crit_m * ((p * (1 - p)) / n) ** 0.5
print(f'\033[92mP({round(lic, 4)} <= P <= {round(lsc, 4)}) = {(1 - alfa)}\033[0m')

del alfa, n, x, p, p0, z_calc, z_crit_i, z_crit_m, z_crit_d, h0_i, h0_m, h0_d, p_valor_i, p_valor_m, p_valor_d, lic, lsc
