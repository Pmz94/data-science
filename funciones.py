import numpy as np
import scipy.stats as st
from typing import List
import matplotlib.pyplot as plt
from math import log

# agrupar datos en tabla de frecuencias
def agrupar_datos(lista: list) -> List[tuple]:
	"""
	Crea una lista con las frecuencuas de cada dato de `lista`.
	
	`lista` debe tener la estructura de:
	lista = [(dato_1, frecuencia_1), (dato_2, frecuencia_2), ... (dato_i, frecuencia_i)]
	"""
	hist = {}
	for i in lista:
		hist[i] = hist.get(i, 0) + 1
	dict_items = hist.items()
	freq = sorted(dict_items)
	return freq

# desagrupar datos
def desagrupar_datos(lista: List[tuple]) -> list:
	datos_desagrupados = []
	for tupla in lista:
		for i in range(tupla[1]):
			datos_desagrupados.append(tupla[0])
	return datos_desagrupados

def unique(list):
	"""Obtener los valores unicos de una lista"""
	# initialize a null list
	unique_list = []
	# traverse for all elements
	for x in list:
		# check if exists in unique_list or not
		if x not in unique_list:
			unique_list.append(x)
	return unique_list

def histograma(
		data: list,
		cols = 0,
		titulo = 'Histograma',
		label_x = '',
		label_y = 'Freq',
		linea = False
):
	if cols <= 0:
		cols = int(round(1 + 3.322 * log(len(data), 10), 0))

	plt.hist(
		data,
		bins = cols,
		density = False,
		label = label_x if label_x else None
	)

	if linea:
		mn, mx = plt.xlim()
		plt.xlim(mn, mx)
		kde_xs = np.linspace(mn, mx)
		kde = st.gaussian_kde(data)
		plt.plot(kde_xs, kde.pdf(kde_xs), label = 'Tendencia')
		plt.legend(loc = 'upper left')

	if titulo: plt.title(titulo)
	if label_x: plt.xlabel(label_x)
	if label_y: plt.ylabel(label_y)
	plt.show()

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
