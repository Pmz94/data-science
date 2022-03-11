import numpy as np
from scipy.stats import norm, t, chi2, f

# Generar numeros aleatorios con distribucion normal
x = np.random.normal(size = 100)

print('\033[96mPrueba de hipotesis para varianzas\033[0m')

# Obtener parametros
alfa = 0.05
n = len(x)
s = x.std(ddof = 1)
s2 = s ** 2
print(f'alfa: {alfa}\tn: {n}\tdesv muestral: {round(s, 2)}\tvar muestral: {round(s2, 2)}\n')

# Plantear la hipotesis
v20 = int(round(s, 0))
print('Hipotesis\033[33m')
print(f'H0: v^2 = {v20}\tH0: v^2 = {v20}\tH0: v^2 = {v20}')
print(f'H1: v^2 < {v20}\tH1: v^2 != {v20}\tH1: v^2 > {v20}')
print(f'\033[0m')

# Sacar estadistico de prueba
# con la distribucion X^2
# X2 calculada = (n - 1) * varianza muestral / varianza supuesta
x2_calc = (n - 1) * s2 / v20
print(f'X^2 calculada: {round(x2_calc, 4)}')

# Sacar X2 critica
x2_crit_i = chi2.ppf(alfa, (n - 1))
x2_crit_m1 = abs(chi2.ppf(alfa / 2, (n - 1)))
x2_crit_m2 = abs(chi2.ppf(1 - (alfa / 2), (n - 1)))
x2_crit_d = chi2.ppf(1 - alfa, (n - 1))
print(
	f'X^2 criticas\n'
	f'izq: {round(x2_crit_i, 4)}\t'
	f'medio: {round(x2_crit_m1, 4)} o {round(x2_crit_m2, 4)}\t'
	f'der: {round(x2_crit_d, 4)}\n'
)

# H0 se rechaza si
h0_i = 'H0 rechazada' if x2_calc <= x2_crit_i else 'H0 NO rechazada'
h0_m = 'H0 rechazada' if x2_calc >= x2_crit_m1 or x2_calc <= x2_crit_m2 else 'H0 NO rechazada'
h0_d = 'H0 rechazada' if x2_calc >= x2_crit_d else 'H0 NO rechazada'
print(f'\033[92m{h0_i}\t{h0_m}\t{h0_d}\033[0m\n')

# Sacar P valores
p_valor_i = chi2.cdf(x2_calc, df = n - 1)
p_valor_m1 = 1 - chi2.sf(abs(x2_calc), df = n - 1)
p_valor_m2 = chi2.sf(abs(x2_calc), df = n - 1)
p_valor_d = 1 - chi2.cdf(x2_calc, df = n - 1)
print(
	f'\033[94m'
	f'P-valores\n'
	f'izq: {round(p_valor_i, 4)}\t'
	f'medio: {round(p_valor_m1, 4)} o {round(p_valor_m2, 4)}\t'
	f'der: {round(p_valor_d, 4)}\n'
	f'\033[0m'
)

# Intervalo de confianza para medias con sigma desconocida

# Calcular limites de confianza
# ((n - 1) * s^2) / (X2 1-alfa/2,gl) <= varianza <= ((n - 1) * s^2) / (X2 alfa/2,gl)
lic = ((n - 1) * s2) / x2_crit_m2
lsc = ((n - 1) * s2) / x2_crit_m1

print('Intervalo de confianza')
print(f'\033[92mP({round(lic, 4)} <= v^2 <= {round(lsc, 4)}) = {(1 - alfa)}\033[0m\n')

del alfa, n, s, s2, v20, x2_calc, x2_crit_i, x2_crit_m1, x2_crit_m2, x2_crit_d, h0_i, h0_m, h0_d, p_valor_i, p_valor_m1, p_valor_m2, p_valor_d, lic, lsc
