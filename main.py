'''@documentacion:
    https://requests.readthedocs.io/projects/es/es/latest/ 
    https://pokeapi.co/
    https://fakestoreapi.com/
'''
# from email import header
# from unicodedata import category
import requests
import json

def login():
    try:
        data={
            "username":"mor_2314",
            "password":"83r5^_"
        }
        response = requests.post("https://fakestoreapi.com/auth/login",json = data)
       
        get_products(response.json()['token'])
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")

def get_products(token):
    headers ={
        "Authorization": token  
    }
    print(headers)
    response = requests.get('https://fakestoreapi.com/products',headers=headers)
    print(json.dumps(response.json(),indent = 4))
    
if __name__ == "__main__":
    login()
    