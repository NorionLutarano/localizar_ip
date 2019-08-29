import sys
import menu
import geo
import url


parametros = menu.obter_parametros()

if not(parametros['ip']) and not(parametros['url']):
	print('Informe os parametros')
	sys.exit()

ip = parametros['ip'] if parametros['ip'] else url.obter_ip(parametros['url'])


print("-----------Localizador de ip------------")
print("\nVersão 0.1")
print("\nDesenvolvedor Norion")
geo.mostrar_dados(geo.localizar(ip))