#!/usr/bin/env python

import paramiko

class Lanzadera(object):

	def __init__(self,ip,username,clave):
		self._ip = ip
		self._usuario = username
		self._clave = clave

	def conectar(self):
		global conexion
		conexion = paramiko.Transport((self._ip, 22))
		conexion.connect(username = self._usuario, password = self._clave)
		# Abrimos una sesion en el servidor
		#global canal


def comando(com):
	# Ejecutamos el comando, en este caso un sencillo 'ls' para ver
	# el listado de archivos y directorios
	canal = conexion.open_session()
	canal.exec_command(com)
	# Y vamos a ver la salida
	salida = canal.makefile('rb', -1).readlines()
	if salida:
		# Si ha ido todo bien mostramos el listado de directorios
		print salida
	else:
		# Si se ha producido algun error lo mostramos
		print canal.makefile_stderr('rb', -1).readlines()
	canal = conexion.open_session()
	return salida

a = Lanzadera('localhost','root','tetra')
a.conectar()

b = str(comando('ifconfig |grep Link |grep -e ^[A-Za-z] |cut -d \" \" -f 1'))
print b

