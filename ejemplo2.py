
# Importar en Python o Google Colab
import requests

url = "https://api.chucknorris.io/jokes/random"
respuesta = requests.get(url)

print("Código de estado:", respuesta.status_code)

if respuesta.status_code == 200:
    datos = respuesta.json()
    print(datos["value"])
else:
    print("Error al consumir la API")


datos = respuesta.json()
print(type(datos))
print(datos.keys())
print(datos.get("value", "Campo no encontrado"))
