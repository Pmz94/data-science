import pandas as pd
import datetime

fechas = pd.read_csv('./conjunto_datos/fechas.csv')
print(fechas)

def calculate_age(born):
	today = datetime.date.today()
	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

for fecha in sorted(fechas['fecha'], reverse = True):
	dd = datetime.datetime.strptime(str(fecha), '%y%m%d')
	if dd.year > 2005: dd = dd.replace(year = dd.year - 100)
	nueva_fecha = dd.strftime('%d de %b de %Y')
	edad = calculate_age(dd.date())
	print(fecha, 'tiene', edad, 'años', f'(Nacio en {nueva_fecha})')
