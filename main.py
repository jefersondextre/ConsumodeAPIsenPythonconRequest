'''@documentacion:
    https://requests.readthedocs.io/projects/es/es/latest/ 
    https://pokeapi.co/
    https://fakestoreapi.com/
'''
import requests
import json

def get_data():
    try:
        headers = { "Content-Type":"application/json:charset = utf-8"}
        response=requests.get(f'https://fakestoreapi.com/carts/6',headers=headers)
        print(json.dumps(response.json(),indent=4))
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
        
if __name__ == "__main__":
    get_data()
    