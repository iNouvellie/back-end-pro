class Estudiante(object):
	def __init__(self, nombre_r, edad_r):
		self.nombre = nombre_r
		self.edad = edad_r

	def hola(self):
		#(%s texto) (%i numero)
		return "Mi nombre es %s y tengo %i" % (self.nombre, self.edad)

e = Estudiante("Roberto", 28)

s = e.hola()

#print s

lista_de_alumnos = list()

for es in range(5):
	nombre = "Estudiante %i" % es
	e = Estudiante(nombre, 23)
	lista_de_alumnos.append(e)

#print lista_de_alumnos

for es in lista_de_alumnos:
	if es.nombre == "Estudiante 2":
		print "Soy el estudiante 2"
	else:
		print "No soy el estudiante 2"