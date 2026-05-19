"""
Pruebas unitarias para ejemplo3-mejorado.py.

Estas pruebas no consumen la API real de OpenRouter.
Se simulan variables de entorno, entrada por consola y respuesta del modelo.
"""

import pytest

from conftest import load_module_from_file


def load_openrouter_module(monkeypatch, module_name: str):
    """
    Carga ejemplo3-mejorado.py con variables de entorno simuladas.
    """

    monkeypatch.setenv("OPENROUTER_API_KEY", "test-api-key")
    monkeypatch.setenv(
        "OPENROUTER_URL",
        "https://openrouter.ai/api/v1/chat/completions"
    )
    monkeypatch.setenv("OPENROUTER_MODEL", "openai/gpt-chat-latest")
    monkeypatch.setenv("OPENROUTER_REFERER", "https://test.local")
    monkeypatch.setenv("OPENROUTER_APP_NAME", "Tests OpenRouter")
    monkeypatch.setenv("TIMEOUT_SECONDS", "30")
    monkeypatch.setenv("MAX_TOKENS", "300")

    return load_module_from_file("ejemplo3-mejorado.py", module_name)


def test_get_api_key_success(monkeypatch):
    """
    Debe leer la API Key desde variables de entorno.
    """

    module = load_openrouter_module(monkeypatch, "openrouter_test_api_key")

    assert module.get_api_key() == "test-api-key"


def test_get_api_key_missing(monkeypatch):
    """
    Debe lanzar OpenRouterAPIError si no existe OPENROUTER_API_KEY.
    """

    module = load_openrouter_module(monkeypatch, "openrouter_test_missing_key")

    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)

    with pytest.raises(module.OpenRouterAPIError) as error:
        module.get_api_key()

    assert "OPENROUTER_API_KEY" in str(error.value)


def test_build_headers(monkeypatch):
    """
    Debe construir correctamente los headers de OpenRouter.
    """

    module = load_openrouter_module(monkeypatch, "openrouter_test_headers")

    headers = module.build_headers("abc123")

    assert headers["Authorization"] == "Bearer abc123"
    assert headers["Content-Type"] == "application/json"
    assert headers["HTTP-Referer"] == "https://test.local"
    assert headers["X-OpenRouter-Title"] == "Tests OpenRouter"


def test_build_payload_uses_user_prompt(monkeypatch):
    """
    Debe construir el payload usando el prompt ingresado por el usuario.
    """

    module = load_openrouter_module(monkeypatch, "openrouter_test_payload")

    payload = module.build_payload("Dame 5 buenas prácticas para consumir APIs REST.")

    assert payload["model"] == "openai/gpt-chat-latest"
    assert payload["messages"][0]["role"] == "system"
    assert payload["messages"][1]["role"] == "user"
    assert (
        payload["messages"][1]["content"]
        == "Dame 5 buenas prácticas para consumir APIs REST."
    )
    assert payload["temperature"] == 0.3
    assert payload["max_tokens"] == 300


def test_read_user_prompt_success(monkeypatch):
    """
    Debe leer un prompt ingresado por consola.
    """

    module = load_openrouter_module(monkeypatch, "openrouter_test_read_prompt")

    monkeypatch.setattr(
        "builtins.input",
        lambda mensaje: "Explica qué es una API en 3 líneas."
    )

    prompt = module.read_user_prompt()

    assert prompt == "Explica qué es una API en 3 líneas."


def test_read_user_prompt_empty(monkeypatch):
    """
    Debe lanzar error si el usuario presiona Enter sin escribir prompt.
    """

    module = load_openrouter_module(monkeypatch, "openrouter_test_empty_prompt")

    monkeypatch.setattr("builtins.input", lambda mensaje: "")

    with pytest.raises(module.OpenRouterAPIError) as error:
        module.read_user_prompt()

    assert "No se ingresó ningún prompt" in str(error.value)


def test_ask_model_success_without_real_api_call(monkeypatch):
    """
    Debe retornar la respuesta del modelo simulando la llamada HTTP.
    """

    module = load_openrouter_module(monkeypatch, "openrouter_test_ask_model")

    def fake_send_request(headers, payload):
        assert headers["Authorization"] == "Bearer test-api-key"
        assert payload["messages"][1]["content"] == "Hola modelo"
        return {
            "choices": [
                {
                    "message": {
                        "content": "Respuesta simulada del modelo"
                    }
                }
            ]
        }

    monkeypatch.setattr(module, "send_request", fake_send_request)

    response = module.ask_model("Hola modelo")

    assert response == "Respuesta simulada del modelo"
