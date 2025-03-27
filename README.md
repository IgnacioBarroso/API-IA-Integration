# API IA Integration

API para integración con servicios de IA construida con FastAPI.

## Requisitos

- Python 3.8+
- pip (gestor de paquetes de Python)
- API Key de OpenAI

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd API-IA-Integration
```

2. Crear un entorno virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
   - Copiar el archivo `.env.example` a `.env`
   - Agregar tu API key de OpenAI en el archivo `.env`

## Uso

Para ejecutar la API en modo desarrollo:

```bash
uvicorn src.main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Documentación

- Documentación Swagger UI: `http://localhost:8000/docs`
- Documentación ReDoc: `http://localhost:8000/redoc`

## Endpoints

### GET /
Endpoint de bienvenida que devuelve un mensaje de saludo.

### POST /generate
Genera una respuesta usando la API de OpenAI.

**Headers requeridos:**
- `api-key`: Tu API key de OpenAI

**Body:**
```json
{
    "prompt": "Tu pregunta aquí"
}
```

**Respuesta:**
```json
{
    "response": "Respuesta generada por OpenAI"
}
```

## Pruebas

Para ejecutar las pruebas:

```bash
pytest test-api.py -v
```

Las pruebas incluyen:
- Verificación del endpoint raíz
- Validación de API key
- Manejo de errores
- Respuestas del endpoint /generate

## Estructura del Proyecto

```
API-IA-Integration/
├── src/                    # Código fuente de la aplicación
│   └── main.py            # Archivo principal de la API
├── api/                   # Entorno virtual de Python
├── .env                   # Variables de entorno (no incluido en git)
├── requirements.txt       # Dependencias del proyecto
├── test-api.py           # Pruebas de la API
└── README.md             # Documentación del proyecto
```

## Seguridad

- Las API keys deben mantenerse seguras y nunca compartirse
- El archivo `.env` está excluido del control de versiones
- Se recomienda usar variables de entorno en producción 