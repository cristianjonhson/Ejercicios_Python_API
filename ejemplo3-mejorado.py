import os
import logging
from typing import Any, Dict, List

import requests
from requests import Response
from requests.exceptions import HTTPError, RequestException, Timeout



os.environ["OPENROUTER_API_KEY"] = "TU_API_KEY_AQUI"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "openai/gpt-chat-latest"
TIMEOUT_SECONDS = 30


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


class OpenRouterAPIError(Exception):
    """Excepción personalizada para errores al consumir OpenRouter."""


def get_api_key() -> str:
    """
    Obtiene la API Key desde las variables de entorno.

    Returns:
        API Key de OpenRouter.

    Raises:
        OpenRouterAPIError: Si la API Key no existe.
    """

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise OpenRouterAPIError(
            "No se encontró la variable de entorno OPENROUTER_API_KEY."
        )

    return api_key


def build_headers(api_key: str) -> Dict[str, str]:
    """
    Construye los headers necesarios para consumir la API.
    """

    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://mi-sitio.cl",
        "X-OpenRouter-Title": "Clase APIs IA"
    }


def build_payload(prompt: str) -> Dict[str, Any]:
    """
    Construye el cuerpo de la solicitud enviada al modelo.
    """

    return {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "Responde como mentor de Python."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.3
    }


def send_request(headers: Dict[str, str], payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Envía la solicitud a OpenRouter y retorna la respuesta en JSON.
    """

    try:
        response: Response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload,
            timeout=TIMEOUT_SECONDS
        )

        logger.info("Código de estado recibido: %s", response.status_code)

        response.raise_for_status()

        return response.json()

    except Timeout as error:
        raise OpenRouterAPIError("La solicitud superó el tiempo máximo de espera.") from error

    except HTTPError as error:
        error_message = response.text if response is not None else str(error)
        raise OpenRouterAPIError(f"Error HTTP al consumir OpenRouter: {error_message}") from error

    except RequestException as error:
        raise OpenRouterAPIError(f"Error de conexión con OpenRouter: {error}") from error

    except ValueError as error:
        raise OpenRouterAPIError("La respuesta recibida no es un JSON válido.") from error


def extract_model_response(data: Dict[str, Any]) -> str:
    """
    Extrae el texto generado por el modelo desde la respuesta de OpenRouter.
    """

    try:
        return data["choices"][0]["message"]["content"]

    except KeyError as error:
        raise OpenRouterAPIError(f"Falta una clave esperada en la respuesta: {error}") from error

    except IndexError as error:
        raise OpenRouterAPIError("La respuesta no contiene resultados en 'choices'.") from error


def ask_model(prompt: str) -> str:
    """
    Función principal para enviar un prompt al modelo y obtener la respuesta.
    """

    api_key = get_api_key()
    headers = build_headers(api_key)
    payload = build_payload(prompt)

    data = send_request(headers, payload)

    return extract_model_response(data)


def main() -> None:
    prompt = "Explica qué es una API en 3 líneas."

    try:
        respuesta = ask_model(prompt)
        print("Respuesta del modelo:")
        print(respuesta)

    except OpenRouterAPIError as error:
        logger.error(error)


if __name__ == "__main__":
    main()