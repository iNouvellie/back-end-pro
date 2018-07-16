if "Hola" == "Mundo":
	print "Igual"
else:
	print "No son iguales"

#Ejemplo

a = 4
b = a

l = [32, 23, 13, 14, "Hola", True, [0, 2]]

print l[2]
print l[6][1]

t = (32, 23, 13, 14, "Hola", True, (0, 2))

print t[2]

d = {"libro" : "opera en el vacio", "autor" : "freeddy vega"}
print d["autor"]

l2 = [1, 2, 3, 4]
print l2

#Agrega al final
l2.append(65)
print l2

#Borra el ultimo
l2.pop()
print l2

#Borrar item indicandolos
l2.remove(2)
print l2