GOLANG_VERSION := go1.13.6
all:
	wget https://dl.google.com/go/$(GOLANG_VERSION).linux-amd64.tar.gz
	sudo tar -xvf $(GOLANG_VERSION).linux-amd64.tar.gz
	[ -e /usr/local/go ] && sudo rm -rf /usr/local/go
	sudo mv go /usr/local
	rm $(GOLANG_VERSION).linux-amd64.tar.gz