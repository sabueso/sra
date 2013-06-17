#!/usr/bin/python
#Apartado de redes , funciones relativas a la configuracion de networking
#import netifaces
import ssh_cliente

class Interfaces():

	#Obtenemos Interfaces disponibles en el equipo remoto
	def obtenerinterfaces(self):
		interf=[]
		for i in ssh_cliente.comando('ifconfig |grep Link |grep -e ^[A-Za-z] |cut -d " " -f 1'): 
			interf.append(i.rstrip())
		return interf

	def obteneraddripv4(self):
		return
		
