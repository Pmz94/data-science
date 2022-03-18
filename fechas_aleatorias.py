import datetime as dt
import random as rm
import time

def random_date(time_format = '%Y-%m-%d', n = 1, start = None, end = None):
	"""Get a time at a proportion of a range of two formatted times.
	time_format (strftime-style) is the format you want the date be given
	start and end should be strings specifying times formatted in the
	given format, giving an interval [start, end].
	The returned time will be in the specified format.
	"""
	if start and end:
		stime = time.mktime(time.strptime(start, time_format))
		etime = time.mktime(time.strptime(end, time_format))
	else:
		stime = time.mktime(time.strptime('700101', '%y%m%d'))
		etime = time.mktime(time.localtime())

	rand_time = []
	if n > 1:
		for _ in range(n):
			ptime = stime + rm.random() * (etime - stime)
			rand_time.append(time.strftime(time_format, time.localtime(ptime)))
	else:
		ptime = stime + rm.random() * (etime - stime)
		rand_time = time.strftime(time_format, time.localtime(ptime))

	return rand_time

def calcular_edad(born):
	today = dt.date.today()
	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

fechas = random_date('%Y-%m-%d', 5)

for fecha in sorted(fechas, reverse = True):
	dd = dt.datetime.strptime(fecha, '%Y-%m-%d')
	# if dd.year > 2005: dd = dd.replace(year = dd.year - 100)
	nueva_fecha = dd.strftime('%d de %b de %Y')
	edad = calcular_edad(dd.date())
	print(fecha, 'tiene', edad, 'años', f'(Nacio en {nueva_fecha})')
