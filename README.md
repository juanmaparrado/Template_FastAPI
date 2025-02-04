# FastAPI Modular Template

Este repositorio proporciona una estructura modular para el desarrollo de aplicaciones con FastAPI. Está diseñado para facilitar la organización del código, mejorar la escalabilidad y permitir un rápido desarrollo con herramientas preconfiguradas.

## Características

- **Estructura modular** con soporte para routers.
- **Logger preconfigurado** listo para usar.
- **Limitador de peticiones** con `slowapi`.
- **Archivo de constantes** para una mejor gestión de configuraciones.
- **Soporte para Docker** con `Dockerfile` y `docker-compose` optimizados para desarrollo.
- **Carpeta `models/`** para modelos de Pydantic.
- **Carpeta `connection/`** para gestionar conexiones a bases de datos y otros servicios externos/internos.
- **Carpeta `routers/`** para definir las rutas de la API.
- **Carpeta `services/`** para la lógica de negocio.
- **Carpeta `utils/`** para utilidades y funciones comunes.
- **Carpeta `configuration/`** para configuraciones y constantes.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```
2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta el servidor:
   ```bash
   uvicorn app:app --reload
   ```

## Uso con Docker

Para ejecutar la aplicación con Docker:
```bash
docker-compose up --build
```

## Uso del Logger

El logger ya está configurado y listo para usar en cualquier archivo. Por defecto, está en nivel de `DEBUG`, pero se puede modificar fácilmente para producción ajustando la configuración en `logger_config.py`:


El logger ya está configurado y listo para usar en cualquier archivo:

```python
from configuration.logger_config import logger

logger.info("Mensaje de información")
logger.error("Mensaje de error")
```
## Uso del Limitador con SlowAPI

El limitador de peticiones `slowapi` está configurado y se puede usar en los endpoints mediante el decorador `@limiter.limit`. 
Ejemplo de uso en un router:
```python
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import APIRouter, Depends

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()

@router.get("/rate-limited-endpoint")
@limiter.limit("5/minute")
def limited_route():
    return {"message": "Este endpoint está limitado a 5 solicitudes por minuto"}
```

## Estructura del Proyecto

```
.
├── app.py                # Punto de entrada de la aplicación
├── configuration/
│   ├── logger_config.py  # Configuración del logger
│   ├── constants.py      # Archivo de constantes
│
├── routers/
│   ├── example_router.py # Ejemplo de router modular
│
├── models/
│   ├── example_model.py  # Modelos de Pydantic
│
├── connection/
│   ├── database.py       # Conexión a bases de datos u otros servicios
│
├── services/
│   ├── example_service.py # Lógica de negocio
│
├── utils/
│   ├── example_util.py    # Funciones auxiliares
│
├── requirements.txt      # Dependencias del proyecto
├── Dockerfile            # Configuración para Docker
├── docker-compose.yml    # Orquestación de contenedores
└── README.md             # Documentación del proyecto
```

