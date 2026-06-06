# Python APIs: Chuck Norris + OpenRouter

Proyecto educativo en Python para aprender a consumir APIs REST, procesar respuestas JSON, manejar errores HTTP, trabajar con variables de entorno y enviar prompts a un modelo de IA mediante OpenRouter.

El repositorio contiene ejemplos progresivos: primero se consume una API pública de chistes de Chuck Norris, luego se mejora el manejo de errores y traducción, y finalmente se integra una API de inteligencia artificial usando OpenRouter.

---

## Tabla de contenidos

- [Descripción del proyecto](#descripción-del-proyecto)
- [Objetivos de aprendizaje](#objetivos-de-aprendizaje)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración de variables de entorno](#configuración-de-variables-de-entorno)
- [Cómo ejecutar el proyecto](#cómo-ejecutar-el-proyecto)
- [Explicación de los archivos](#explicación-de-los-archivos)
- [Ejemplo de salida esperada](#ejemplo-de-salida-esperada)
- [Manejo de errores](#manejo-de-errores)
- [Buenas prácticas aplicadas](#buenas-prácticas-aplicadas)
- [Posibles mejoras](#posibles-mejoras)
- [Autor](#autor)

---

## Descripción del proyecto

Este proyecto muestra cómo consumir servicios externos desde Python utilizando la librería `requests`.

Incluye dos casos principales:

1. **Consumo de una API pública**
   Se obtiene un chiste aleatorio desde la API de Chuck Norris y se muestra su contenido en consola.

2. **Consumo de una API de IA**
   Se realiza una petición a OpenRouter para enviar un prompt y obtener una respuesta generada por un modelo de lenguaje.

Además, el proyecto incluye versiones mejoradas con manejo de errores, uso de funciones, clases personalizadas, logging, timeout y variables de entorno.

---

## Objetivos de aprendizaje

Con este proyecto podrás practicar:

- Consumo de APIs REST con Python.
- Uso de métodos HTTP como `GET` y `POST`.
- Lectura y procesamiento de respuestas JSON.
- Validación de códigos de estado HTTP.
- Manejo de errores con `try/except`.
- Uso de variables de entorno con `.env`.
- Envío de prompts a modelos de IA mediante OpenRouter.
- Separación básica de responsabilidades en funciones.
- Uso de `logging` para registrar información de ejecución.
- Buenas prácticas para proteger API Keys.

---

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal del proyecto |
| requests | Consumo de APIs HTTP |
| python-dotenv | Carga de variables desde archivo `.env` |
| deep-translator | Traducción de texto desde inglés a español |
| OpenRouter API | Acceso a modelos de inteligencia artificial |
| Chuck Norris API | API pública para obtener chistes aleatorios |
| Logging | Registro de eventos y errores |

---

## Estructura del proyecto

```bash
.
├── ejemplo.py
├── ejemplo2.py
├── ejemplo3.py
├── ejemplo3-mejorado.py
├── README.md
├── requirements.txt          # Opcional, recomendado
└── .env                      # No subir a GitHub
```

### Descripción rápida

| Archivo | Descripción |
|---|---|
| `ejemplo2.py` | Ejemplo inicial para consumir la API pública de Chuck Norris. |
| `ejemplo.py` | Versión mejorada del consumo de Chuck Norris API con traducción, `dataclass`, logging y manejo de errores. |
| `ejemplo3.py` | Ejemplo de consumo de OpenRouter usando variables de entorno desde `.env`. |
| `ejemplo3-mejorado.py` | Versión más estructurada para consumir OpenRouter usando funciones, excepciones personalizadas y logging. |

---

## Requisitos previos

Antes de ejecutar el proyecto necesitas tener instalado:

- Python 3.10 o superior.
- pip.
- Acceso a internet.
- Una API Key de OpenRouter, solo para ejecutar los ejemplos relacionados con IA.

Puedes verificar tu versión de Python con:

```bash
python3 --version
```

O en Windows:

```bash
python --version
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

Si aún no tienes el proyecto en GitHub, entra directamente a la carpeta donde están los archivos `.py`.

---

### 2. Crear un entorno virtual

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Instalar dependencias

Puedes instalar las dependencias manualmente:

```bash
pip install requests python-dotenv deep-translator
```

O crear un archivo `requirements.txt` con este contenido:

```txt
requests
python-dotenv
deep-translator
```

Luego instala todo con:

```bash
pip install -r requirements.txt
```

---

## Configuración de variables de entorno

Para ejecutar los ejemplos de OpenRouter, crea un archivo `.env` en la raíz del proyecto.

```env
OPENROUTER_API_KEY=tu_api_key_aqui
OPENROUTER_URL=https://openrouter.ai/api/v1/chat/completions
OPENROUTER_MODEL=openai/gpt-chat-latest
OPENROUTER_REFERER=https://mi-sitio.cl
OPENROUTER_APP_NAME=Clase APIs IA
TIMEOUT_SECONDS=30
MAX_TOKENS=300
```

### Importante

No subas el archivo `.env` a GitHub porque contiene información sensible como API Keys.

Agrega este archivo `.gitignore`:

```gitignore
.venv/
.env
__pycache__/
*.pyc
```

---

## Cómo ejecutar el proyecto

### Ejecutar ejemplo básico de API pública

```bash
python ejemplo2.py
```

Este script consume la API pública de Chuck Norris, imprime el código de estado HTTP y muestra el chiste recibido.

---

### Ejecutar ejemplo mejorado de Chuck Norris API

```bash
python ejemplo.py
```

Este script obtiene un chiste aleatorio, lo traduce al español y muestra la fuente original.

---

### Ejecutar ejemplo con OpenRouter usando `.env`

```bash
python ejemplo3.py
```

Este script carga las variables desde el archivo `.env`, envía un prompt a OpenRouter y muestra la respuesta generada por el modelo.

---

### Ejecutar versión mejorada de OpenRouter

```bash
python ejemplo3-mejorado.py
```

Esta versión organiza el código en funciones, valida la API Key, construye headers y payload por separado, maneja errores HTTP y extrae la respuesta del modelo.

> Nota: se recomienda evitar dejar API Keys directamente en el código. Lo ideal es usar siempre variables de entorno o un archivo `.env` excluido de Git.

---

## Explicación de los archivos

### `ejemplo2.py`

Archivo introductorio que muestra el flujo mínimo para consumir una API:

```python
respuesta = requests.get(url)
datos = respuesta.json()
print(datos["value"])
```

Es útil para entender:

- Cómo hacer una petición `GET`.
- Cómo revisar el código de estado.
- Cómo convertir una respuesta a JSON.
- Cómo acceder a campos específicos del diccionario.

---

### `ejemplo.py`

Versión más profesional del consumo de la Chuck Norris API.

Incluye:

- Constantes para URL y timeout.
- `dataclass` para representar el chiste.
- Excepción personalizada `JokeAPIError`.
- Traducción automática con `GoogleTranslator`.
- Manejo de errores para timeout, errores HTTP, conexión, JSON inválido y claves faltantes.
- Función `main()` como punto de entrada.

---

### `ejemplo3.py`

Script para consumir OpenRouter cargando configuración desde `.env`.

Incluye:

- Lectura de variables de entorno.
- Validación de configuración obligatoria.
- Construcción de headers HTTP.
- Construcción del payload con mensajes `system` y `user`.
- Envío de petición `POST`.
- Extracción del contenido generado por el modelo.

---

### `ejemplo3-mejorado.py`

Versión estructurada del ejemplo de OpenRouter.

Incluye:

- Función `get_api_key()`.
- Función `build_headers()`.
- Función `build_payload()`.
- Función `send_request()`.
- Función `extract_model_response()`.
- Función `ask_model()`.
- Excepción personalizada `OpenRouterAPIError`.
- Logging para registrar el estado de la ejecución.

Esta versión es la más cercana a una estructura reutilizable para futuros proyectos.

---

## Ejemplo de salida esperada

### Para `ejemplo.py`

```bash
INFO - Código de estado recibido: 200
Chiste original:
Chuck Norris can divide by zero.

Chiste traducido al español:
Chuck Norris puede dividir por cero.

Fuente: https://api.chucknorris.io/jokes/...
```

### Para `ejemplo3.py` o `ejemplo3-mejorado.py`

```bash
Código de estado: 200
Respuesta del modelo:
Una API es un mecanismo que permite que dos aplicaciones se comuniquen entre sí.
Define reglas para enviar solicitudes y recibir respuestas.
Se usa para integrar servicios, datos o funcionalidades externas.
```

---

## Manejo de errores

El proyecto contempla errores comunes al consumir APIs:

| Error | Posible causa | Solución |
|---|---|---|
| `Timeout` | La API tarda demasiado en responder | Aumentar el timeout o intentar más tarde |
| `HTTPError` | La API responde con error 4xx o 5xx | Revisar URL, API Key o permisos |
| `RequestException` | Problema de conexión | Verificar internet o disponibilidad del servicio |
| `KeyError` | La respuesta JSON no tiene el campo esperado | Revisar estructura de la respuesta |
| `ValueError` | JSON inválido o configuración faltante | Validar `.env` y respuesta recibida |

---

## Buenas prácticas aplicadas

- Uso de entorno virtual para aislar dependencias.
- Separación de configuración mediante variables de entorno.
- Uso de `timeout` en peticiones HTTP.
- Manejo de excepciones específicas.
- Uso de constantes para URLs y configuración.
- Uso de funciones pequeñas y reutilizables.
- Uso de `logging` en lugar de solo `print` para eventos internos.
- Protección de credenciales mediante `.env` y `.gitignore`.

---

## Posibles mejoras

Algunas mejoras que se podrían agregar al proyecto:

- Crear un menú interactivo para elegir qué ejemplo ejecutar.
- Permitir que el usuario escriba su propio prompt por consola.
- Guardar las respuestas en un archivo `.txt` o `.json`.
- Agregar pruebas unitarias con `pytest`.
- Crear una interfaz web simple con Streamlit o Flask.
- Validar variables de entorno con una función dedicada.
- Crear un módulo `services/` para separar lógica de APIs.
- Agregar tipado más estricto y documentación de funciones.
- Preparar el proyecto para publicarlo como repositorio educativo en GitHub.

---

## Autor

**Cristian Jonhson Alvarez**
Proyecto educativo para practicar consumo de APIs REST, manejo de JSON, variables de entorno e integración básica con modelos de IA usando Python.

---

## Licencia

Este proyecto puede utilizarse con fines educativos y de práctica personal.
