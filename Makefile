.PHONY: default deb

default: deb lint

all: deb lint

deb:
	dpkg --build lightdm-login-chromiumos ./

lint:
	lintian lightdm-login-chromiumos*.deb	
