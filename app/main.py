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
from app.zenith_calculator import find_zenith_star
from app.constellation_data import get_constellation_data

app = FastAPI(title="Murphy-1", description="Explore as coordenadas do espaço-tempo e encontre sua estrela-guia")

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
calculator = None
modern_sky_renderer = None

def get_calculator():
    global calculator
    if calculator is None:
        calculator = AstrologyCalculator()
    return calculator

def get_modern_sky_renderer():
    global modern_sky_renderer
    if modern_sky_renderer is None:
        modern_sky_renderer = ModernSkyRenderer()
    return modern_sky_renderer

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Página inicial"""
    print("🏠 Home endpoint called")
    print(f"🏠 Templates object: {templates}")
    print(f"🏠 Looking for index.html in: {BASE_DIR / 'templates' / 'index.html'}")
    
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
async def calculate_cosmic_echo(
    request: Request,
    birth_date: str = Form(...),
    birth_time: str = Form(...),
    city: str = Form(...),
    country: str = Form(...)
):
    """Calcular análise Murphy-1"""
    try:
        # Parse da data de nascimento
        birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
        
        # Coordenadas fixas para testes (São Paulo)
        latitude = -23.5505
        longitude = -46.6333
        
        # Encontrar estrela do zênite
        zenith_star = find_zenith_star(birth_date, birth_time, latitude, longitude)
        
        # Gerar dados do céu moderno
        sky_renderer = get_modern_sky_renderer()
        modern_sky_data = sky_renderer.generate_modern_sky_data(
            zenith_star['ra_degrees'], 
            zenith_star['dec_degrees'], 
            zenith_star, 
            birth_datetime, 
            latitude, 
            longitude
        )
        
        # Obter dados de astrologia
        astrology_data = get_astrology_data(birth_date, birth_time, latitude, longitude)
        
        # Obter coincidências astronômicas
        coincidences = get_astronomical_coincidences(birth_date, birth_time, latitude, longitude)
        
        # Gerar dados para o template
        result_data = {
            'birth_info': {
                'date': birth_date,
                'time': birth_time,
                'location': f"{city}, {country}",
                'coordinates': f"{latitude:.4f}, {longitude:.4f}"
            },
            'star': zenith_star,
            'cosmic_message': generate_cosmic_message(zenith_star),
            'modern_sky_data': modern_sky_data,
            'astrology': astrology_data,
            'star_curiosities': zenith_star.get('curiosities', {}),
            'coincidences': coincidences
        }
        
        return templates.TemplateResponse("result.html", {
            "request": request,
            "data": result_data
        })
        
    except Exception as e:
        print(f"Erro no cálculo: {e}")
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error": str(e)
        })

@app.get("/health")
async def health_check():
    """Health check para Railway"""
    return {"status": "ok", "message": "Murphy-1 está funcionando!"}

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