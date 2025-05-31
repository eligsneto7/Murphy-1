"""
Zenith Calculator - Calcula a estrela no zênite para um momento específico
"""

from datetime import datetime
import pytz
from skyfield.api import load, Topos
from app.star_data import find_nearest_named_star
import pandas as pd
import math

# Cache global para dados astronômicos
_ts = None
_planets = None

def _get_astronomical_data():
    """Lazy loading dos dados astronômicos"""
    global _ts, _planets
    if _ts is None:
        _ts = load.timescale()
        _planets = load('de421.bsp')
    return _ts, _planets

def find_zenith_star(birth_date, birth_time, latitude, longitude):
    """
    Encontra a estrela nomeada mais próxima do zênite no momento do nascimento
    """
    try:
        # Converter strings para datetime
        if isinstance(birth_date, str) and isinstance(birth_time, str):
            birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
        else:
            birth_datetime = datetime.combine(birth_date, birth_time)
            
        # Adicionar timezone se não tiver
        if birth_datetime.tzinfo is None:
            birth_datetime = pytz.UTC.localize(birth_datetime)
            
        # Obter dados astronômicos
        ts, planets = _get_astronomical_data()
        earth = planets['earth']
        
        # Criar objeto de tempo
        t = ts.from_datetime(birth_datetime)
        
        # Criar observador
        observer = earth + Topos(latitude_degrees=latitude, longitude_degrees=longitude)
        
        # Calcular tempo sideral local
        greenwich_sidereal = t.gast
        local_sidereal = greenwich_sidereal + longitude / 15.0
        local_sidereal = local_sidereal % 24
        
        # Coordenadas do zênite
        zenith_ra = local_sidereal * 15  # Converter horas para graus
        zenith_dec = latitude
        
        # Buscar estrela nomeada mais próxima
        star_name, distance, star_data = find_nearest_named_star(zenith_ra, zenith_dec)
        
        # Montar dados da estrela com informações precisas
        result = {
            'name': star_name,
            'constellation': star_data['constellation'],
            'magnitude': star_data['magnitude'],
            'distance_ly': star_data['distance_ly'],
            'ra_degrees': star_data['ra_degrees'],
            'dec_degrees': star_data['dec_degrees'],
            'distance_to_zenith': round(distance, 2),
            'spectral_class': star_data['spectral_class'],
            'color': get_star_color(star_data['spectral_class']),
            'radial_velocity': generate_velocity_description(star_name),
            'curiosities': generate_star_curiosities(
                star_name,
                star_data
            ),
            # Dados adicionais da estrela
            'age_billion_years': star_data['age_billion_years'],
            'temperature_k': star_data['temperature_k'],
            'mass_solar': star_data['mass_solar'],
            'history': star_data['history'],
            'constellation_stars': star_data['constellation_stars']
        }
        
        return result
        
    except Exception as e:
        print(f"Erro no cálculo do zênite: {e}")
        # Retornar Sirius como fallback
        from app.star_data import NAMED_STARS
        sirius = NAMED_STARS['Sirius']
        return {
            'name': 'Sirius',
            'constellation': sirius['constellation'],
            'magnitude': sirius['magnitude'],
            'distance_ly': sirius['distance_ly'],
            'ra_degrees': sirius['ra_degrees'],
            'dec_degrees': sirius['dec_degrees'],
            'distance_to_zenith': 0,
            'spectral_class': sirius['spectral_class'],
            'color': '#E6F3FF',
            'radial_velocity': {'description': 'Se aproximando a 5.5 km/s'},
            'curiosities': generate_star_curiosities('Sirius', sirius),
            'age_billion_years': sirius['age_billion_years'],
            'temperature_k': sirius['temperature_k'],
            'mass_solar': sirius['mass_solar'],
            'history': sirius['history'],
            'constellation_stars': sirius['constellation_stars']
        }


def angular_distance(ra1, dec1, ra2, dec2):
    """Calcula distância angular entre duas posições em graus"""
    ra1, dec1, ra2, dec2 = map(math.radians, [ra1, dec1, ra2, dec2])
    
    cos_dist = (math.sin(dec1) * math.sin(dec2) + 
               math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2))
    
    cos_dist = max(-1, min(1, cos_dist))
    return math.degrees(math.acos(cos_dist))


def estimate_spectral_class(magnitude):
    """Estima classe espectral baseada na magnitude"""
    if magnitude < 0:
        return 'O5V'
    elif magnitude < 1:
        return 'B2V'
    elif magnitude < 2:
        return 'A0V'
    elif magnitude < 3:
        return 'F5V'
    elif magnitude < 4:
        return 'G2V'
    elif magnitude < 5:
        return 'K0V'
    else:
        return 'M0V'


def estimate_distance(magnitude):
    """Estima distância em anos-luz baseada na magnitude"""
    # Fórmula simples: mais brilhante geralmente = mais próximo
    if magnitude < 0:
        return int(50 + magnitude * 10)
    elif magnitude < 2:
        return int(100 + magnitude * 50)
    elif magnitude < 4:
        return int(200 + magnitude * 100)
    else:
        return int(500 + magnitude * 200)


def get_star_color(spectral_class):
    """Retorna cor baseada na classe espectral"""
    colors = {
        'O': '#9bb0ff',  # Azul
        'B': '#aabfff',  # Azul-branco
        'A': '#cad7ff',  # Branco
        'F': '#f8f7ff',  # Branco-amarelo
        'G': '#fff4ea',  # Amarelo
        'K': '#ffd2a1',  # Laranja
        'M': '#ffcc6f'   # Vermelho
    }
    return colors.get(spectral_class[0], '#ffffff')


def generate_velocity_description(star_name):
    """Gera descrição da velocidade radial"""
    import random
    descriptions = [
        f"{star_name} está se aproximando lentamente",
        f"{star_name} está se afastando gradualmente", 
        f"{star_name} está se movendo perpendicularmente",
        f"{star_name} está se movendo lentamente",
        f"{star_name} está se aproximando rapidamente"
    ]
    return random.choice(descriptions)


# Importar função necessária
def generate_star_curiosities(name, star_data):
    """Placeholder - será importado do astro_data"""
    return {
        'age_formatted': f"{star_data['distance_ly'] * 10} milhões de anos",
        'birth_era': "Era Pré-Solar",
        'temporal_message': f"Esta estrela brilha há muito mais tempo que nosso Sol",
        'history': f"{name} é uma estrela fascinante com características únicas",
        'fun_facts': [
            f"Está a {star_data['distance_ly']} anos-luz de distância",
            f"Sua magnitude aparente é {star_data['magnitude']}",
            f"Pertence à classe espectral {star_data['spectral_class']}"
        ],
        'timeline_comparison': {
            'comparisons': [
                f"Quando {name} nasceu, a Terra ainda não existia",
                f"A luz que vemos hoje saiu da estrela há {star_data['distance_ly']} anos"
            ],
            'era_when_light_started': f"Há {star_data['distance_ly']} anos"
        }
    } 