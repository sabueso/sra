## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src 

sradocdir = ${prefix}/doc/sra
sradoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS


EXTRA_DIST = $(sradoc_DATA)


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(sradocdir)
