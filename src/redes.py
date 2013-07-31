#!/usr/bin/python
#Apartado de redes , funciones relativas a la configuracion de networking
#import netifaces
import ssh_cliente

class Interfaces():

	#Obtenemos Interfaces disponibles en el equipo remoto
	def obtenerinterfaces(self):
		interf=dict()
		tjtdisponibles=ssh_cliente.comando('ifconfig |grep Link |grep -e ^[A-Za-z] |cut -d " " -f 1')
		for tjtred in tjtdisponibles:
			ip=ssh_cliente.comando("ifconfig "+str(tjtred).rstrip('\n')+" | grep -Eo \'inet (addr:)?([0-9]*\.){3}[0-9]*\' | grep -Eo \'([0-9]*\.){3}[0-9]*\'")
			mascara=ssh_cliente.comando("ifconfig "+str(tjtred).rstrip('\n')+" | grep -Eo \'Mask:?([0-9]*\.){3}[0-9]*\' | grep -Eo \'([0-9]*\.){3}[0-9]*\'")
			#interf.append(i.rstrip()).append(ip)
			interf[""+str(tjtred).rstrip('\n')+""] = [""+str(ip).rstrip('\n')+""]
			interf[""+str(tjtred).rstrip('\n')+""].append(""+str(mascara).rstrip('\n')+"")
		print "----------**********************DEBUG********************************---------------"
		print interf
		print "----------***********************************************************---------------"
		return interf

	def obteneraddripv4(self):
		return
		
