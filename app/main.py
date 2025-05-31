from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, time
import pytz
from pathlib import Path
from app.astrology_calculator import AstrologyCalculator
from app.astro_data import (
    generate_cosmic_message, 
    generate_star_curiosities, 
    get_astrology_data,
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

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(
    request: Request,
    birth_date: str = Form(...),
    birth_time: str = Form(...),
    latitude: float = Form(...),
    longitude: float = Form(...)
):
    """Calcula a estrela zenital e retorna o resultado"""
    try:
        # Usar a função find_zenith_star existente
        result = find_zenith_star(birth_date, birth_time, latitude, longitude)
        
        # Gerar visualização do céu se tiver dados necessários
        try:
            renderer = get_modern_sky_renderer()
            sky_data = renderer.generate_modern_sky_data(
                result['ra_degrees'],
                result['dec_degrees'],
                result,
                datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M"),
                latitude,
                longitude
            )
            result.update(sky_data)
        except Exception as sky_error:
            print(f"Erro na visualização do céu: {sky_error}")
            # Dados padrão se houver erro
            result.update({
                'stars': [],
                'constellation': {'name': result.get('constellation', 'N/A'), 'lines': []}
            })
        
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "result": result,
                "constellation": {'name': result.get('constellation', 'N/A')},
                "star_data": result,
                "events": ASTRONOMICAL_EVENTS
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

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