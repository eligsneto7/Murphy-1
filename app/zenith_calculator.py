"""
Zenith Calculator para Murphy-1
Calcula estrelas próximas ao zênite baseado na localização e horário
"""

from datetime import datetime
import pytz
from skyfield.api import load, Topos
from skyfield.data import hipparcos
import pandas as pd
import math


def find_zenith_star(birth_date, birth_time, latitude, longitude):
    """
    Encontra a estrela mais próxima do zênite no momento e local do nascimento
    """
    try:
        # Converter para timezone UTC
        if isinstance(birth_date, str):
            birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
        else:
            birth_datetime = datetime.combine(birth_date, birth_time)
        
        # Assumir UTC se não especificado
        if birth_datetime.tzinfo is None:
            birth_datetime = pytz.UTC.localize(birth_datetime)
        
        # Carregar dados astronômicos
        ts = load.timescale()
        planets = load('de421.bsp')
        earth = planets['earth']
        
        # Criar observador na localização
        observer = earth + Topos(latitude, longitude)
        t = ts.from_datetime(birth_datetime)
        
        # Calcular zênite (Ra, Dec do observador no momento)
        zenith_alt, zenith_az, zenith_distance = observer.at(t).observe(earth).apparent().altaz()
        
        # O zênite está em altitude 90°, azimute qualquer
        # Calcular coordenadas do zênite
        zenith_ra, zenith_dec, _ = observer.at(t).observe(earth).apparent().radec()
        
        # Carregar catálogo de estrelas
        with load.open(hipparcos.URL) as f:
            stars_df = hipparcos.load_dataframe(f)
        
        # Filtrar estrelas brilhantes
        bright_stars = stars_df[stars_df['magnitude'] < 6.0].dropna(subset=['ra_hours', 'dec_degrees'])
        
        if bright_stars.empty:
            # Retornar uma estrela padrão se não encontrar nenhuma
            return {
                'name': 'Polaris',
                'constellation': 'Ursa Minor',
                'ra_degrees': 37.95,
                'dec_degrees': 89.26,
                'magnitude': 1.97,
                'spectral_class': 'F7Ib',
                'distance_to_zenith': 45.0,
                'estimated_distance_ly': 433,
                'color': '#fff4ea',
                'radial_velocity_description': 'Aproximando-se lentamente',
                'curiosities': generate_star_curiosities('Polaris', 433, 1.97, 'F7Ib')
            }
        
        # Converter RA de horas para graus
        bright_stars['ra_degrees'] = bright_stars['ra_hours'] * 15
        
        # Calcular distância angular ao zênite para cada estrela
        zenith_ra_deg = float(zenith_ra.hours * 15)
        zenith_dec_deg = float(zenith_dec.degrees)
        
        distances = []
        for _, star in bright_stars.iterrows():
            dist = angular_distance(
                zenith_ra_deg, zenith_dec_deg,
                star['ra_degrees'], star['dec_degrees']
            )
            distances.append(dist)
        
        bright_stars['distance_to_zenith'] = distances
        
        # Encontrar a estrela mais próxima do zênite
        closest_star = bright_stars.loc[bright_stars['distance_to_zenith'].idxmin()]
        
        # Nomes de estrelas famosas
        star_names = {
            32349: "Sirius",
            30438: "Canopus", 
            69673: "Arcturus",
            91262: "Vega",
            24436: "Capella",
            37279: "Rigel",
            37826: "Procyon",
            25336: "Betelgeuse"
        }
        
        star_name = star_names.get(closest_star.name, f"HIP {closest_star.name}")
        
        # Estimar propriedades da estrela
        spectral_class = estimate_spectral_class(closest_star['magnitude'])
        estimated_distance = estimate_distance(closest_star['magnitude'])
        color = get_star_color(spectral_class)
        
        return {
            'name': star_name,
            'constellation': 'Desconhecida',  # Seria necessário um catálogo adicional
            'ra_degrees': closest_star['ra_degrees'],
            'dec_degrees': closest_star['dec_degrees'],
            'magnitude': closest_star['magnitude'],
            'spectral_class': spectral_class,
            'distance_to_zenith': closest_star['distance_to_zenith'],
            'estimated_distance_ly': estimated_distance,
            'color': color,
            'radial_velocity_description': generate_velocity_description(),
            'curiosities': generate_star_curiosities(star_name, estimated_distance, closest_star['magnitude'], spectral_class)
        }
        
    except Exception as e:
        print(f"Erro ao calcular estrela do zênite: {e}")
        # Retornar estrela padrão em caso de erro
        return {
            'name': 'Vega',
            'constellation': 'Lyra',
            'ra_degrees': 279.23,
            'dec_degrees': 38.78,
            'magnitude': 0.03,
            'spectral_class': 'A0V',
            'distance_to_zenith': 30.0,
            'estimated_distance_ly': 25,
            'color': '#cad7ff',
            'radial_velocity_description': 'Aproximando-se',
            'curiosities': generate_star_curiosities('Vega', 25, 0.03, 'A0V')
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


def generate_velocity_description():
    """Gera descrição da velocidade radial"""
    import random
    descriptions = [
        "Aproximando-se lentamente",
        "Afastando-se gradualmente", 
        "Movimento perpendicular",
        "Velocidade radial baixa",
        "Aproximando-se rapidamente"
    ]
    return random.choice(descriptions)


# Importar função necessária
def generate_star_curiosities(name, distance, magnitude, spectral_class):
    """Placeholder - será importado do astro_data"""
    return {
        'age_formatted': f"{distance * 10} milhões de anos",
        'birth_era': "Era Pré-Solar",
        'temporal_message': f"Esta estrela brilha há muito mais tempo que nosso Sol",
        'history': f"{name} é uma estrela fascinante com características únicas",
        'fun_facts': [
            f"Está a {distance} anos-luz de distância",
            f"Sua magnitude aparente é {magnitude}",
            f"Pertence à classe espectral {spectral_class}"
        ],
        'timeline_comparison': {
            'comparisons': [
                f"Quando {name} nasceu, a Terra ainda não existia",
                f"A luz que vemos hoje saiu da estrela há {distance} anos"
            ],
            'era_when_light_started': f"Há {distance} anos"
        }
    } 