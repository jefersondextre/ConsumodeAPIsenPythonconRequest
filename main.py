'''@documentacion:
    https://requests.readthedocs.io/projects/es/es/latest/ 
    https://pokeapi.co/
    https://fakestoreapi.com/
'''
import requests
import json

def get_data():
    try:
        # response = requests.get('https://www.diresacallao.gob.pe/wdiresa/portal/')
        # print(response.content)
        # response = requests.get('https://pokeapi.co/api/v2/pokemon/')
        # print(response.status_code, response.content)
        # data={
        #     "title":"new product",
        #     "description" : "new product",
        #     "price": 12.50,
        #     "image": "https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_.jpg",
        #     "category": "electronic"
        # }
        # data={
        #     "username":"johnd",
        #     "password":"m38rmF$"
        # }
        data = {
            "title":"test product",
            "price":25.50,
            "descripcion": "test",
            "image": "https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_.jpg",
            "category":"electronic"
        }
        id=input("Ingrese el id del producto a modificar: ")
        response=requests.put(f"https://fakestoreapi.com/products/{id}",data)
        # response = requests.post('https://fakestoreapi.com/auth/login',data)
        print(json.dumps(response.json(),indent=4))
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
        
if __name__ == "__main__":
    get_data()
    