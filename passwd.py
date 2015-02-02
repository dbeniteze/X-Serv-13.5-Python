#!usr/bin/python 
fich = open("/etc/passwd", "r")
lineas= fich.readlines()
dicc = {}
for i in lineas:
    separada = i.split(":", len(lineas))
    user = separada[0]
    shell = separada[-1]
    dicc[user] = shell
try:
	print 'root', dicc['root'], 'imaginario', dicc['imaginario']
except KeyError, e:
	print "No se encuentra el usuario", str(e)