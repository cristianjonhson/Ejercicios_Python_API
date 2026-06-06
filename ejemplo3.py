import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
url = os.getenv("OPENROUTER_URL")
model = os.getenv("OPENROUTER_MODEL")
referer = os.getenv("OPENROUTER_REFERER")
app_name = os.getenv("OPENROUTER_APP_NAME")
timeout = int(os.getenv("TIMEOUT_SECONDS", 30))
max_tokens = int(os.getenv("MAX_TOKENS", 300))


if not api_key:
    raise ValueError("Falta OPENROUTER_API_KEY en el archivo .env")

if not url:
    raise ValueError("Falta OPENROUTER_URL en el archivo .env")

if not model:
    raise ValueError("Falta OPENROUTER_MODEL en el archivo .env")


headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": referer or "https://mi-sitio.cl",
    "X-OpenRouter-Title": app_name or "Clase APIs IA"
}


payload = {
    "model": model,
    "messages": [
        {
            "role": "system",
            "content": "Responde como mentor de Python."
        },
        {
            "role": "user",
            "content": "Explica qué es una API en 3 líneas."
        }
    ],
    "temperature": 0.3,
    "max_tokens": max_tokens
}


try:
    respuesta = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=timeout
    )

    print("Código de estado:", respuesta.status_code)

    respuesta.raise_for_status()

    datos = respuesta.json()

    mensaje = datos["choices"][0]["message"]["content"]

    print("Respuesta del modelo:")
    print(mensaje)

except requests.exceptions.HTTPError as error:
    print("Error HTTP:")
    print(error)
    print("Detalle:")
    print(respuesta.text)

except requests.exceptions.Timeout:
    print("La solicitud tardó demasiado en responder.")

except requests.exceptions.RequestException as error:
    print("Error de conexión:")
    print(error)

except KeyError:
    print("La respuesta no tiene el formato esperado.")
    print(datos)

except ValueError as error:
    print("Error de configuración o JSON:")
    print(error)