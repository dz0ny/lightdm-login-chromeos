.PHONY: default deb skip ch

default: skip

all: skip

ch:
	git-dch -R --auto -c

deb:
	git-buildpackage

skip:
	echo "Tabularasa"
