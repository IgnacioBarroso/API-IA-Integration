import pytest
from fastapi.testclient import TestClient
from src.main import app
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Crear cliente de prueba
client = TestClient(app)

# Obtener API key para las pruebas
API_KEY = os.getenv("OPENAI_API_KEY")

def test_root_endpoint():
    """Prueba el endpoint raíz"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a la API de Integración con IA"}

def test_generate_endpoint_without_api_key():
    """Prueba el endpoint /generate sin API key"""
    response = client.post("/generate", json={"prompt": "Hola"})
    assert response.status_code == 422  # FastAPI validation error

def test_generate_endpoint_with_api_key():
    """Prueba el endpoint /generate con API key válida"""
    headers = {"api-key": API_KEY}
    response = client.post("/generate", json={"prompt": "Hola"}, headers=headers)
    assert response.status_code == 200
    assert "response" in response.json()

def test_generate_endpoint_with_invalid_api_key():
    """Prueba el endpoint /generate con API key inválida"""
    headers = {"api-key": "invalid_key"}
    response = client.post("/generate", json={"prompt": "Hola"}, headers=headers)
    assert response.status_code == 401
    assert response.json()["detail"] == "No credits left" 