import sys
import geoip2.database as geo


def localizar(ip):
	try:
		localizador = geo.Reader('./GeoLite2-City.mmdb')
		posicao = localizador.city(ip)
		return posicao
	except Exception as e:
		print(e)
		print("\narquivo não encontrado")
		sys.exit()




def mostrar_dados(dados):
	print("\nContinente %s"%dados.continent.names['en'])
	print("\nPaís %s"%dados.country.names['en'])
	
	try:
		print("\nEstado %s"%dados.subdivisions[0].names['en'])
	except Exception as e:
		print("\nEstado não encontrado")
	
	
	try:
		print("\nCidade %s"%dados.city.names['en'])
	except Exception as e:
		print("\nCidade não encontrada")

	

	print("\nLatitude %f"%dados.location.latitude)
	print("\nLongitude %f"%dados.location.longitude)
	print("\nTime zone %s"%dados.location.time_zone)
	print("\nPrecisão %s"%dados.location.accuracy_radius)		


	print("\nIP %s"%dados.traits.ip_address)