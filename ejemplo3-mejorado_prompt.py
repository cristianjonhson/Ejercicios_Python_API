import os
import logging
from typing import Any, Dict

import requests
from requests import Response
from requests.exceptions import HTTPError, RequestException, Timeout
from dotenv import load_dotenv


load_dotenv()


OPENROUTER_URL = os.getenv(
    "OPENROUTER_URL",
    "https://openrouter.ai/api/v1/chat/completions"
)

MODEL_NAME = os.getenv(
    "OPENROUTER_MODEL",
    "openai/gpt-chat-latest"
)

OPENROUTER_REFERER = os.getenv(
    "OPENROUTER_REFERER",
    "https://mi-sitio.cl"
)

OPENROUTER_APP_NAME = os.getenv(
    "OPENROUTER_APP_NAME",
    "Clase APIs IA"
)

TIMEOUT_SECONDS = int(os.getenv("TIMEOUT_SECONDS", 30))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 300))


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


def validate_config() -> None:
    """
    Valida que las variables principales estén configuradas.
    """

    if not OPENROUTER_URL:
        raise OpenRouterAPIError("No se encontró OPENROUTER_URL.")

    if not MODEL_NAME:
        raise OpenRouterAPIError("No se encontró OPENROUTER_MODEL.")


def build_headers(api_key: str) -> Dict[str, str]:
    """
    Construye los headers necesarios para consumir la API.
    """

    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_REFERER,
        "X-OpenRouter-Title": OPENROUTER_APP_NAME
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
        "temperature": 0.3,
        "max_tokens": MAX_TOKENS
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
        raise OpenRouterAPIError(
            "La solicitud superó el tiempo máximo de espera."
        ) from error

    except HTTPError as error:
        error_message = (
            error.response.text
            if error.response is not None
            else str(error)
        )

        raise OpenRouterAPIError(
            f"Error HTTP al consumir OpenRouter: {error_message}"
        ) from error

    except RequestException as error:
        raise OpenRouterAPIError(
            f"Error de conexión con OpenRouter: {error}"
        ) from error

    except ValueError as error:
        raise OpenRouterAPIError(
            "La respuesta recibida no es un JSON válido."
        ) from error


def extract_model_response(data: Dict[str, Any]) -> str:
    """
    Extrae el texto generado por el modelo desde la respuesta de OpenRouter.
    """

    try:
        return data["choices"][0]["message"]["content"]

    except KeyError as error:
        raise OpenRouterAPIError(
            f"Falta una clave esperada en la respuesta: {error}"
        ) from error

    except IndexError as error:
        raise OpenRouterAPIError(
            "La respuesta no contiene resultados en 'choices'."
        ) from error


def ask_model(prompt: str) -> str:
    """
    Función principal para enviar un prompt al modelo y obtener la respuesta.
    """

    validate_config()

    api_key = get_api_key()
    headers = build_headers(api_key)
    payload = build_payload(prompt)

    data = send_request(headers, payload)

    return extract_model_response(data)


def read_user_prompt() -> str:
    """
    Solicita al usuario un prompt desde la consola.

    Returns:
        Prompt ingresado por el usuario.

    Raises:
        OpenRouterAPIError: Si el usuario no escribe un prompt válido.
    """

    print("\nEscribe el prompt que quieres enviar a OpenRouter.")
    print("Ejemplo: Explica qué es una API en 3 líneas.")
    print("Para cancelar, presiona Enter sin escribir nada.\n")

    prompt = input("Prompt: ").strip()

    if not prompt:
        raise OpenRouterAPIError("No se ingresó ningún prompt.")

    return prompt


def main() -> None:
    try:
        prompt = read_user_prompt()
        respuesta = ask_model(prompt)

        print("\nRespuesta del modelo:")
        print("-----------------------------------")
        print(respuesta)

    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")

    except OpenRouterAPIError as error:
        logger.error(error)


if __name__ == "__main__":
    main()
