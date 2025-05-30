from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from datetime import datetime
import pytz
from geopy.geocoders import Nominatim
import math
from skyfield.api import load, Topos
from skyfield.data import hipparcos
import numpy as np
import pandas as pd
import json
import os
from typing import Optional, Dict, Any
import asyncio
from app.modern_sky_renderer import ModernSkyRenderer
from app.astrology_calculator import AstrologyCalculator

app = FastAPI(title="Murphy-1", description="Explore as coordenadas do espaço-tempo e encontre sua estrela-guia")

# Configuração de templates e arquivos estáticos
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Cache global para dados astronômicos
star_catalog = None
ts = None
planets = None
modern_sky_renderer = None
astrology_calculator = AstrologyCalculator()

class AstronomicalCalculator:
    def __init__(self):
        global ts, planets
        if ts is None:
            ts = load.timescale()
            planets = load('de421.bsp')
        self.ts = ts
        self.planets = planets
        self.earth = planets['earth']
    
    def get_coordinates_from_location(self, city: str, country: str) -> tuple:
        """Obtém latitude e longitude a partir de cidade e país"""
        try:
            geolocator = Nominatim(user_agent="cosmic_echo")
            location = geolocator.geocode(f"{city}, {country}")
            if location:
                return location.latitude, location.longitude
            else:
                raise ValueError("Localização não encontrada")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao obter coordenadas: {str(e)}")
    
    def calculate_zenith_coordinates(self, birth_datetime: datetime, latitude: float, longitude: float) -> tuple:
        """Calcula as coordenadas do zênite para o momento e local específicos"""
        import numpy as np
        
        try:
            # Verificar se as coordenadas são válidas
            if np.isnan(latitude) or np.isnan(longitude):
                raise ValueError(f"Coordenadas inválidas: lat={latitude}, lon={longitude}")
            
            # Converter para UTC se necessário
            if birth_datetime.tzinfo is None:
                birth_datetime = pytz.UTC.localize(birth_datetime)
            
            # Criar objeto de tempo Skyfield
            t = self.ts.from_datetime(birth_datetime)
            
            # Criar observador na Terra
            observer = self.earth + Topos(latitude_degrees=latitude, longitude_degrees=longitude)
            
            # O zênite é simplesmente a direção "para cima" do observador
            # Em coordenadas astronômicas, isso corresponde à posição onde
            # a altitude é 90 graus (diretamente acima)
            
            # Para o zênite, usamos as coordenadas locais do observador
            # Ascensão Reta = Tempo Sideral Local
            # Declinação = Latitude do observador
            
            # Calcular tempo sideral local
            greenwich_sidereal = t.gast  # Greenwich Apparent Sidereal Time
            local_sidereal = greenwich_sidereal + longitude / 15.0  # Converter longitude para horas
            
            # Normalizar para 0-24 horas
            local_sidereal = local_sidereal % 24
            
            # Converter para graus (RA em horas * 15 = graus)
            zenith_ra = local_sidereal * 15
            zenith_dec = latitude
            
            # Verificar se os resultados são válidos
            if np.isnan(zenith_ra) or np.isnan(zenith_dec):
                raise ValueError(f"Coordenadas do zênite inválidas: RA={zenith_ra}, Dec={zenith_dec}")
            
            print(f"Zênite calculado: RA={zenith_ra:.2f}°, Dec={zenith_dec:.2f}°")
            return zenith_ra, zenith_dec
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro no cálculo astronômico: {str(e)}")

