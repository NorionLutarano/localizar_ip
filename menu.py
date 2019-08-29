import argparse


def obter_parametros():
	parametros = argparse.ArgumentParser()
	parametros.add_argument("--url",help="url do site, exemplo www.site.com",default=False)
	parametros.add_argument("--ip",help="ip do site, ipv4",default=False)	
	obterParametro = parametros.parse_args()
	return {'url':obterParametro.url,'ip':obterParametro.ip}