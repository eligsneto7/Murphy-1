from pathlib import Path
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from app.astro_data import (
    get_astronomical_coincidences
)
from app.modern_sky_renderer import ModernSkyRenderer
from app.zenith_calculator import find_zenith_star, load_hipparcos_data
from app.constellation_data import get_constellation_data
from skyfield.api import load, wgs84
from skyfield.units import Angle
from skyfield.timelib import Time
from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN
from skyfield.data import hipparcos
from skyfield.units import Distance
import math
CONSTELLATIONS = get_constellation_data()
from app.star_data_extended import NAMED_STARS, find_nearest_named_star
from app.astro_data import ASTRONOMICAL_EVENTS
import httpx
import asyncio

app = FastAPI(title="Murphy-1", description="Calculadora de Estrelas Zenitais com TARS")

# Adicionar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuração de templates e arquivos estáticos
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Debug: verificar caminhos
print(f"🔍 BASE_DIR: {BASE_DIR}")
print(f"🔍 Static directory: {BASE_DIR / 'static'}")
print(f"🔍 Templates directory: {BASE_DIR / 'templates'}")
print(f"🔍 Static files exist: {(BASE_DIR / 'static').exists()}")
print(f"🔍 CSS exists: {(BASE_DIR / 'static' / 'css' / 'style.css').exists()}")
print(f"🔍 Templates directory exists: {(BASE_DIR / 'templates').exists()}")
print(f"🔍 Index.html exists: {(BASE_DIR / 'templates' / 'index.html').exists()}")

# Listar arquivos no diretório de templates
if (BASE_DIR / 'templates').exists():
    print("🔍 Template files:")
    for file in (BASE_DIR / 'templates').iterdir():
        print(f"   - {file.name}")

# Montar arquivos estáticos
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Middleware de debug
@app.middleware("http")
async def debug_middleware(request: Request, call_next):
    print(f"📍 Request: {request.method} {request.url.path}")
    print(f"📍 Headers: {dict(request.headers)}")
    
    response = await call_next(request)
    print(f"📍 Response: {response.status_code}")
    
    return response

# Lazy loading - criar objetos apenas quando necessário
modern_sky_renderer_instance = None

def get_modern_sky_renderer():
    global modern_sky_renderer_instance
    if modern_sky_renderer_instance is None:
        modern_sky_renderer_instance = ModernSkyRenderer()
    return modern_sky_renderer_instance

