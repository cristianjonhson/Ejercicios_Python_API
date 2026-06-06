import logging
from dataclasses import dataclass
from typing import Any, Dict

import requests
from requests.exceptions import HTTPError, RequestException, Timeout
from deep_translator import GoogleTranslator


API_URL = "https://api.chucknorris.io/jokes/random"
TIMEOUT_SECONDS = 10


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


@dataclass
class Joke:
    id: str
    value: str
    translated_value: str
    url: str


class JokeAPIError(Exception):
    """Excepción personalizada para errores al consumir la API."""


def traducir_texto(texto: str) -> str:
    """
    Traduce un texto desde inglés a español.

    Args:
        texto: Texto original en inglés.

    Returns:
        Texto traducido al español.
    """

    return GoogleTranslator(source="en", target="es").translate(texto)


def get_random_joke() -> Joke:
    """
    Obtiene un chiste aleatorio desde la API de Chuck Norris
    y traduce su contenido al español.

    Returns:
        Objeto Joke con el chiste original y traducido.
    """

    try:
        response = requests.get(API_URL, timeout=TIMEOUT_SECONDS)

        logger.info("Código de estado recibido: %s", response.status_code)

        response.raise_for_status()

        data: Dict[str, Any] = response.json()

        original_joke = data["value"]
        translated_joke = traducir_texto(original_joke)

        return Joke(
            id=data["id"],
            value=original_joke,
            translated_value=translated_joke,
            url=data["url"]
        )

    except Timeout as error:
        raise JokeAPIError("La API tardó demasiado en responder.") from error

    except HTTPError as error:
        raise JokeAPIError(f"La API respondió con un error HTTP: {error}") from error

    except RequestException as error:
        raise JokeAPIError(f"No fue posible conectarse a la API: {error}") from error

    except KeyError as error:
        raise JokeAPIError(f"La respuesta no contiene el campo esperado: {error}") from error

    except ValueError as error:
        raise JokeAPIError("La respuesta no contiene un JSON válido.") from error


def main() -> None:
    try:
        joke = get_random_joke()

        print("Chiste original:")
        print(joke.value)

        print("\nChiste traducido al español:")
        print(joke.translated_value)

        print(f"\nFuente: {joke.url}")

    except JokeAPIError as error:
        logger.error(error)


if __name__ == "__main__":
    main()