import math
import random as rm
import numpy as np
from prettytable import PrettyTable

def rm_uniforme(a, b, r = rm.random()):
	return round(a + r * (b - a), 2)

def rm_bernoulli(p, r = rm.random()):
	return 1 if r >= p else 0

def rm_normal(m, d):
	return round(m + d * (sum([rm.random() for _ in range(12)]) - 6), 2)

def rm_exponencial(uno_sobre_lambda, r = rm.random()):
	return round(-uno_sobre_lambda * math.log(1 - r), 2)

def rm_weibull(d, b, r = rm.random()):
	return round(1 / d * (-math.log(1 - r)) ** (1 / b), 2)

tabla = PrettyTable(field_names = ['uniforme', 'bernoulli', 'normal', 'exponencial', 'weibull'])

for i in range(50):
	r = rm.random()
	tabla.add_row([
		rm_uniforme(10, 100, r),
		rm_bernoulli(0.6, r),
		rm_normal(0, 1),
		rm_exponencial(6, r),
		rm_weibull(1, 5, r)
	])

print(tabla.get_string())

def estadistica_descriptiva(x: list):
	n = len(x)
	media = np.mean(x)
	dv = np.std(x)
	minimo = min(x)
	maximo = max(x)
