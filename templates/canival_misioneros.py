#!/usr/bin/env python
# coding: utf-8
# vim:fileencoding=utf-8

import copy

"""
Tres misioneros y tres canÃ­bales quieren cruzar un rÃ­o. Solo hay una canoa
que puede ser usada por una o dos personas, ya sean misioneros o canÃ­bales.

Hay que tener cuidado en que en ningÃºn momento el nÃºmero de canÃ­bales supere
al de misioneros en ninguna de las dos orillas, o se los comerÃ¡n.

Juan J. MartÃ­nez <reidrac*en*usebox.net>
"""

class Estado(object):
	def __init__(self, estado, canoa):
		self.estado = estado
		self.canoa = canoa

		if not self.es_valido():
			raise ValueError("estado no vÃ¡lido")

	def es_valido(self):
		for gente in self.estado:
			for persona in gente:
				if persona > 3 or persona < 0:
					return False

		for mis, can in self.estado:
			if mis and can > mis:
				return False

		return True

	def viaja(self, gente):
		"""
		Genera un nuevo estado basado en el actual y aplicando un
		viaje como parÃ¡metro.
		"""
		estado = copy.deepcopy(self.estado)
		canoa = self.canoa

		estado[canoa][0] -= gente[0]
		estado[canoa][1] -= gente[1]
		canoa = 0 if canoa else 1
		estado[canoa][0] += gente[0]
		estado[canoa][1] += gente[1]

		return Estado(estado, canoa)

	def __str__(self):
		"""Muestra el estado como una representaciÃ³n en texto."""
		return "M: %d C: %d | %s\\___/%s | M: %d C: %d" % (
			   self.estado[0][0], self.estado[0][1],
			   '~' * 8 * self.canoa, '~' * (8 - 8 * self.canoa),
			   self.estado[1][0], self.estado[1][1]
			   )

	def __eq__(self, other):
		return self.estado == other.estado and self.canoa == other.canoa

	def __ne__(self, other):
		return not self.__eq__(other)

def main():
	# donde empezamos
	inicio = Estado([[3,3],[0,0]], 0)
	# a donde queremos llegar
	final = Estado([[0,0],[3,3]], 1)

	# los viaje posibles (legales)
	viajes = [[1,0], [0, 1], [1, 1], [2, 0], [0, 2]]

	# los viajes que probamos desde cada estado
	viajes_posibles = list(viajes)

	# guardamos el recorrido y las opciones que no hemos usado
	# para poder 'volver atrÃ¡s' si hay problemas (backtracking)
	recorrido = []
	viajes_restantes = []

	while inicio != final and viajes_posibles:
		while viajes_posibles:
			# probamos un viaje cualquiera
			viaje = viajes_posibles.pop()

			try:
				nuevo = inicio.viaja(viaje)

				# si no hemos estado nunca allÃ­
				if nuevo not in recorrido:
					# guarda el estado y las opciones restantes
					recorrido.append(inicio)
					viajes_restantes.append(viajes_posibles)

					# continuamos desde la nueva posiciÃ³n
					inicio = nuevo
					viajes_posibles = list(viajes)
			except ValueError:
				# no es vÃ¡lido, probamos el siguiente
				pass

		# si no hemos encontrado nada, backtracking
		if not viajes_posibles and recorrido:
			inicio = recorrido.pop()
			viajes_posibles = viajes_restantes.pop()

	if inicio == final:
		print "Tenemos un resultado!"
		for estado in recorrido:
			print estado
		print inicio
	else:
		# no va a pasar ;)
		print "No hemos encontrado un resultado :("

if __name__ == "__main__":
	main()

# EOF