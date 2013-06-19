## Process this file with automake to produce Makefile.in
## Created by Anjuta


uidir = $(pkgdatadir)/ui
ui_DATA = sra.ui


## The main script
bin_SCRIPTS = sra.py \
	ssh_cliente.py \
	redes.py \
	performance.py

## Directory where .class files will be installed
sradir = $(pythondir)/sra


sra_PYTHON = \
	sra.py


EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(pkgdatadir)
