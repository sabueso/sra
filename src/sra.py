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

from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys
import ssh_cliente
import redes

#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "src/sra.ui"
#UI_FILE = "/usr/local/share/sra/ui/sra.ui"

class GUI:
	def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)
		window = self.builder.get_object('window1')
		window.show_all()
		
	#Conectamos al host
	def conectarhost(self,button):
		ent_ip = self.builder.get_object('entry1').get_text()
		ent_usuario = self.builder.get_object('entry2').get_text()
		ent_password = self.builder.get_object('entry3').get_text()
		status = self.builder.get_object('statusbar1')
		a = ssh_cliente.Lanzadera(ent_ip,ent_usuario,ent_password)	
		#status.push(1,"Conectando a"+str(ent_ip)+"")
		a.conectar()
		status.push(1,""+str(a.conectar())+"")
		#Devolvemos por pantalla el estado de conexion
		print a.conectar()
		
	#Funcion por la que mostramos en el liststore los datos de las interfaces de red
	def agregar(self,store):
		lista=self.builder.get_object('liststore2')
		test=redes.Interfaces()
		for i in test.obtenerinterfaces():
			 #lista.append([''+str(i)+'',''+test.obtenerdatoscompuestos()[i]+''])
		#for i in ssh_cliente.comando('ifconfig |grep Link |grep -e ^[A-Za-z] |cut -d \" \" -f 1'):
			 lista.append([''+str(i)+'',''+str(i)+''])

	#Detectamos las opciones seleccionadas y actuamos en consecuencia ;)
	def selector(self,treeView):
		valor=self.builder.get_object('treeview1')
		listStore, lIter = valor.get_selection().get_selected()
		seleccion = str(listStore.get(lIter,0)[0])
		pesta = self.builder.get_object('notebook2')
		if seleccion == 'Interfaces Red':
			print str(seleccion)
			pesta.set_current_page(0)
			self.agregar(self)
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
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
    sys.exit(main())