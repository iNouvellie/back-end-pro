#Ejemplo de clases
class Pokemon(object):
	def __init__(self, nombreP, numeroP):
		self.nombre = nombreP
		self.numero = numeroP

	def pokedex(self):
		return "El pokemon atrapado es %s: %s" % (self.numero, self.nombre)

a = Pokemon("Bulbasaur", "001")

b = a.pokedex()

print b