class StarCatalog:
    def __init__(self):
        self.stars_df = None
        self.load_catalog()
    
    def load_catalog(self):
        """Carrega o catálogo de estrelas"""
        try:
            # Usar catálogo Hipparcos integrado do Skyfield
            with load.open(hipparcos.URL) as f:
                stars = hipparcos.load_dataframe(f)
            
            # Remover estrelas com valores NaN em campos críticos
            stars = stars.dropna(subset=['ra_hours', 'dec_degrees', 'magnitude'])
            
            # Filtrar estrelas mais brilhantes (magnitude < 6.0 para visibilidade a olho nu)
            bright_stars = stars[stars['magnitude'] < 6.0].copy()
            
            # Adicionar nomes próprios conhecidos
            star_names = self.get_star_names()
            bright_stars['proper_name'] = bright_stars.index.map(star_names)
            
            # Calcular coordenadas em graus
            bright_stars['ra_degrees'] = bright_stars['ra_hours'] * 15
            bright_stars['dec_degrees'] = bright_stars['dec_degrees']
            
            # Verificar se ainda temos dados válidos
            if bright_stars.empty:
                print("Nenhuma estrela válida encontrada no catálogo, usando fallback")
                self.create_fallback_catalog()
            else:
                self.stars_df = bright_stars
                print(f"Catálogo carregado com {len(bright_stars)} estrelas")
            
        except Exception as e:
            print(f"Erro ao carregar catálogo: {e}")
            # Criar catálogo mínimo de fallback
            self.create_fallback_catalog()
    
    def get_star_names(self) -> dict:
        """Retorna dicionário com nomes próprios de estrelas famosas"""
        return {
            32349: "Sirius",      # Alpha Canis Majoris
            30438: "Canopus",     # Alpha Carinae  
            69673: "Arcturus",    # Alpha Bootis
            91262: "Vega",        # Alpha Lyrae
            24436: "Capella",     # Alpha Aurigae
            37279: "Rigel",       # Beta Orionis
            37826: "Procyon",     # Alpha Canis Minoris
            25336: "Betelgeuse",  # Alpha Orionis
            5447: "Achernar",     # Alpha Eridani
            68702: "Hadar",       # Beta Centauri
            71683: "Altair",      # Alpha Aquilae
            21421: "Aldebaran",   # Alpha Tauri
            68756: "Antares",     # Alpha Scorpii
            24608: "Spica",       # Alpha Virginis
            113368: "Fomalhaut",  # Alpha Piscis Austrini
            26311: "Pollux",      # Beta Geminorum
            14576: "Deneb",       # Alpha Cygni
            11767: "Regulus",     # Alpha Leonis
        }
    
    def create_fallback_catalog(self):
        """Cria um catálogo mínimo caso o principal falhe"""
        fallback_data = {
            'ra_hours': [6.75, 14.66, 18.62, 5.60, 7.58],
            'dec_degrees': [-16.72, -60.84, 38.78, 7.41, 28.03],
            'magnitude': [1.46, -0.74, 0.03, 0.87, 1.14],
            'proper_name': ['Sirius', 'Canopus', 'Vega', 'Betelgeuse', 'Capella']
        }
        
        self.stars_df = pd.DataFrame(fallback_data)
        self.stars_df['ra_degrees'] = self.stars_df['ra_hours'] * 15
        self.stars_df.index = range(len(self.stars_df))
    
    def find_zenith_star(self, zenith_ra: float, zenith_dec: float) -> dict:
        """Encontra a estrela mais relevante próxima ao zênite - APENAS estrelas com nomes próprios"""
        import numpy as np
        
        if self.stars_df is None or self.stars_df.empty:
            return None
        
        # Verificar se as coordenadas do zênite são válidas
        if np.isnan(zenith_ra) or np.isnan(zenith_dec):
            print(f"Coordenadas do zênite inválidas: RA={zenith_ra}, Dec={zenith_dec}")
            return None
        
        # Calcular distância angular para todas as estrelas
        def angular_distance(ra1, dec1, ra2, dec2):
            """Calcula distância angular entre duas posições em graus"""
            try:
                ra1, dec1, ra2, dec2 = map(math.radians, [ra1, dec1, ra2, dec2])
                
                cos_dist = (math.sin(dec1) * math.sin(dec2) + 
                           math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2))
                
                # Evitar erros de arredondamento
                cos_dist = max(-1, min(1, cos_dist))
                return math.degrees(math.acos(cos_dist))
            except (ValueError, TypeError):
                return 180.0  # Distância máxima em caso de erro
        
        # Calcular distâncias
        distances = []
        for _, star in self.stars_df.iterrows():
            # Verificar se as coordenadas da estrela são válidas
            if np.isnan(star['ra_degrees']) or np.isnan(star['dec_degrees']):
                distances.append(180.0)  # Distância máxima para estrelas inválidas
            else:
                dist = angular_distance(zenith_ra, zenith_dec, 
                                      star['ra_degrees'], star['dec_degrees'])
                distances.append(dist)
        
        self.stars_df['distance_to_zenith'] = distances
        
        # APENAS estrelas com nomes próprios - ignorar HD, HIP, etc.
        named_stars = self.stars_df[self.stars_df['proper_name'].notna()].copy()
        
        if named_stars.empty:
            print("Nenhuma estrela com nome próprio encontrada, usando fallback")
            # Fallback para estrelas brilhantes se não houver nomes próprios
            bright_stars = self.stars_df[self.stars_df['magnitude'] < 2.0]
            if not bright_stars.empty:
                best_star = bright_stars.loc[bright_stars['distance_to_zenith'].idxmin()]
                return self.format_star_info(best_star, "bright_fallback")
            else:
                best_star = self.stars_df.loc[self.stars_df['distance_to_zenith'].idxmin()]
                return self.format_star_info(best_star, "closest_fallback")
        
        # Encontrar a estrela com nome próprio mais próxima do zênite
        best_named_star = named_stars.loc[named_stars['distance_to_zenith'].idxmin()]
        
        print(f"Estrela selecionada: {best_named_star['proper_name']} - Distância: {best_named_star['distance_to_zenith']:.2f}°")
        
        return self.format_star_info(best_named_star, "named_star")
    
    def format_star_info(self, star, priority_type: str) -> dict:
        """Formata informações da estrela para exibição"""
        import numpy as np
        
        # Verificar e tratar valores NaN
        magnitude = star['magnitude'] if not np.isnan(star['magnitude']) else 5.0
        ra_degrees = star['ra_degrees'] if not np.isnan(star['ra_degrees']) else 0.0
        dec_degrees = star['dec_degrees'] if not np.isnan(star['dec_degrees']) else 0.0
        distance_to_zenith = star['distance_to_zenith'] if not np.isnan(star['distance_to_zenith']) else 90.0
        
        # Determinar cor baseada na magnitude (simplificado)
        if magnitude < 1.0:
            color = "#E6F3FF"  # Azul muito claro para estrelas muito brilhantes
        elif magnitude < 2.0:
            color = "#CCE7FF"  # Azul claro
        elif magnitude < 3.0:
            color = "#B3DBFF"  # Azul médio
        else:
            color = "#99CFFF"  # Azul mais escuro
        
        # Calcular distância estimada (simplificado baseado na magnitude)
        try:
            estimated_distance = max(10, int(10 ** ((magnitude + 5) / 5)))
        except (ValueError, OverflowError):
            estimated_distance = 100  # Valor padrão
        
        # Obter nome da estrela
        star_name = "Estrela Desconhecida"
        if pd.notna(star.get('proper_name')):
            star_name = star['proper_name']
        elif hasattr(star, 'name') and star.name:
            star_name = f"HD {star.name}"
        
        # Calcular velocidade radial estimada
        radial_velocity_info = self.estimate_radial_velocity(star_name, magnitude)
        
        # Estimar classe espectral
        spectral_class = self.estimate_spectral_class(magnitude)
        
        # Gerar curiosidades da estrela
        curiosities = self.generate_star_curiosities(star_name, magnitude, estimated_distance, spectral_class)
        
        return {
            'name': star_name,
            'magnitude': round(magnitude, 2),
            'ra_degrees': round(ra_degrees, 2),
            'dec_degrees': round(dec_degrees, 2),
            'distance_to_zenith': round(distance_to_zenith, 2),
            'estimated_distance_ly': estimated_distance,
            'color': color,
            'priority_type': priority_type,
            'spectral_class': spectral_class,
            'constellation': self.estimate_constellation(ra_degrees, dec_degrees),
            'radial_velocity': radial_velocity_info['velocity'],
            'radial_velocity_direction': radial_velocity_info['direction'],
            'radial_velocity_description': radial_velocity_info['description'],
            'curiosities': curiosities
        }
    
    def estimate_spectral_class(self, magnitude: float) -> str:
        """Estima classe espectral baseada na magnitude (simplificado)"""
        import numpy as np
        
        # Tratar valores NaN
        if np.isnan(magnitude):
            magnitude = 5.0
            
        if magnitude < 0:
            return "O5V - Supergigante Azul"
        elif magnitude < 1:
            return "B2V - Gigante Azul-Branca"
        elif magnitude < 2:
            return "A0V - Estrela Branca"
        elif magnitude < 3:
            return "F5V - Estrela Branco-Amarelada"
        elif magnitude < 4:
            return "G2V - Anã Amarela"
        else:
            return "K0V - Anã Laranja"
    
    def estimate_constellation(self, ra: float, dec: float) -> str:
        """Estima constelação baseada em coordenadas (simplificado)"""
        import numpy as np
        
        # Tratar valores NaN
        if np.isnan(ra):
            ra = 0.0
        if np.isnan(dec):
            dec = 0.0
            
        # Mapeamento muito simplificado baseado em RA
        ra_hours = ra / 15
        
        if 0 <= ra_hours < 2:
            return "Pisces"
        elif 2 <= ra_hours < 4:
            return "Aries"
        elif 4 <= ra_hours < 6:
            return "Taurus"
        elif 6 <= ra_hours < 8:
            return "Gemini"
        elif 8 <= ra_hours < 10:
            return "Cancer"
        elif 10 <= ra_hours < 12:
            return "Leo"
        elif 12 <= ra_hours < 14:
            return "Virgo"
        elif 14 <= ra_hours < 16:
            return "Libra"
        elif 16 <= ra_hours < 18:
            return "Scorpius"
        elif 18 <= ra_hours < 20:
            return "Sagittarius"
        elif 20 <= ra_hours < 22:
            return "Capricornus"
        else:
            return "Aquarius"
    
    def estimate_radial_velocity(self, star_name: str, magnitude: float) -> dict:
        """Estima velocidade radial da estrela baseada em dados conhecidos"""
        import random
        
        # Velocidades radiais conhecidas para estrelas famosas (em km/s)
        known_velocities = {
            'Sirius': {'velocity': -5.5, 'direction': 'approaching'},
            'Vega': {'velocity': -13.9, 'direction': 'approaching'},
            'Arcturus': {'velocity': -5.2, 'direction': 'approaching'},
            'Capella': {'velocity': 30.2, 'direction': 'receding'},
            'Rigel': {'velocity': 17.8, 'direction': 'receding'},
            'Betelgeuse': {'velocity': 21.9, 'direction': 'receding'},
            'Aldebaran': {'velocity': 54.3, 'direction': 'receding'},
            'Spica': {'velocity': 1.0, 'direction': 'stable'},
            'Antares': {'velocity': -3.4, 'direction': 'approaching'},
            'Fomalhaut': {'velocity': 6.5, 'direction': 'receding'},
            'Pollux': {'velocity': 3.3, 'direction': 'receding'},
            'Deneb': {'velocity': -4.5, 'direction': 'approaching'},
            'Regulus': {'velocity': 5.9, 'direction': 'receding'},
            'Altair': {'velocity': -26.1, 'direction': 'approaching'},
            'Procyon': {'velocity': -3.2, 'direction': 'approaching'}
        }
        
        if star_name in known_velocities:
            data = known_velocities[star_name]
            velocity = abs(data['velocity'])
            direction = data['direction']
        else:
            # Estimar baseado na magnitude e tipo espectral
            # Estrelas mais brilhantes tendem a ter velocidades menores (mais próximas)
            if magnitude < 1.0:
                velocity = random.uniform(5, 25)
            elif magnitude < 2.0:
                velocity = random.uniform(10, 40)
            elif magnitude < 3.0:
                velocity = random.uniform(15, 60)
            else:
                velocity = random.uniform(20, 80)
            
            # Direção aleatória mas com tendência baseada na posição galáctica
            direction = random.choice(['approaching', 'receding', 'stable'])
        
        # Gerar descrição
        if direction == 'approaching':
            description = f"Se aproximando de nós a {velocity:.1f} km/s"
            emoji = "🔵"
        elif direction == 'receding':
            description = f"Se afastando de nós a {velocity:.1f} km/s"
            emoji = "🔴"
        else:
            description = f"Movimento radial estável (~{velocity:.1f} km/s)"
            emoji = "⚪"
        
        return {
            'velocity': round(velocity, 1),
            'direction': direction,
            'description': f"{emoji} {description}"
        }
    
    def generate_star_curiosities(self, star_name: str, magnitude: float, distance: float, spectral_class: str) -> dict:
        """Gera curiosidades interessantes sobre a estrela"""
        import random
        
        # Base de dados de curiosidades para estrelas famosas
        famous_stars_data = {
            'Sirius': {
                'age_billion_years': 0.25,
                'history': 'Conhecida pelos antigos egípcios como Sopdet, Sirius era associada à deusa Ísis. Seu surgimento no céu marcava o início da inundação anual do Nilo, crucial para a agricultura.',
                'fun_facts': [
                    'É na verdade um sistema estelar duplo',
                    'Sua companheira é uma anã branca super densa',
                    'É 25 vezes mais luminosa que o Sol',
                    'Aparece com cores cintilantes devido à atmosfera terrestre'
                ]
            },
            'Vega': {
                'age_billion_years': 0.455,
                'history': 'Vega foi a primeira estrela fotografada em 1850 e a primeira a ter seu espectro registrado. Há 12.000 anos, era a estrela polar, e voltará a ser em cerca de 13.727 d.C.',
                'fun_facts': [
                    'Foi usada como padrão de magnitude zero',
                    'Tem um disco de detritos que pode indicar planetas',
                    'Gira tão rápido que é achatada nos polos',
                    'Era a estrela polar dos neandertais'
                ]
            },
            'Betelgeuse': {
                'age_billion_years': 0.01,
                'history': 'Uma das estrelas mais famosas de Órion, Betelgeuse é uma supergigante vermelha que pode explodir como supernova a qualquer momento (astronomicamente falando).',
                'fun_facts': [
                    'Se estivesse no lugar do Sol, englobaria a órbita de Júpiter',
                    'Sua luminosidade varia irregularmente',
                    'Pode explodir nos próximos 100.000 anos',
                    'Ejeta material suficiente para formar planetas'
                ]
            },
            'Rigel': {
                'age_billion_years': 0.008,
                'history': 'Apesar de ser designada como Beta Orionis, Rigel é geralmente mais brilhante que Betelgeuse (Alpha Orionis). É uma das estrelas mais luminosas conhecidas.',
                'fun_facts': [
                    'É 120.000 vezes mais luminosa que o Sol',
                    'É na verdade um sistema múltiplo de 4 estrelas',
                    'Suas camadas externas são ejetadas por ventos estelares',
                    'É jovem demais para ter planetas rochosos formados'
                ]
            },
            'Arcturus': {
                'age_billion_years': 7.1,
                'history': 'Arcturus é uma das estrelas mais antigas do halo galáctico. Move-se de forma diferente das outras estrelas, sugerindo que pertencia a uma galáxia menor que foi absorvida pela Via Láctea.',
                'fun_facts': [
                    'É uma das estrelas mais rápidas no céu',
                    'Tem baixa metalicidade, indicando origem antiga',
                    'Em 1933, sua luz foi usada para abrir a Feira Mundial de Chicago',
                    'Pode ser um intruso de uma galáxia antiga'
                ]
            },
            'Capella': {
                'age_billion_years': 0.59,
                'history': 'Capella é na verdade um sistema complexo de seis estrelas. Era considerada uma única estrela pelos antigos, mas telescópios modernos revelaram sua verdadeira natureza múltipla.',
                'fun_facts': [
                    'Contém duas gigantes douradas e quatro anãs vermelhas',
                    'É a terceira estrela mais brilhante do hemisfério norte',
                    'Suas componentes principais orbitam uma à outra em 104 dias',
                    'Foi usada para testes iniciais de interferometria estelar'
                ]
            }
        }
        
        # Se a estrela está na base de dados
        if star_name in famous_stars_data:
            star_data = famous_stars_data[star_name]
            age = star_data['age_billion_years']
            history = star_data['history']
            fun_facts = star_data['fun_facts']
        else:
            # Gerar dados baseados nas características da estrela
            age = self.estimate_star_age(magnitude, spectral_class)
            history = self.generate_generic_history(star_name, spectral_class)
            fun_facts = self.generate_generic_facts(spectral_class, magnitude, distance)
        
        # Converter idade para diferentes escalas de tempo
        age_in_years = age * 1_000_000_000
        light_travel_years = distance
        
        # Mensagem temporal Murphy-1
        temporal_message = self.generate_temporal_message(age, light_travel_years)
        
        return {
            'age_billion_years': age,
            'age_formatted': f"{age:.2f} bilhões de anos",
            'history': history,
            'fun_facts': fun_facts,
            'temporal_message': temporal_message,
            'birth_era': self.determine_birth_era(age),
            'timeline_comparison': self.create_timeline_comparison(age, light_travel_years)
        }
    
    def estimate_star_age(self, magnitude: float, spectral_class: str) -> float:
        """Estima a idade da estrela baseada em suas características"""
        import random
        
        # Idade estimada baseada na classe espectral
        if 'O' in spectral_class or 'B' in spectral_class:
            # Estrelas muito quentes e jovens
            return random.uniform(0.001, 0.1)
        elif 'A' in spectral_class:
            # Estrelas quentes, relativamente jovens
            return random.uniform(0.1, 2.0)
        elif 'F' in spectral_class:
            # Estrelas similares ao Sol, mas um pouco mais quentes
            return random.uniform(1.0, 8.0)
        elif 'G' in spectral_class:
            # Estrelas tipo solar
            return random.uniform(1.0, 12.0)
        elif 'K' in spectral_class:
            # Estrelas laranjas, de longa vida
            return random.uniform(5.0, 15.0)
        elif 'M' in spectral_class:
            # Anãs vermelhas, muito longevas
            return random.uniform(8.0, 13.8)  # Até a idade do universo
        else:
            # Estimativa genérica
            return random.uniform(1.0, 10.0)
    
    def generate_generic_history(self, star_name: str, spectral_class: str) -> str:
        """Gera uma história genérica para estrelas menos conhecidas"""
        type_descriptions = {
            'O': 'uma jovem gigante azul, nascida em uma região de intensa formação estelar',
            'B': 'uma estrela jovem e quente, típica de aglomerados estelares ativos',
            'A': 'uma estrela branca em sua sequência principal, queimando hidrogênio em seu núcleo',
            'F': 'uma estrela branco-amarelada, ligeiramente mais massiva que o Sol',
            'G': 'uma estrela amarela similar ao nosso Sol, estável em sua sequência principal',
            'K': 'uma estrela laranja de longa vida, menor e mais fria que o Sol',
            'M': 'uma anã vermelha, o tipo mais comum de estrela na galáxia'
        }
        
        spectral_type = spectral_class[0] if spectral_class else 'G'
        description = type_descriptions.get(spectral_type, 'uma estrela de características interessantes')
        
        return f"{star_name} é {description}. Como muitas estrelas em nossa região da galáxia, ela se formou a partir do colapso de uma nuvem molecular, iniciando sua jornada cósmica através do espaço-tempo."
    
    def generate_generic_facts(self, spectral_class: str, magnitude: float, distance: float) -> list:
        """Gera fatos interessantes baseados nas características da estrela"""
        facts = []
        
        # Fatos baseados na distância
        if distance < 50:
            facts.append(f"É uma das estrelas mais próximas da Terra, a apenas {distance:.0f} anos-luz")
        elif distance > 1000:
            facts.append(f"Sua luz viajou {distance:,.0f} anos-luz através do espaço para chegar até você")
        
        # Fatos baseados na magnitude
        if magnitude < 2.0:
            facts.append("É visível a olho nu mesmo em céus urbanos com poluição luminosa")
        elif magnitude < 4.0:
            facts.append("É facilmente visível a olho nu em noites claras")
        else:
            facts.append("Requer céus escuros para ser observada a olho nu")
        
        # Fatos baseados na classe espectral
        if 'O' in spectral_class or 'B' in spectral_class:
            facts.append("Queima combustível tão rapidamente que viverá apenas milhões de anos")
            facts.append("Termina sua vida de forma dramática como supernova")
        elif 'G' in spectral_class:
            facts.append("Tem temperatura e composição similares ao nosso Sol")
            facts.append("Pode hospedar planetas com condições favoráveis à vida")
        elif 'M' in spectral_class:
            facts.append("Viverá por trilhões de anos, muito além da idade atual do universo")
            facts.append("É parte do tipo mais comum de estrela na Via Láctea")
        
        return facts[:4]  # Retornar no máximo 4 fatos
    
    def generate_temporal_message(self, age_billion_years: float, light_distance: float) -> str:
        """Gera mensagem temporal estilo Murphy-1/Interestelar"""
        age_millions = age_billion_years * 1000
        
        if age_billion_years < 0.1:
            temporal_context = "uma estrela-criança no tempo cósmico"
        elif age_billion_years < 1:
            temporal_context = "uma estrela jovem na linha temporal universal"
        elif age_billion_years < 5:
            temporal_context = "uma estrela em sua idade adulta cósmica"
        elif age_billion_years < 10:
            temporal_context = "uma estrela veterana do cosmos"
        else:
            temporal_context = "uma estrela anciã, testemunha da evolução galáctica"
        
        return f"No espaço-tempo quadridimensional, {temporal_context} observou sua chegada ao universo. Sua luz, viajando por {light_distance:,.0f} anos através das coordenadas espaciais, carrega informações de quando você ainda era apenas uma possibilidade quântica."
    
    def determine_birth_era(self, age_billion_years: float) -> str:
        """Determina a era cósmica do nascimento da estrela"""
        if age_billion_years > 13:
            return "Era Primordial (impossível - anterior ao Big Bang)"
        elif age_billion_years > 10:
            return "Era das Primeiras Galáxias"
        elif age_billion_years > 8:
            return "Era da Formação Galáctica Ativa"
        elif age_billion_years > 5:
            return "Era da Maturidade Galáctica"
        elif age_billion_years > 1:
            return "Era Solar (similar ao Sol)"
        else:
            return "Era Moderna da Formação Estelar"
    
    def create_timeline_comparison(self, star_age: float, light_travel: float) -> dict:
        """Cria comparações temporais interessantes"""
        earth_age = 4.54  # bilhões de anos
        universe_age = 13.8  # bilhões de anos
        
        star_age_years = star_age * 1_000_000_000
        
        comparisons = []
        
        if star_age < earth_age:
            difference = earth_age - star_age
            comparisons.append(f"Nasceu {difference:.1f} bilhões de anos após a Terra")
        else:
            difference = star_age - earth_age
            comparisons.append(f"É {difference:.1f} bilhões de anos mais antiga que a Terra")
        
        if light_travel < 100:
            comparisons.append(f"Sua luz é praticamente contemporânea à escala humana")
        elif light_travel < 1000:
            comparisons.append(f"Sua luz começou a jornada antes das primeiras civilizações")
        else:
            comparisons.append(f"Sua luz começou a viajar na era dos dinossauros")
        
        return {
            'star_age_percent_of_universe': (star_age / universe_age) * 100,
            'comparisons': comparisons,
            'era_when_light_started': self.calculate_light_start_era(light_travel)
        }
    
    def calculate_light_start_era(self, light_years: float) -> str:
        """Calcula que era histórica a luz começou a viajar"""
        years_ago = light_years  # anos-luz = anos no passado
        
        if years_ago < 100:
            return "Era moderna recente"
        elif years_ago < 2000:
            return "Era do Império Romano"
        elif years_ago < 10000:
            return "Era Neolítica"
        elif years_ago < 100000:
            return "Era dos primeiros Homo sapiens"
        elif years_ago < 1000000:
            return "Era Pleistocena"
        elif years_ago < 65000000:
            return "Era Cenozoica"
        elif years_ago < 250000000:
            return "Era dos dinossauros"
        else:
            return "Era Paleozoica ou anterior"

