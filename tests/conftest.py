"""
Configuración común para las pruebas unitarias.

Permite importar archivos Python que tienen nombres con guion,
por ejemplo: ejemplo3-mejorado.py.
"""

import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module_from_file(file_name: str, module_name: str):
    """
    Carga un módulo Python desde un archivo específico del proyecto.
    """

    file_path = PROJECT_ROOT / file_name

    assert file_path.exists(), f"No se encontró el archivo requerido: {file_path}"

    spec = spec_from_file_location(module_name, file_path)

    assert spec is not None
    assert spec.loader is not None

    module = module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module
