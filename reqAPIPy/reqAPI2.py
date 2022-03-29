import requests
url = 'https://viacep.com.br/ws/'
cep = 30140070
formato = '/json/'
while cep < 30140075: 
        cep = cep +1
        r = requests.get(url + str(cep) + formato)    
        print()
        print('JSON : ', r.json())
        print()
  
 