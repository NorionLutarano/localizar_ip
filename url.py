import socket

def obter_ip(url):
	return socket.gethostbyname(url)
