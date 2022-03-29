import requests
url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'
r = requests.get(url + cep + formato,'xml')

if (r.status_code == 200):
 print()
 print('XML : ', r.text)
 with open('r.txt', 'w') as file:
    file.write(r.content)
 print()
else:
 print('Nao houve sucesso na requisicao.')