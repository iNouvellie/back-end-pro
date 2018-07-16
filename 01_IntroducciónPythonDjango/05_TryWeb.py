import urllib2

try:
	f = urllib2.urlopen("http://www.mejorando.la")
	print f.read()
	f.close()

except HTTPError, e:
	print "Ocurrio un error1"
	print e.code

except URLError, e:
	print "Ocurrio un error2"
	print e.reason