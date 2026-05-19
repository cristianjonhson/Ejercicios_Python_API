"""
Pruebas unitarias para menu.py.

Valida que el menú principal tenga configuradas las opciones esperadas.
"""

from conftest import load_module_from_file


def test_main_contains_expected_examples():
    """
    Debe tener las opciones principales para ejecutar los ejercicios.
    """

    module = load_module_from_file("menu.py", "main_test_examples")

    assert "1" in module.EXAMPLES
    assert "2" in module.EXAMPLES
    assert "3" in module.EXAMPLES
    assert "4" in module.EXAMPLES

    assert module.EXAMPLES["1"]["file"] == "ejemplo.py"
    assert module.EXAMPLES["2"]["file"] == "ejemplo2.py"
    assert module.EXAMPLES["3"]["file"] == "ejemplo3.py"
    assert module.EXAMPLES["4"]["file"] == "ejemplo3-mejorado.py"


def test_read_option(monkeypatch):
    """
    Debe leer la opción ingresada por consola.
    """

    module = load_module_from_file("menu.py", "main_test_read_option")

    monkeypatch.setattr("builtins.input", lambda mensaje: "4")

    assert module.read_option() == "4"
