"""
Pruebas unitarias para ejemplo.py.

Estas pruebas no consumen internet. Se simula la respuesta de la API
de Chuck Norris y la traducción del texto.
"""

import pytest
from requests.exceptions import Timeout

from conftest import load_module_from_file


class FakeChuckResponse:
    """Respuesta simulada para la API de Chuck Norris."""

    status_code = 200

    def raise_for_status(self):
        """No lanza error porque simula una respuesta exitosa."""

    def json(self):
        """Retorna un JSON simulado con la estructura esperada."""

        return {
            "id": "abc123",
            "value": "Chuck Norris can divide by zero.",
            "url": "https://api.chucknorris.io/jokes/abc123"
        }


def test_get_random_joke_success(monkeypatch):
    """
    Debe obtener un chiste, traducirlo y retornar un objeto Joke.
    """

    module = load_module_from_file("ejemplo.py", "ejemplo_test_success")

    def fake_get(url, timeout):
        assert url == module.API_URL
        assert timeout == module.TIMEOUT_SECONDS
        return FakeChuckResponse()

    monkeypatch.setattr(module.requests, "get", fake_get)
    monkeypatch.setattr(
        module,
        "traducir_texto",
        lambda texto: "Chuck Norris puede dividir por cero."
    )

    joke = module.get_random_joke()

    assert joke.id == "abc123"
    assert joke.value == "Chuck Norris can divide by zero."
    assert joke.translated_value == "Chuck Norris puede dividir por cero."
    assert joke.url == "https://api.chucknorris.io/jokes/abc123"


def test_get_random_joke_timeout(monkeypatch):
    """
    Debe lanzar JokeAPIError cuando la API supera el tiempo de espera.
    """

    module = load_module_from_file("ejemplo.py", "ejemplo_test_timeout")

    def fake_get(url, timeout):
        raise Timeout("Tiempo de espera agotado")

    monkeypatch.setattr(module.requests, "get", fake_get)

    with pytest.raises(module.JokeAPIError) as error:
        module.get_random_joke()

    assert "tardó demasiado" in str(error.value)