# Carregar dados do Hipparcos
df = load_hipparcos_data()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Página inicial com formulário de entrada"""
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

async def geocode_location(city: str, country: str) -> tuple[float, float]:
    """
    Convert city and country to latitude and longitude using Nominatim API
    """
    try:
        # Format the query
        query = f"{city}, {country}"
        
        # Use Nominatim (OpenStreetMap) API - free and no API key required
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": query,
            "format": "json",
            "limit": 1,
            "addressdetails": 1
        }
        
        headers = {
            "User-Agent": "Murphy-1-Stellar-Calculator/1.0 (astronomical-calculator)"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            
            if not data:
                raise ValueError(f"Localização não encontrada: {query}")
            
            location = data[0]
            latitude = float(location["lat"])
            longitude = float(location["lon"])
            
            print(f"🌍 Geocoded {query} -> {latitude}, {longitude}")
            return latitude, longitude
            
    except Exception as e:
        print(f"❌ Erro na geocodificação: {e}")
        # Fallback para coordenadas padrão (São Paulo, Brasil)
        print("🔄 Usando coordenadas padrão de São Paulo")
        return -23.5505, -46.6333

@app.post("/test-geocode")
async def test_geocode(
    city: str = Form(...),
    country: str = Form(...)
):
    """Test endpoint for geocoding only"""
    try:
        latitude, longitude = await geocode_location(city, country)
        return {
            "status": "success",
            "city": city,
            "country": country,
            "latitude": latitude,
            "longitude": longitude
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(
    request: Request,
    birth_date: str = Form(...),
    birth_time: str = Form(...),
    city: str = Form(...),
    country: str = Form(...)
):
    """Calcula a estrela zenital e retorna o resultado"""
    try:
        # Convert city and country to coordinates
        latitude, longitude = await geocode_location(city, country)
        
        print(f"🗺️ Processando: {city}, {country} -> {latitude}, {longitude}")
        
        # Usar a função find_zenith_star existente
        result = find_zenith_star(birth_date, birth_time, latitude, longitude)
        
        # Add location info to result
        result['location'] = {
            'city': city,
            'country': country,
            'latitude': latitude,
            'longitude': longitude
        }
        
        # Skip sky rendering for now to avoid the error
        result.update({
            'stars': [
                {
                    'name': result['name'],
                    'ra': result['ra_degrees'],
                    'dec': result['dec_degrees'],
                    'magnitude': result['magnitude'],
                    'isZenith': True,
                    'x': 0,
                    'y': 0,
                    'size': 20,
                    'color': '#FFD700'
                }
            ],
            'constellation_lines': [],
            'constellation_name': result.get('constellation', 'N/A'),
            'total_stars': 1
        })
        
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "data": {
                    "star": {
                        "name": result['name'],
                        "constellation": result.get('constellation', 'N/A'),
                        "magnitude": result['magnitude'],
                        "distance_ly": result['distance_ly'],
                        "spectral_class": result['spectral_class'],
                        "curiosities": {
                            "age_formatted": f"{result.get('age_billion_years', 5.0)} bilhões de anos",
                            "birth_era": "Era Pré-Solar",
                            "temporal_message": f"Esta estrela brilha há muito mais tempo que nosso Sol",
                            "history": result.get('history', f"{result['name']} é uma estrela fascinante com características únicas"),
                            "fun_facts": [
                                f"Está a {result['distance_ly']} anos-luz de distância",
                                f"Sua magnitude aparente é {result['magnitude']}",
                                f"Pertence à classe espectral {result['spectral_class']}"
                            ],
                            "timeline_comparison": {
                                "comparisons": [
                                    f"Quando {result['name']} nasceu, a Terra ainda não existia",
                                    f"A luz que vemos hoje saiu da estrela há {result['distance_ly']} anos"
                                ],
                                "era_when_light_started": f"Há {result['distance_ly']} anos"
                            }
                        }
                    },
                    "birth_info": {
                        "date": birth_date,
                        "time": birth_time,
                        "location": f"{city}, {country}"
                    },
                    "cosmic_message": f"No momento do seu nascimento, {result['name']} estava no zênite, brilhando diretamente sobre você. Esta estrela da constelação de {result.get('constellation', 'N/A')} será sua companheira cósmica eterna.",
                    "coincidences": {"has_coincidence": False}
                },
                "result": result,
                "constellation": {'name': result.get('constellation', 'N/A')},
                "star_data": result,
                "events": ASTRONOMICAL_EVENTS
            }
        )
        
    except Exception as e:
        print(f"❌ Erro no cálculo: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculate-json")
async def calculate_json(
    birth_date: str = Form(...),
    birth_time: str = Form(...),
    city: str = Form(...),
    country: str = Form(...)
):
    """Calculate zenith star and return JSON result"""
    try:
        # Convert city and country to coordinates
        latitude, longitude = await geocode_location(city, country)
        
        print(f"🗺️ Processando: {city}, {country} -> {latitude}, {longitude}")
        
        # Use the find_zenith_star function
        result = find_zenith_star(birth_date, birth_time, latitude, longitude)
        
        # Add location info to result
        result['location'] = {
            'city': city,
            'country': country,
            'latitude': latitude,
            'longitude': longitude
        }
        
        return {
            "status": "success",
            "star": result,
            "birth_info": {
                "date": birth_date,
                "time": birth_time,
                "location": f"{city}, {country}"
            }
        }
        
    except Exception as e:
        print(f"❌ Erro no cálculo: {e}")
        return {
            "status": "error",
            "error": str(e)
        }

@app.get("/api/health")
async def health_check():
    """Endpoint de verificação de saúde para Railway"""
    return {"status": "healthy"}

@app.get("/test")
async def test_endpoint():
    """Teste básico"""
    return {"message": "Murphy-1 test endpoint working!"}

@app.get("/debug-structure")
async def debug_structure():
    """Debug endpoint para verificar estrutura de diretórios"""
    import os
    
    result = {
        "base_dir": str(BASE_DIR),
        "cwd": os.getcwd(),
        "app_dir_contents": [],
        "templates_exists": (BASE_DIR / "templates").exists(),
        "static_exists": (BASE_DIR / "static").exists(),
        "templates_contents": [],
        "static_contents": []
    }
    
    # Listar conteúdo do diretório app
    try:
        for item in BASE_DIR.iterdir():
            result["app_dir_contents"].append({
                "name": item.name,
                "is_dir": item.is_dir(),
                "is_file": item.is_file()
            })
    except Exception as e:
        result["app_dir_error"] = str(e)
    
    # Listar templates
    try:
        if (BASE_DIR / "templates").exists():
            for item in (BASE_DIR / "templates").iterdir():
                result["templates_contents"].append(item.name)
    except Exception as e:
        result["templates_error"] = str(e)
    
    # Listar static
    try:
        if (BASE_DIR / "static").exists():
            for item in (BASE_DIR / "static").iterdir():
                result["static_contents"].append(item.name)
    except Exception as e:
        result["static_error"] = str(e)
    
    return result

@app.get("/test-static")
async def test_static():
    """Teste específico para arquivos estáticos"""
    css_path = BASE_DIR / "static" / "css" / "style.css"
    js_path = BASE_DIR / "static" / "js" / "script.js"
    
    return {
        "css_exists": css_path.exists(),
        "css_size": css_path.stat().st_size if css_path.exists() else 0,
        "js_exists": js_path.exists(),
        "js_size": js_path.stat().st_size if js_path.exists() else 0,
        "static_mount_working": "app.mount() está ativo",
        "css_url_should_be": "/static/css/style.css",
        "js_url_should_be": "/static/js/script.js"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 