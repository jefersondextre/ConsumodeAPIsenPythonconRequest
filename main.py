'''@documentacion:
    https://requests.readthedocs.io/projects/es/es/latest/ 
    https://pokeapi.co/
'''
import requests
import json

def get_data():
    # response = requests.get('https://www.diresacallao.gob.pe/wdiresa/portal/')
    # print(response.content)
    # response = requests.get('https://pokeapi.co/api/v2/pokemon/')
    # print(response.status_code, response.content)
    response = requests.get('https://pokeapi.co/api/v2/pokemon/')
    print(json.dumps(response.json(),indent=4))

if __name__ == "__main__":
    get_data()
    