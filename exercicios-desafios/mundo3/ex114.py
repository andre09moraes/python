import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está disponível no momento.')
else:
    print('Tudo OK!')
    print(site.read())
    