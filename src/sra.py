#!/usr/bin/python
#
# main.py
# Copyright (C) 2013 Sabueso (aka Ramiro Magallanes) <ramiro@gnubit.com>
# 
# sRa is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# sRa is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, GdkPixbuf, Gdk, GLib
import os, sys,subprocess
import ssh_cliente,redes
#import performance
import threading

###################################################################
#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "src/sra.ui"


class GUI:
	def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)
		window = self.builder.get_object('window1')
		store=self.builder.get_object('treestore1')
		#print str(store)
		padre=store.append(None, ["Interfaces"])
		store.append(padre, ["IP"])
		store.append(padre, ["Negociacion"])
		dos=store.append(None,["Otra"])
		store.append(dos, ["Sincronizacion"])
		#Gdk.threads_init()
		#threading.Thread(target=self.comandociclo).start()
		window.show_all()

	#Conectamos al host
	def conectarhost(self,button):
		ent_ip = self.builder.get_object('entry1').get_text()
		ent_usuario = self.builder.get_object('entry2').get_text()
		ent_password = self.builder.get_object('entry3').get_text()
		status = self.builder.get_object('statusbar1')
		a = ssh_cliente.Lanzadera(ent_ip,ent_usuario,ent_password)
		a.conectar()
		#Mostramos el estado de la conexion
		status.push(1,""+str(a.conectar())+"")
		#Sacamos via stdout el estado
		print a.conectar()
		#execuptime=ssh_cliente.comando("uptime")
		#Enviamos el comando a ejecutar por la tarea ciclica
		self.uptimestate()
		status2 = self.builder.get_object('statusbar2')

	def uptimestate(self):
		#commands.getstatusoutput("uptime")
		#print "hola"
		status2 = self.builder.get_object('statusbar2')
		status2.push(1,""+str(ssh_cliente.comando('uptime')).rstrip("\n")+"")
		threading.Timer(3,self.uptimestate).start()

		
	#Funcion por la que mostramos en el liststore los datos de las interfaces de red
	def infointerfaces(self,store):
		lista=self.builder.get_object('liststore2')
		#Limpiamos antiguos valores cargados en el liststore
		lista.clear()
		#Recogemos los valores de la funcion Interfaces
		test=redes.Interfaces()
		for a,b in test.obtenerinterfaces().iteritems():
			#Falta eliminar caracters de nueva liena, corchetes...
			lista.append([''+str(a)+'',''+str(b[0].strip('\n'))+'',''+str(b[1].strip('\n'))+'',''+str(b[2].strip('\n'))+''])

	#Detectamos las opciones seleccionadas y actuamos en consecuencia ;)
	def selector(self,treeView):
		valor=self.builder.get_object('treeview4')
		listStore, lIter = valor.get_selection().get_selected()
		seleccion = str(listStore.get(lIter,0)[0])
		pesta = self.builder.get_object('notebook2')
		if seleccion == 'IP':
			print str(seleccion)
			pesta.set_current_page(0)
			self.infointerfaces(self)
		else:
			print str(seleccion)
			pesta.set_current_page(1)

	#def ventana(self,button):
	#	box = Gtk.Button()
	#	#box.set_spacing (5)
	#	#box.set_orientation (Gtk.Orientation.VERTICAL)
	#	window1 = self.builder.get_object('window1')
	#	window1.show_all()
	
	#Destruimos la ventana salir
	def destroy(window, self):
		ssh_cliente.desconectar()
		Gtk.main_quit()
		

def main():
	GLib.threads_init()
	Gdk.threads_init()
	Gdk.threads_enter()
	app = GUI()
	Gtk.main()
	#Gdk.threads_leave()

if __name__ == "__main__":	
	sys.exit(main())