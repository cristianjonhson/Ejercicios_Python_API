## Pruebas unitarias con pytest

El proyecto incluye pruebas unitarias con `pytest` para validar la lógica principal sin consumir APIs reales.

Las pruebas usan `monkeypatch` para simular variables de entorno, entradas por consola y respuestas HTTP. De esta forma, los tests no dependen de internet, no consumen tokens de OpenRouter y se pueden ejecutar de forma segura en local o en GitHub Actions.

### Estructura de pruebas

```bash
.
├── pytest.ini
├── requirements-dev.txt
└── tests/
    ├── conftest.py
    ├── test_chuck_norris_api.py
    ├── test_openrouter_api.py
    └── test_main.py
```

### Instalar dependencias de desarrollo

```bash
pip install -r requirements-dev.txt
```

También puedes instalar `pytest` directamente:

```bash
pip install pytest
```

### Ejecutar todas las pruebas

```bash
pytest
```

O con salida más detallada:

```bash
pytest -v
```

### Ejecutar un archivo de pruebas específico

```bash
pytest tests/test_openrouter_api.py -v
```

### Qué validan las pruebas

| Archivo de prueba | Qué valida |
|---|---|
| `test_chuck_norris_api.py` | Consumo exitoso simulado de Chuck Norris API y manejo de timeout. |
| `test_openrouter_api.py` | Lectura de API Key, construcción de headers, payload, prompt por consola y respuesta simulada del modelo. |
| `test_main.py` | Configuración de opciones del menú principal y lectura de opción por consola. |

### Importante

Las pruebas no llaman a la API real de OpenRouter ni a la API real de Chuck Norris. Esto se hace para mantener las pruebas rápidas, estables y seguras.
