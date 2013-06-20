#!/usr/bin/python
import threading,ssh_cliente,commands
import sra

def uptimestate():
	#commands.getstatusoutput("uptime")
	#print "hola"
	status2 = self.builder.get_object('statusbar2')
	status2.push(1,""+ssh_cliente.comando("uptime")+"")
	threading.Timer(3,uptimestate).start()
	return
