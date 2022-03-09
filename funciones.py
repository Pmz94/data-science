from typing import List
from prettytable import PrettyTable
import numpy as np
from math import log

# agrupar datos en tabla de frecuencias
def agrupar_datos(lista: list) -> List[tuple]:
	"""Tally elements from `data`."""
	hist = {}
	for i in lista:
		hist[i] = hist.get(i, 0) + 1
	dict_items = hist.items()
	freq = sorted(dict_items)
	return freq

# agrupar datos en tabla de frecuencias
def freq_table2(data: list) -> PrettyTable:
	"""Tally elements from `data`."""
	hist = {}
	for j in data:
		hist[j] = hist.get(j, 0) + 1
	dict_items = hist.items()
	freq = sorted(dict_items)
	t = PrettyTable(['x', 'freq'])
	for j in freq:
		t.add_row([j[0], j[1]])
	return t

# desagrupar datos
def desagrupar_datos(lista: List[tuple]) -> list:
	datos_desagrupados = []
	for tupla in lista:
		for i in range(tupla[1]):
			datos_desagrupados.append(tupla[0])
	return datos_desagrupados

# desviacion estandar poblacional
def desv_p(lista: list) -> float:
	n = len(lista)
	media = sum(lista) / n
	varianza = sum((x - media) ** 2 for x in lista) / n
	return varianza ** 0.5

# desviacion estandar muestral
def desv_m(lista: list) -> float:
	n = len(lista)
	media = sum(lista) / n
	varianza = sum((x - media) ** 2 for x in lista) / (n - 1)
	return varianza ** 0.5

# function to get unique values
def unique(list1):
	# initialize a null list
	unique_list = []
	# traverse for all elements
	for x in list1:
		# check if exists in unique_list or not
		if x not in unique_list:
			unique_list.append(x)
	return unique_list

def crappyhist(data: list, bins = 0, width = 140):
	if bins <= 0:
		# regla de sturges
		bins = int(round(1 + 3.322 * log(len(data), 10), 0))

	h, b = np.histogram(data, bins)

	for i in range(0, bins):
		print(
			'{:12.5f} | {:{width}s} {}'.format(
				b[i],
				'#' * int(width * h[i] / np.amax(h)),
				h[i],
				width = width
			)
		)
	print('{:12.5f} |'.format(b[bins]))
