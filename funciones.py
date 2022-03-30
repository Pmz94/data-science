import datetime as dt
import math
import random as rm
import re
from itertools import groupby
from typing import List, Union
import matplotlib.pyplot as plt
import numpy as np
import prettytable as pt
import scipy.stats as st
import unicodedata


def quitar_acentos(s):
	return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def tirar_moneda(n = 1):
	lista_intentos = []  # definicion multiple
	for _ in range(n):  # haga esto n intentos
		lista_intentos.append(rm.choice(['aguila', 'sello']))
	return lista_intentos


def unique(lista):
	"""Obtener los valores unicos de una lista"""
	# initialize a null list
	unique_list = []
	# traverse for all elements
	for x in lista:
		# check if exists in unique_list or not
		if x not in unique_list:
			unique_list.append(x)
	return sorted(unique_list)


# agrupar datos en tabla de frecuencias
def agrupar_datos(lista: list) -> List[tuple]:
	"""
	Crea una lista con las frecuencuas de cada dato de `lista`.
	
	`lista` debe tener la estructura de:
	lista = [(dato_1, frecuencia_1), (dato_2, frecuencia_2), ..., (dato_i, frecuencia_i)]
	"""
	counts = {}
	for i in lista:
		counts[i] = counts.get(i, 0) + 1
	dict_items = counts.items()
	freq = sorted(dict_items)
	return freq


# desagrupar datos
def desagrupar_datos(lista: List[tuple]) -> list:
	datos_desagrupados = []
	for tupla in lista:
		for _ in range(tupla[1]):
			datos_desagrupados.append(tupla[0])
	return datos_desagrupados


def estadistica_descriptiva(x: list):
	n = len(x)
	minimo = min(x)
	maximo = max(x)
	rango = maximo - minimo
	media = np.mean(x)
	mediana = np.median(x)
	moda = st.mode(x)
	varianza = np.var(x)
	dv = np.std(x)
	q1, q2, q3 = np.quantile(x, [0.25, 0.5, 0.75])
	sesgo = st.skew(np.array(x))
	curtosis = st.kurtosis(x)
	error_tipico = dv / (n ** 0.5)
	suma = sum(x)
	sturges = round(1 + 3.322 * np.log10(n))
	alfa = 0.05
	ampl_ic = abs(st.t.ppf(alfa / 2, n - 1)) * error_tipico
	lic = media - ampl_ic
	lsc = media + ampl_ic
	return {
		'n': n,
		'minimo': minimo,
		'maximo': maximo,
		'rango': rango,
		'media': media,
		'mediana': mediana,
		'moda': moda,
		'varianza': varianza,
		'desv': dv,
		'q1': q1,
		'q2': q2,
		'q3': q3,
		'sesgo': sesgo,
		'curtosis': curtosis,
		'error_tipico': error_tipico,
		'suma': suma,
		'sturges': sturges,
		'alfa': alfa,
		'ampl_ic': ampl_ic,
		'lic': lic,
		'lsc': lsc
	}


def histograma(
	data: list,
	cols = 0,
	titulo = None,
	label_x = None,
	label_y = None,
	linea = False
):
	plt.hist(
		data,
		bins = cols if cols > 0 else 'sturges',
		density = False
	)

	if linea:
		min_lim, max_lim = plt.xlim()
		plt.xlim(min_lim, max_lim)
		kde_xs = np.linspace(min_lim, max_lim)
		kde = st.gaussian_kde(data)
		plt.plot(kde_xs, kde.pdf(kde_xs), label = 'Tendencia')
		plt.legend(loc = 'upper left')

	if titulo: plt.title(titulo)
	if label_x: plt.xlabel(label_x)
	if label_y: plt.ylabel(label_y)
	plt.show()


