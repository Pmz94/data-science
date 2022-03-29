import math
import random as rm
import numpy as np
import pandas as pd

def rm_uniforme(a, b, r = rm.random()):
	return round(a + r * (b - a), 2)

def rm_bernoulli(p, r = rm.random()):
	return 1 if r >= p else 0

def rm_poisson(lamb, r = rm.random()):
	t = 0  # initialize sum of exponential variables as zero
	n = -1  # initialize counting variable as negative one
	while t < 1:
		e = -(1 / lamb) * np.log(r)  # generate exponential random variable
		t = t + e  # update sum of exponential variables
		n = n + 1  # update number of exponential variables
	nn = n
	return nn

def rm_normal(m = 0, d = 1):
	return round(m + d * (sum([rm.random() for _ in range(12)]) - 6), 2)

def rm_exponencial(uno_sobre_lambda, r = rm.random()):
	return round(-uno_sobre_lambda * math.log(1 - r), 2)

def rm_weibull(d, b, r = rm.random()):
	return round(1 / d * (-math.log(1 - r)) ** (1 / b), 2)

numeros = []
for i in range(50):
	ra = rm.random()
	numeros.append({
		'uniforme': rm_uniforme(10, 100, ra),
		'bernoulli': rm_bernoulli(0.6, ra),
		'poisson': rm_poisson(8, ra),
		'normal': rm_normal(0, 1),
		'exponencial': rm_exponencial(6, ra),
		'weibull': rm_weibull(1, 5, ra)
	})
print(pd.DataFrame(numeros))
