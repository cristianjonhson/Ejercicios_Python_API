# Python APIs: Chuck Norris + OpenRouter

Proyecto educativo en Python para aprender a consumir APIs REST, procesar respuestas JSON, manejar errores HTTP, trabajar con variables de entorno y enviar prompts personalizados a un modelo de IA mediante OpenRouter.

El repositorio contiene ejemplos progresivos: primero se consume una API pública de chistes de Chuck Norris, luego se mejora el manejo de errores y traducción, finalmente se integra una API de inteligencia artificial usando OpenRouter, se permite ingresar prompts por consola y se agrega un menú interactivo para ejecutar los ejercicios.

---

## Tabla de contenidos

- [Descripción del proyecto](#descripción-del-proyecto)
- [Objetivos de aprendizaje](#objetivos-de-aprendizaje)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso de entorno virtual para aislar dependencias](#uso-de-entorno-virtual-para-aislar-dependencias)
- [Configuración de variables de entorno](#configuración-de-variables-de-entorno)
- [Cómo ejecutar el proyecto](#cómo-ejecutar-el-proyecto)
- [Menú interactivo](#menú-interactivo)
- [Explicación de los archivos](#explicación-de-los-archivos)
- [Ejemplo de salida esperada](#ejemplo-de-salida-esperada)
- [Manejo de errores](#manejo-de-errores)
- [Buenas prácticas aplicadas](#buenas-prácticas-aplicadas)
- [Posibles mejoras](#posibles-mejoras)
- [Autor](#autor)
- [Licencia](#licencia)

---

## Descripción del proyecto

Este proyecto muestra cómo consumir servicios externos desde Python utilizando la librería `requests`.

Incluye cuatro casos principales:

1. **Consumo de una API pública**
   Se obtiene un chiste aleatorio desde la API de Chuck Norris y se muestra su contenido en consola.

2. **Consumo mejorado de una API pública**
   Se obtiene un chiste aleatorio, se traduce al español y se manejan errores comunes al consumir APIs.

3. **Consumo de una API de IA**
   Se realiza una petición a OpenRouter para enviar un prompt y obtener una respuesta generada por un modelo de lenguaje.

4. **Prompt personalizado desde consola**
   En la versión mejorada de OpenRouter, el usuario puede escribir su propio prompt desde la terminal antes de enviar la solicitud al modelo.

5. **Ejecución mediante menú interactivo**
   Se agrega un archivo `menu.py` que permite elegir desde la terminal qué ejemplo ejecutar, sin escribir manualmente el nombre de cada script.

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
- Entrada de datos por consola con `input()`.
- Validación de prompts ingresados por el usuario.
- Separación básica de responsabilidades en funciones.
- Uso de `logging` para registrar información de ejecución.
- Buenas prácticas para proteger API Keys.
- Ejecución de scripts Python mediante un menú interactivo.
- Uso de `subprocess` y `sys.executable` para ejecutar archivos desde otro script.
- Uso de entorno virtual para aislar dependencias del proyecto.

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
| subprocess | Ejecución de scripts Python desde el menú interactivo |
| pathlib | Manejo de rutas de archivos de forma portable |
| venv | Creación de entorno virtual para aislar dependencias |

---

## Estructura del proyecto

```bash
.
├── .gitignore
├── .env.example                   # Plantilla de variables de entorno
├── ejemplo.py
├── ejemplo2.py
├── ejemplo3.py
├── ejemplo3-mejorado.py
├── menu.py
├── README.md
└── requirements.txt
```

### Archivos locales no versionados

Estos archivos o carpetas se usan localmente, pero no deben subirse a GitHub:

```bash
.venv/                             # Entorno virtual local
.env                               # Variables de entorno sensibles
__pycache__/                       # Caché generado por Python
*.pyc                              # Archivos compilados de Python
```

### Descripción rápida

| Archivo                | Descripción                                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| `ejemplo2.py`          | Ejemplo inicial para consumir la API pública de Chuck Norris.                                              |
| `ejemplo.py`           | Versión mejorada del consumo de Chuck Norris API con traducción, `dataclass`, logging y manejo de errores. |
| `ejemplo3.py`          | Ejemplo de consumo de OpenRouter usando variables de entorno desde `.env`.                                 |
| `ejemplo3-mejorado.py` | Versión más estructurada para consumir OpenRouter usando funciones, excepciones personalizadas y logging.  |
| `ejemplo3-mejorado_prompt.py` | Versión más estructurada para consumir OpenRouter usando funciones, excepciones personalizadas, logging y prompt ingresado por consola. |
| `menu.py`              | Menú interactivo para elegir y ejecutar los ejemplos desde la terminal.                                    |
| `.env.example`         | Plantilla de variables de entorno sin credenciales reales.                                                 |
| `requirements.txt`     | Lista de dependencias necesarias para ejecutar el proyecto.                                                |
| `.gitignore`           | Archivos y carpetas que no deben subirse al repositorio.                                                   |

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

## Uso de entorno virtual para aislar dependencias

Se recomienda ejecutar este proyecto dentro de un entorno virtual de Python.

Un entorno virtual permite aislar las dependencias del proyecto para evitar conflictos con otras instalaciones de Python en el sistema. Esto es especialmente útil cuando trabajamos con librerías externas como `requests`, `python-dotenv` y `deep-translator`.

### Crear entorno virtual

En macOS o Linux:

```bash
python3 -m venv .venv
```

En Windows:

```bash
python -m venv .venv
```

### Activar entorno virtual

En macOS o Linux:

```bash
source .venv/bin/activate
```

En Windows:

```bash
.venv\Scripts\activate
```

Cuando el entorno virtual está activo, la terminal debería mostrar algo similar a:

```bash
(.venv) admin@admins-MacBook-Pro Ejercicios_Python_API %
```

### Instalar dependencias dentro del entorno virtual

Puedes instalar las dependencias manualmente:

```bash
pip install requests python-dotenv deep-translator
```

O instalar todo desde `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Verificar dependencias instaladas

```bash
pip list
```

### Guardar dependencias del proyecto

Si instalas nuevas librerías, puedes actualizar el archivo `requirements.txt` con:

```bash
pip freeze > requirements.txt
```

### Desactivar entorno virtual

Cuando termines de trabajar en el proyecto, puedes desactivar el entorno virtual con:

```bash
deactivate
```

> Importante: la carpeta `.venv/` no debe subirse a GitHub. Por eso debe estar incluida en el archivo `.gitignore`.

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

También se recomienda crear un archivo `.env.example` para documentar las variables necesarias sin exponer credenciales reales:

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

Agrega este contenido al archivo `.gitignore`:

```gitignore
.venv/
.env
__pycache__/
*.pyc
.DS_Store
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

Este script carga las variables desde el archivo `.env`, envía un prompt fijo a OpenRouter y muestra la respuesta generada por el modelo.

---

### Ejecutar versión mejorada de OpenRouter con prompt personalizado

```bash
python ejemplo3-mejorado.py
```

Esta versión organiza el código en funciones, valida la API Key, construye headers y payload por separado, maneja errores HTTP, solicita un prompt por consola y extrae la respuesta del modelo.

Al ejecutar este archivo, el programa pedirá un prompt:

```text
Escribe el prompt que quieres enviar a OpenRouter.
Ejemplo: Explica qué es una API en 3 líneas.
Para cancelar, presiona Enter sin escribir nada.

Prompt:
```

Ejemplo de prompt ingresado por el usuario:

```text
Dame 5 buenas prácticas para consumir APIs REST en Python
```

---

### Ejecutar el menú interactivo

```bash
python menu.py
```

El menú permite seleccionar qué ejemplo ejecutar desde una lista de opciones.

> Nota: se recomienda evitar dejar API Keys directamente en el código. Lo ideal es usar siempre variables de entorno o un archivo `.env` excluido de Git.

---

## Menú interactivo

El archivo `menu.py` permite ejecutar los ejercicios desde una sola entrada principal.

Al ejecutar:

```bash
python menu.py
```

Se mostrará un menú similar a este:

```text
===================================
   MENÚ DE EJERCICIOS PYTHON API
===================================
1. Ejemplo 1 - Chuck Norris API básico
2. Ejemplo 2 - Chuck Norris API exploración JSON
3. Ejemplo 3 - OpenRouter básico con .env
4. Ejemplo 4 - OpenRouter mejorado con prompt personalizado
0. Salir
===================================
```

El usuario puede ingresar el número de la opción deseada y el menú ejecutará el archivo correspondiente.

Este archivo utiliza:

- `pathlib` para ubicar los archivos dentro del proyecto.
- `subprocess.run()` para ejecutar cada script.
- `sys.executable` para usar el mismo intérprete de Python del entorno virtual activo.
- Validación básica para detectar si un archivo no existe.
- Manejo de errores cuando un script termina con un código de salida distinto de cero.

Ejemplo de uso:

```bash
python menu.py
```

Luego seleccionar:

```text
4
```

Para ejecutar:

```bash
ejemplo3-mejorado.py
```

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

* Cómo hacer una petición `GET`.
* Cómo revisar el código de estado.
* Cómo convertir una respuesta a JSON.
* Cómo acceder a campos específicos del diccionario.

---

### `ejemplo.py`

Versión más profesional del consumo de la Chuck Norris API.

Incluye:

* Constantes para URL y timeout.
* `dataclass` para representar el chiste.
* Excepción personalizada `JokeAPIError`.
* Traducción automática con `GoogleTranslator`.
* Manejo de errores para timeout, errores HTTP, conexión, JSON inválido y claves faltantes.
* Función `main()` como punto de entrada.

---

### `ejemplo3.py`

Script para consumir OpenRouter cargando configuración desde `.env`.

Incluye:

* Lectura de variables de entorno.
* Validación de configuración obligatoria.
* Construcción de headers HTTP.
* Construcción del payload con mensajes `system` y `user`.
* Envío de petición `POST`.
* Extracción del contenido generado por el modelo.

---

### `ejemplo3-mejorado.py`

Versión estructurada del ejemplo de OpenRouter.

Incluye:

* Función `get_api_key()`.
* Función `build_headers()`.
* Función `build_payload()`.
* Función `send_request()`.
* Función `extract_model_response()`.
* Función `ask_model()`.
* Excepción personalizada `OpenRouterAPIError`.
* Logging para registrar el estado de la ejecución.

Esta versión es la más cercana a una estructura reutilizable para futuros proyectos.

---

### `ejemplo3-mejorado_prompt.py`

Versión estructurada del ejemplo de OpenRouter.

Incluye:

* Función `get_api_key()`.
* Función `validate_config()`.
* Función `build_headers()`.
* Función `build_payload()`.
* Función `send_request()`.
* Función `extract_model_response()`.
* Función `ask_model()`.
* Función `read_user_prompt()` para solicitar un prompt desde consola.
* Excepción personalizada `OpenRouterAPIError`.
* Logging para registrar el estado de la ejecución.

Esta versión permite que el usuario escriba su propio prompt en la terminal antes de enviar la solicitud a OpenRouter.

---

### `menu.py`

Archivo que funciona como punto de entrada interactivo del proyecto.

Permite ejecutar los diferentes ejemplos sin escribir manualmente el nombre del archivo en la terminal.

Incluye:

* Diccionario `EXAMPLES` con las opciones disponibles.
* Función `show_menu()` para mostrar las opciones.
* Función `run_example()` para ejecutar el archivo seleccionado.
* Función `main()` con un ciclo `while True` para mantener activo el menú hasta que el usuario seleccione salir.
* Validación de opciones inválidas.
* Manejo de interrupción con `KeyboardInterrupt`.

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

### Para `ejemplo3-mejorado_prompt.py`

```text
Escribe el prompt que quieres enviar a OpenRouter.
Ejemplo: Explica qué es una API en 3 líneas.
Para cancelar, presiona Enter sin escribir nada.

Prompt: Dame 5 buenas prácticas para consumir APIs REST en Python

INFO - Código de estado recibido: 200

Respuesta del modelo:
-----------------------------------
1. Usa timeouts en tus peticiones.
2. Maneja errores HTTP con excepciones.
3. Protege tus API Keys usando variables de entorno.
4. Valida la estructura de las respuestas JSON.
5. Separa la lógica de consumo de API en funciones reutilizables.
```

### Para `menu.py`

```bash
===================================
   MENÚ DE EJERCICIOS PYTHON API
===================================
1. Ejemplo 1 - Chuck Norris API básico
2. Ejemplo 2 - Chuck Norris API exploración JSON
3. Ejemplo 3 - OpenRouter básico con .env
4. Ejemplo 4 - OpenRouter mejorado
5. Ejemplo 5 - OpenRouter mejorado con prompt personalizado
0. Salir
===================================

Selecciona una opción: 5

Ejecutando: ejemplo3-mejorado_prompt.py
-----------------------------------

Escribe el prompt que quieres enviar a OpenRouter.
Ejemplo: Explica qué es una API en 3 líneas.
Para cancelar, presiona Enter sin escribir nada.

Prompt:
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
| `OpenRouterAPIError` | Configuración faltante, prompt vacío o error controlado del consumo de OpenRouter | Revisar `.env`, API Key o ingresar un prompt válido |
| `CalledProcessError` | Un script ejecutado desde `menu.py` terminó con error | Revisar el mensaje mostrado por el script seleccionado |

---

## Buenas prácticas aplicadas

* Uso de entorno virtual para aislar dependencias.
* Separación de configuración mediante variables de entorno.
* Uso de `timeout` en peticiones HTTP.
* Manejo de excepciones específicas.
* Uso de constantes para URLs y configuración.
* Uso de funciones pequeñas y reutilizables.
* Uso de `logging` en lugar de solo `print` para eventos internos.
* Protección de credenciales mediante `.env` y `.gitignore`.
* Uso de `.env.example` para documentar variables sin exponer secretos.
* Menú interactivo como punto de entrada para mejorar la experiencia de uso.
* Uso de `sys.executable` para respetar el entorno virtual activo.
* Uso de `requirements.txt` para instalar dependencias de forma reproducible.
* Lectura de prompts desde consola para hacer el ejemplo de IA más interactivo.
* Validación de entrada vacía antes de enviar una solicitud al modelo.

---

## Posibles mejoras

Algunas mejoras que se podrían agregar al proyecto:

* Guardar las respuestas en un archivo `.txt` o `.json`.
* Agregar pruebas unitarias con `pytest`.
* Crear una interfaz web simple con Streamlit o Flask.
* Validar variables de entorno con una función dedicada.
* Crear un módulo `services/` para separar lógica de APIs.
* Agregar tipado más estricto y documentación de funciones.
* Preparar el proyecto para publicarlo como repositorio educativo en GitHub.
* Permitir que el menú ejecute solo ejemplos locales si no existe API Key.
* Agregar una opción al menú para verificar configuración del `.env`.

---

## Autor

**Cristian Jonhson Alvarez**
Proyecto educativo para practicar consumo de APIs REST, manejo de JSON, variables de entorno e integración básica con modelos de IA usando Python.

---

## Licencia

Este proyecto puede utilizarse con fines educativos y de práctica personal.
