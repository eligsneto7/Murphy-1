"""
Zenith Calculator - Calcula a estrela no zênite para um momento específico
"""

from datetime import datetime
import pytz
from skyfield.api import load, Topos, wgs84
from skyfield.units import Angle
from skyfield.timelib import Time
from skyfield.data import hipparcos
from app.star_data import find_nearest_named_star
import pandas as pd
import math
import numpy as np
import os
from pathlib import Path

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

def load_hipparcos_data():
    """Load Hipparcos catalog data"""
    # Create data directory if it doesn't exist
    data_dir = Path(__file__).parent / 'data'
    data_dir.mkdir(exist_ok=True)
    
    # Download and load the catalog
    with load.open(hipparcos.URL) as f:
        df = pd.read_csv(f, sep='|', skiprows=1)
    
    return df

def find_zenith_star(birth_date, birth_time, latitude, longitude):
    """Find the star that was at zenith at the given time and location"""
    try:
        # Load Hipparcos data
        df = load_hipparcos_data()
        
        # Parse birth datetime
        birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
        
        # Create time object
        ts = load.timescale()
        t = ts.from_datetime(birth_datetime)
        
        # Create location object
        location = wgs84.latlon(latitude, longitude)
        
        # Calculate zenith position
        zenith = location.at(t).from_altaz(alt_degrees=90, az_degrees=0)
        
        # Convert star positions to same frame
        star_positions = df[['ra', 'dec']].values
        
        # Calculate angular distances
        distances = []
        for ra, dec in star_positions:
            star_pos = zenith.from_radec(ra, dec)
            distance = star_pos.separation_from(zenith).degrees
            distances.append(distance)
        
        # Find closest star
        closest_idx = np.argmin(distances)
        closest_star = df.iloc[closest_idx]
        
        return {
            'name': closest_star['name'],
            'ra_degrees': closest_star['ra'],
            'dec_degrees': closest_star['dec'],
            'magnitude': closest_star['magnitude'],
            'distance_ly': closest_star['distance'],
            'spectral_class': closest_star['spectral_type'],
            'constellation': closest_star['constellation']
        }
        
    except Exception as e:
        raise Exception(f"Error finding zenith star: {str(e)}")

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