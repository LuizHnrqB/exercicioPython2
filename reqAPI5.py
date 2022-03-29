import requests
r = requests.get('http://www.google.com/search', params={'q':
'Protocolo HTTP'})
if (r.status_code == 200):
 with open('response.txt', 'w') as file:
    file.write(str(r.content))
else:
 print('Nao houve sucesso na requisicao.')