def diagrama_tallo_hoja(x: list):
	table = pt.PrettyTable()
	table.field_names = ['Tallo', 'Hoja', 'Freq']
	table.align['Tallo'] = 'r'
	table.align['Hoja'] = 'l'
	table.align['Freq'] = 'c'
	for tallo, g in groupby(sorted(x), key = lambda a: int(a) // 10):
		lst = map(str, [int(y) % 10 for y in list(g)])
		hoja = ' '.join(lst)
		freq = sum(c.isdigit() for c in hoja)
		table.add_row([tallo, hoja, freq])
	print(table.get_string())


def grafica_serie_tiempo(
	ejex: List[int], ejey: List[int],
	etiquetax = 'Tiempo',
	etiquetay = 'Variable',
	titulo = 'Grafica de serie de tiempo',
	ejex_enteros = False
) -> None:
	plt.plot(ejex, ejey, 'o-')
	if ejex_enteros: plt.xticks(range(math.floor(min(ejex)), math.ceil(max(ejex)) + 1))
	plt.title(titulo)
	plt.xlabel(etiquetax)
	plt.ylabel(etiquetay)
	plt.show()


def crappyhist(data: list, bins = 0, width = 140):
	if bins <= 0:
		# regla de sturges
		bins = int(round(1 + 3.322 * math.log(len(data), 10), 0))

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


def sacar_curp(nombre: str, apellido_paterno: str, apellido_materno: str, sexo: str, fecha_nac: Union[str, dt.datetime], estado_nac: str) -> str:
	if isinstance(fecha_nac, str):
		fecha_nac = dt.datetime.strptime(fecha_nac, '%Y-%m-%d')
	nombre = quitar_acentos(nombre)
	apellido_paterno = quitar_acentos(apellido_paterno)
	apellido_materno = quitar_acentos(apellido_materno)
	estado_nac = quitar_acentos(estado_nac)
	# Primera letra y vocal del primer apellido
	curp = apellido_paterno[0:2].upper()
	# Primera letra del segundo apellido
	curp += apellido_materno[0:1].upper()
	# Primera letra del nombre de pila
	curp += nombre[0:1].upper()
	# Fecha de nacimiento (2 últimos dígitos del año, 2 del mes y 2 del día de nacimiento)
	curp += fecha_nac.strftime('%y%m%d')
	# Letra del sexo (H o M)
	curp += sexo[0:1].upper()
	# Dos letras correspondientes a la entidad de nacimiento (Sonora => SR)
	# en el caso de extranjeros, se marca como NE (Nacido Extranjero)
	clave_estados = {
		'aguascalientes': 'AS',
		'baja_california': 'BC',
		'baja_california_sur': 'BS',
		'campeche': 'CC',
		'coahuila': 'CL',
		'colima': 'CM',
		'chiapas': 'CS',
		'chihuahua': 'CH',
		'distrito_federal': 'DF',
		'ciudad_de_mexico': 'DF',
		'durango': 'DG',
		'guanajuato': 'GT',
		'guerrero': 'GR',
		'hidalgo': 'HG',
		'jalisco': 'JC',
		'mexico': 'MC',
		'estado_de_mexico': 'MC',
		'michoacan': 'MN',
		'morelos': 'MS',
		'nayarit': 'NT',
		'nuevo_leon': 'NL',
		'oaxaca': 'OC',
		'puebla': 'PL',
		'queretaro': 'QT',
		'quintana_roo': 'QR',
		'san_luis_potosi': 'SP',
		'sinaloa': 'SL',
		'sonora': 'SR',
		'tabasco': 'TC',
		'tamaulipas': 'TS',
		'tlaxcala': 'TL',
		'veracruz': 'VZ',
		'yucatan': 'YN',
		'zacatecas': 'ZS'
	}
	clave_estado_nac = clave_estados[estado_nac.replace(' ', '_').lower()]
	curp += clave_estado_nac
	# Primera consonante interna del primer apellido
	pcap = re.sub(f'[aeiou]', '', apellido_paterno)[1:2].upper()
	curp += pcap if pcap != 'Ñ' else 'X'
	# Primera consonante interna del segundo apellido
	curp += re.sub(f'[aeiou]', '', apellido_materno)[1:2].upper()
	# Primera consonante interna del nombre
	curp += re.sub(f'[aeiou]', '', nombre)[1:2].upper()
	# Dígito verificador del 0-9 para fechas de nacimiento hasta el año 1999 y A-Z para fechas de nacimiento a partir del 2000
	int_char = [rm.randint(0, 9), chr(rm.randint(65, 90))]
	curp += str(int_char[0] if fecha_nac.year <= 1999 else int_char[1])
	# Homoclave, para evitar duplicaciones
	curp += str(rm.randint(0, 9))
	return curp
