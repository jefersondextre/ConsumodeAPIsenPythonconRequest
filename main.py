'''@documentacion:
    https://requests.readthedocs.io/projects/es/es/latest/ 
    https://pokeapi.co/
'''
import requests
import json

def get_data():
    try:
        # response = requests.get('https://www.diresacallao.gob.pe/wdiresa/portal/')
        # print(response.content)
        # response = requests.get('https://pokeapi.co/api/v2/pokemon/')
        # print(response.status_code, response.content)
        response = requests.get('https://pokeapi.co/api/v2/ability/immunity')
        print(json.dumps(response.json(),indent=4))
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
        
if __name__ == "__main__":
    get_data()
    