# Inicializar objetos globais
calculator = AstronomicalCalculator()
star_catalog = StarCatalog()
modern_sky_renderer = ModernSkyRenderer()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Página inicial do aplicativo"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
async def calculate_cosmic_echo(
    request: Request,
    birth_date: str = Form(...),
    birth_time: str = Form(...),
    city: str = Form(...),
    country: str = Form(...)
):
    """Calcula a análise temporal Murphy-1 do usuário"""
    try:
        # Parse da data e hora
        birth_datetime_str = f"{birth_date} {birth_time}"
        birth_datetime = datetime.strptime(birth_datetime_str, "%Y-%m-%d %H:%M")
        
        # Obter coordenadas
        latitude, longitude = calculator.get_coordinates_from_location(city, country)
        
        # Calcular coordenadas do zênite
        zenith_ra, zenith_dec = calculator.calculate_zenith_coordinates(
            birth_datetime, latitude, longitude
        )
        
        # Encontrar estrela do zênite
        zenith_star = star_catalog.find_zenith_star(zenith_ra, zenith_dec)
        
        if not zenith_star:
            raise HTTPException(status_code=500, detail="Não foi possível encontrar uma estrela adequada")
        
        # Gerar dados para visualização moderna
        modern_sky_data = modern_sky_renderer.generate_modern_sky_data(
            zenith_ra, zenith_dec, zenith_star, 
            birth_datetime, latitude, longitude
        )
        
        # Calcular perfil astrológico completo
        astro_profile = astrology_calculator.generate_cosmic_profile(
            birth_datetime, latitude, longitude
        )
        
        # Preparar dados para o template
        result_data = {
            'birth_info': {
                'date': birth_date,
                'time': birth_time,
                'location': f"{city}, {country}",
                'coordinates': f"{latitude:.2f}°, {longitude:.2f}°"
            },
            'zenith_coordinates': {
                'ra': zenith_ra,
                'dec': zenith_dec
            },
            'star': zenith_star,
            'cosmic_message': generate_cosmic_message(zenith_star),
            'modern_sky_data': modern_sky_data,
            'astrology': astro_profile
        }
        
        return templates.TemplateResponse("result.html", {
            "request": request,
            "data": result_data
        })
        
    except Exception as e:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error": str(e)
        })

def generate_cosmic_message(star: dict) -> str:
    """Gera mensagem cósmica personalizada"""
    distance = star['estimated_distance_ly']
    name = star['name']
    
    if star['priority_type'] == 'named_close':
        return f"A majestosa {name} estava perfeitamente alinhada com você no seu primeiro momento. Sua luz viajou {distance:,} anos através do cosmos para testemunhar seu nascimento."
    elif star['priority_type'] == 'bright_close':
        return f"A brilhante estrela {name} iluminava seu zênite quando você chegou ao mundo. Por {distance:,} anos, sua luz cruzou o universo para encontrar você."
    else:
        return f"A estrela {name} era sua guardiã celestial no momento do seu nascimento. Através de {distance:,} anos-luz de jornada cósmica, sua luz chegou até você."

@app.get("/api/health")
async def health_check():
    """Endpoint de verificação de saúde"""
    return {"status": "healthy", "message": "Murphy-1 está operacional e pronto para análise temporal!"}

# Remover a execução direta para deploy
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000) 