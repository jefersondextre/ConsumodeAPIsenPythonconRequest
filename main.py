'''@documentacion:
    https://requests.readthedocs.io/projects/es/es/latest/ 
    https://pokeapi.co/
    https://fakestoreapi.com/
'''
import requests
import json

def get_data():
    try:
        data={
            "title": "test",
            "price": 10
        }
        
        headers = { "Content-Type":"application/json;charset = utf-8"}
        response = requests.post(f'https://fakestoreapi.com/products',headers=headers,json=data)
        print(json.dumps(response.json(),indent=4))
        print(response.headers)
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
        
if __name__ == "__main__":
    get_data()
    