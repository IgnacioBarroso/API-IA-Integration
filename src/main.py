from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
import ollama
from dotenv import load_dotenv
import os
import openai

# Cargar variables de entorno
load_dotenv()

app = FastAPI(
    title="API IA Integration",
    description="API para integración con servicios de IA",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY_CREDITS = {os.getenv("OPENAI_API_KEY"): 5}

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Integración con IA"}

def verify_api_key(api_key: str = Header(...)):
    credits = API_KEY_CREDITS.get(api_key, 0)
    
    if credits <= 0:
        raise HTTPException(status_code=401, detail="No credits left")
    
    return api_key

@app.post("/generate")
async def generate(prompt: str, api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[api_key] -= 1
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
