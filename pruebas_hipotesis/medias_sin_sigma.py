import numpy as np
from scipy.stats import norm, t, chi2, f

# Generar numeros aleatorios con distribucion normal
x = np.random.normal(size = 100)

print('-----------------------------------------------------')
print('\033[96mPrueba de hipotesis para medias con sigma desconocida\033[0m')
print('-----------------------------------------------------')

# Obtener parametros
alfa = 0.05
n = len(x)
m = x.mean()
s = x.std(ddof = 1)
print(f'alfa: {alfa}\nn: {n}\tmedia: {round(m, 2)}\tdesv m: {round(s, 2)}\n')

# Plantear la hipotesis
m0 = int(round(m, 0))
print('Hipotesis\033[33m')
print(f'H0: \u03BC = {m0}\tH0: \u03BC = {m0}\tH0: \u03BC = {m0}')
print(f'H1: \u03BC < {m0}\tH1: \u03BC != {m0}\tH1: \u03BC > {m0}')
print(f'\033[0m')

# Sacar estadistico de prueba
# con la distribucion T-Student
# T calculada = media - media propuesta / (desv / raiz de n)
t_calc = (m - m0) / (s / np.sqrt(n))
print(f'T calculada: {round(t_calc, 4)}')

# Sacar T critica
t_crit_i = t.ppf(alfa, (n - 1))
t_crit_m = abs(t.ppf(alfa / 2, (n - 1)))
t_crit_d = t.ppf(1 - alfa, (n - 1))
print(
	f'T criticas\n'
	f'izq: {round(t_crit_i, 4)}\t'
	f'medio: {round(t_crit_m, 4)}\t'
	f'der: {round(t_crit_d, 4)}\n'
)

# H0 se rechaza si
h0_i = 'H0 rechazada' if t_calc <= t_crit_i else 'H0 NO rechazada'
h0_m = 'H0 rechazada' if abs(t_calc) >= t_crit_m else 'H0 NO rechazada'
h0_d = 'H0 rechazada' if t_calc >= t_crit_d else 'H0 NO rechazada'
print(f'\033[92m{h0_i}\t{h0_m}\t{h0_d}\033[0m\n')

# Sacar P valores
p_valor_i = t.cdf(t_calc, df = n - 1)
p_valor_m = t.sf(abs(t_calc), df = n - 1) * 2
p_valor_d = 1 - t.cdf(t_calc, df = n - 1)
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
# limites = media +- t critica de enmedio * (desv / raiz de n)
lic = m - t_crit_m * (s / np.sqrt(n))
lsc = m + t_crit_m * (s / np.sqrt(n))
print(f'\033[92mP({round(lic, 4)} <= \u03BC <= {round(lsc, 4)}) = {(1 - alfa)}\033[0m')

del alfa, n, m, m0, s, t_calc, t_crit_i, t_crit_m, t_crit_d, h0_i, h0_m, h0_d, p_valor_i, p_valor_m, p_valor_d, lic, lsc
