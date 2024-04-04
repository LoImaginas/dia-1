import requests
import json

def request_get(url):
    return json.loads(requests.get(url).text)

if __name__ ==  "__main__":
    url = "https://aves.ninjas.cl/api/birds"
    
    #Metodo GET en API
    response = request_get(url)
    print(response)
    

response = requests.get('https://aves.ninjas.cl/api/birds')
#comprobar si la peticion fue existosa
if response.status_code == 200: 
    print(response)
    print("solicitud exitosa")#200 ok solicitud exitosa
else:    
    print("Error en la solicitud. Codigo de error:", response.status_code)
        
    