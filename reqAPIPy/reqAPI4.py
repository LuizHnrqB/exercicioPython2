from distutils.log import error
import requests
url ="https://viacep.com.br/abc/"
cep = '30140071'
formato = '/json/'
r = requests.get(url + cep + formato)
try:
 (r.status_code == 200)
 print()
 print('JSON : ', r.json())
 print()
except Exception as e:
 print(e)
 
