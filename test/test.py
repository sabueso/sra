#!/usr/bin/env python
import netifaces

#def obtener():
#	interf=[]
#	for i in netifaces.interfaces():
#		interf.append(i)
#	print interf


#def obtenerdatoscompuestos():
listinterfaz={}
for b in netifaces.interfaces():
	listinterfaz[''+b+''] = ''+netifaces.ifaddresses(''+b+'')[2][0]['addr']+''
	#print listinterfaz[''+b+'']

for j in listinterfaz.keys():
	print listinterfaz[''+j+'']
#	return listinterfaz

#btenerdatoscompuestos()
