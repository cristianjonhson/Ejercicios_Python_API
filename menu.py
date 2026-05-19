"""
Menú interactivo para ejecutar ejercicios de Python sobre consumo de APIs.

Este archivo muestra un menú interactivo para ejecutar los ejercicios
de consumo de APIs en Python.
"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


EXAMPLES = {
    "1": {
        "name": "Ejemplo 1 - Chuck Norris API mejorado",
        "file": "ejemplo.py",
        "description": "Consume la API de Chuck Norris y muestra un chiste aleatorio."
    },
    "2": {
        "name": "Ejemplo 2 - Chuck Norris API exploración JSON",
        "file": "ejemplo2.py",
        "description": "Consume la API y muestra información del JSON recibido."
    },
    "3": {
        "name": "Ejemplo 3 - OpenRouter básico con .env",
        "file": "ejemplo3.py",
        "description": "Envía un prompt a OpenRouter usando variables de entorno."
    },
    "4": {
        "name": "Ejemplo 4 - OpenRouter mejorado",
        "file": "ejemplo3-mejorado.py",
        "description": "Ejecuta la versión mejorada con funciones, logging y manejo de errores."
    },
     "5": {
        "name": "Ejemplo 5 - OpenRouter mejorado con prompt personalizado",
        "file": "ejemplo3-mejorado.py",
        "description": "Permite escribir un prompt por consola y enviarlo a OpenRouter."
    }
}


def show_header() -> None:
    """Muestra el encabezado del programa."""

    print("\n===================================")
    print("   PYTHON APIs: CHUCK + OPENROUTER")
    print("===================================")


def show_menu() -> None:
    """Muestra el menú principal con los ejercicios disponibles."""

    show_header()

    for option, example in EXAMPLES.items():
        print(f"{option}. {example['name']}")
        print(f"   {example['description']}")

    print("0. Salir")
    print("===================================")


def run_example(file_name: str) -> None:
    """
    Ejecuta un archivo Python usando el mismo intérprete activo.

    Args:
        file_name: Nombre del archivo Python que se ejecutará.
    """

    file_path = BASE_DIR / file_name

    if not file_path.exists():
        print(f"\nError: No se encontró el archivo '{file_name}'.")
        print("Verifica que el archivo exista en la raíz del proyecto.")
        return

    print(f"\nEjecutando: {file_name}")
    print("-----------------------------------")

    try:
        subprocess.run(
            [sys.executable, str(file_path)],
            check=True
        )

    except subprocess.CalledProcessError as error:
        print("\nEl script terminó con un error.")
        print(f"Código de salida: {error.returncode}")

    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")


def read_option() -> str:
    """
    Lee la opción ingresada por el usuario.

    Returns:
        Opción seleccionada como texto.
    """

    return input("\nSelecciona una opción: ").strip()


def main() -> None:
    """Función principal del programa."""

    while True:
        show_menu()

        option = read_option()

        if option == "0":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break

        example = EXAMPLES.get(option)

        if not example:
            print("\nOpción inválida. Intenta nuevamente.")
            continue

        run_example(example["file"])

        input("\nPresiona Enter para volver al menú...")


if __name__ == "__main__":
    main()
