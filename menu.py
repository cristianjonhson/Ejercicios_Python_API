"""
Menú interactivo para ejecutar ejercicios de Python sobre consumo de APIs.

Este archivo permite elegir qué ejemplo ejecutar sin tener que escribir
manualmente el nombre de cada script en la terminal.
"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


EXAMPLES = {
    "1": {
        "name": "Ejemplo 1 - Chuck Norris API básico",
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
    }
}


def show_menu() -> None:
    """Muestra el menú principal."""

    print("\n===================================")
    print("   MENÚ DE EJERCICIOS PYTHON API")
    print("===================================")

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
        print("Verifica que este menú esté en la misma carpeta que los ejemplos.")
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


def main() -> None:
    """Función principal del menú interactivo."""

    while True:
        show_menu()

        option = input("\nSelecciona una opción: ").strip()

        if option == "0":
            print("\nSaliendo del menú. ¡Hasta luego!")
            break

        example = EXAMPLES.get(option)

        if not example:
            print("\nOpción inválida. Intenta nuevamente.")
            continue

        run_example(example["file"])

        input("\nPresiona Enter para volver al menú...")


if __name__ == "__main__":
    main()
