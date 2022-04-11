import random as rm


def disparar():
	if rm.randint(1, 6) == 1:
		# os.remove("C:\Windows\System32")
		print('\033[31m*Bang!*\033[0m')
		return False
	else:
		print('\033[32m*Click*\033[0m')
		return True


# n personas van a jugar a la ruleta rusa
personas = {
	'Persona 1': True,
	'Persona 2': True,
	'Persona 3': True
}

# Estas personas tienen un revolver con capacidad de hasta 6 balas pero solo esta cargado con una
p = 1 / 6

# Se van turnando en apuntarse en su cabeza y jalar el gatillo de su revolver
# El juego se acaba hasta que una persona quede viva
while sum(personas.values()) > 1:
	for k, v in personas.items():
		if not v: continue
		print('Turno de', k)
		personas[k] = disparar()
		if not personas[k]:
			print(f'\033[31m\n{k} eliminada\033[0m\n')
		print('')
		if sum(personas.values()) == 1: break
personas = {k: v for k, v in personas.items() if v}
print(personas)
