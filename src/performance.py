#!/usr/bin/python
import threading

def comandociclo():
	print str("hola")

def ejecucion():
	t = threading.Timer(5, comandociclo)
	t.start()