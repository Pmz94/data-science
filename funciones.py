import math
import random as rm
from itertools import groupby
from typing import List, Union
import matplotlib.pyplot as plt
import numpy as np
import prettytable as pt
import scipy.stats as st
import unicodedata
import datetime as dt
import re


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

	if titulo:
		plt.title(titulo)
	if label_x:
		plt.xlabel(label_x)
	if label_y:
		plt.ylabel(label_y)
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
	if ejex_enteros:
		plt.xticks(range(math.floor(min(ejex)), math.ceil(max(ejex)) + 1))
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


# Obtener complexion fisica segun IMC
def complexion_fisica(altura, peso):
	# peso en kg y altura en m
	imc = peso / (altura ** 2)
	# OJO el imc no distigue sexo, edad, grasa o musculo
	# Digamos que esto define el volumen de la persona
	complexion = ''
	if -np.inf <= imc < 25:
		complexion = 'Chico'
	elif 25 <= imc < 35:
		complexion = 'Medio'
	elif 35 <= imc < np.inf:
		complexion = 'Grande'
	return complexion


# Calcular CURP
def sacar_curp(nombre: str, apellido_paterno: str, apellido_materno: str, sexo: str, fecha_nac: Union[str, dt.datetime], estado_nac: str) -> str:
	nombre = quitar_acentos(nombre).upper().replace('??', 'X')
	apellido_paterno = quitar_acentos(apellido_paterno).upper().replace('??', 'X')
	apellido_materno = quitar_acentos(apellido_materno).upper().replace('??', 'X')
	estado_nac = quitar_acentos(estado_nac.replace(' ', '_').lower())
	if isinstance(fecha_nac, str):
		fecha_nac = dt.datetime.strptime(fecha_nac, '%Y-%m-%d')
	# Primera letra y vocal del primer apellido
	curp = apellido_paterno[0:2].upper()
	# Primera letra del segundo apellido
	curp += apellido_materno[0:1].upper()
	# Primera letra del nombre de pila
	curp += nombre[0:1].upper()
	# Fecha de nacimiento (2 ??ltimos d??gitos del a??o, 2 del mes y 2 del d??a de nacimiento)
	curp += fecha_nac.strftime('%y%m%d')
	# Letra del sexo (H o M)
	curp += sexo[0:1].upper()
	# Dos letras correspondientes a la entidad de nacimiento segun RENAPO (Sonora => SR)
	# en el caso de extranjeros, se marca como NE (Nacido Extranjero)
	clave_estados = {
		'aguascalientes': 'AS', 'baja_california': 'BC', 'baja_california_sur': 'BS',
		'campeche': 'CC', 'coahuila': 'CL', 'colima': 'CM', 'chiapas': 'CS', 'chihuahua': 'CH',
		'distrito_federal': 'DF', 'ciudad_de_mexico': 'DF', 'durango': 'DG', 'guanajuato': 'GT',
		'guerrero': 'GR', 'hidalgo': 'HG', 'jalisco': 'JC', 'mexico': 'MC', 'estado_de_mexico': 'MC',
		'michoacan': 'MN', 'morelos': 'MS', 'nayarit': 'NT', 'nuevo_leon': 'NL', 'oaxaca': 'OC',
		'puebla': 'PL', 'queretaro': 'QT', 'quintana_roo': 'QR', 'san_luis_potosi': 'SP', 'sinaloa': 'SL',
		'sonora': 'SR', 'tabasco': 'TC', 'tamaulipas': 'TS', 'tlaxcala': 'TL', 'veracruz': 'VZ',
		'yucatan': 'YN', 'zacatecas': 'ZS'
	}
	if estado_nac in clave_estados:
		curp += clave_estados[estado_nac]
	else:
		curp += 'NE'
	# Primera consonante interna del primer apellido
	curp += re.sub(f'[aeiou]', '', apellido_paterno)[1:2].upper()
	# Primera consonante interna del segundo apellido
	curp += re.sub(f'[aeiou]', '', apellido_materno)[1:2].upper()
	# Primera consonante interna del nombre
	curp += re.sub(f'[aeiou]', '', nombre)[1:2].upper()
	# D??gito verificador del 0-9 para fechas de nacimiento hasta el a??o 1999 y A-Z para fechas de nacimiento a partir del 2000
	int_char = [rm.randint(0, 9), chr(rm.randint(65, 90))]
	curp += str(int_char[0] if fecha_nac.year <= 1999 else int_char[1])
	# Homoclave, para evitar duplicaciones
	curp += str(rm.randint(0, 9))
	return curp


# Obtener tu signo segun tu cumplea??os
def sacar_signo(fecha_nac: Union[str, dt.datetime]):
	if isinstance(fecha_nac, str):
		fecha_nac = dt.datetime.strptime(fecha_nac, '%Y-%m-%d')
	dia = int(fecha_nac.strftime('%d'))
	mes = int(fecha_nac.strftime('%m'))
	astro_sign = ''
	if mes == 12:
		astro_sign = 'Sagitario' if dia < 22 else 'Capricornio'
	elif mes == 1:
		astro_sign = 'Capricornio' if dia < 20 else 'Aquario'
	elif mes == 2:
		astro_sign = 'Aquario' if dia < 19 else 'Piscis'
	elif mes == 3:
		astro_sign = 'Piscis' if dia < 21 else 'Aries'
	elif mes == 4:
		astro_sign = 'Aries' if dia < 20 else 'Tauro'
	elif mes == 5:
		astro_sign = 'Tauro' if dia < 21 else 'Geminis'
	elif mes == 6:
		astro_sign = 'Geminis' if dia < 21 else 'Cancer'
	elif mes == 7:
		astro_sign = 'Cancer' if dia < 23 else 'Leo'
	elif mes == 8:
		astro_sign = 'Leo' if dia < 23 else 'Virgo'
	elif mes == 9:
		astro_sign = 'Virgo' if dia < 23 else 'Libra'
	elif mes == 10:
		astro_sign = 'Libra' if dia < 23 else 'Escorpio'
	elif mes == 11:
		astro_sign = 'Escorpio' if dia < 22 else 'Sagitario'
	return astro_sign
