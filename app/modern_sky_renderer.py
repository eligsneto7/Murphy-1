import numpy as np
import json
from skyfield.api import load, Topos
from skyfield.data import hipparcos
import pandas as pd
from datetime import datetime
import pytz
import math
import colorsys
import random

# Variáveis globais para compartilhar com main.py
ts = None
planets = None

class ModernSkyRenderer:
    def __init__(self):
        global ts, planets
        # Lazy loading - usar variáveis globais se já carregadas
        if ts is None:
            ts = load.timescale()
            planets = load('de421.bsp')
        self.ts = ts
        self.planets = planets
        self.earth = planets['earth']
        
        # Cores espectrais científicas reais (baseadas na temperatura)
        self.spectral_colors = {
            'O': {'hex': '#9bb0ff', 'temp': 30000, 'name': 'Azul Quente'},
            'B': {'hex': '#aabfff', 'temp': 20000, 'name': 'Azul-Branco'},
            'A': {'hex': '#cad7ff', 'temp': 8500, 'name': 'Branco'},
            'F': {'hex': '#f8f7ff', 'temp': 6500, 'name': 'Branco-Amarelo'},
            'G': {'hex': '#fff4ea', 'temp': 5500, 'name': 'Amarelo Solar'},
            'K': {'hex': '#ffd2a1', 'temp': 4000, 'name': 'Laranja'},
            'M': {'hex': '#ffad51', 'temp': 3000, 'name': 'Vermelho'},
        }
        
        # Cores dos planetas e corpos celestes (baseadas em observações reais)
        self.celestial_colors = {
            'sun': {'hex': '#ffeb3b', 'name': 'Amarelo Solar', 'magnitude': -26.7},
            'mercury': {'hex': '#8c7853', 'name': 'Cinza Rochoso', 'magnitude': -0.4},
            'venus': {'hex': '#ffc649', 'name': 'Dourado Brilhante', 'magnitude': -4.6},
            'mars': {'hex': '#cd5c5c', 'name': 'Vermelho Ferrugem', 'magnitude': -2.9},
            'jupiter': {'hex': '#d8ca9d', 'name': 'Bege Listrado', 'magnitude': -2.9},
            'saturn': {'hex': '#fab27b', 'name': 'Dourado Pálido', 'magnitude': 0.7},
            'uranus': {'hex': '#4fd0e7', 'name': 'Azul Gelo', 'magnitude': 5.7},
            'neptune': {'hex': '#4b70dd', 'name': 'Azul Profundo', 'magnitude': 7.8},
            'moon': {'hex': '#c0c0c0', 'name': 'Prata Lunar', 'magnitude': -12.6}
        }
        
        # Carregar catálogo otimizado
        self.load_optimized_catalog()
        
    def load_optimized_catalog(self):
        """Carrega catálogo otimizado focando nas estrelas mais relevantes"""
        try:
            with load.open(hipparcos.URL) as f:
                stars = hipparcos.load_dataframe(f)
            
            # Filtrar apenas estrelas brilhantes e relevantes (magnitude < 4.0)
            bright_stars = stars[stars['magnitude'] < 4.0].copy()
            bright_stars = bright_stars.dropna(subset=['ra_hours', 'dec_degrees', 'magnitude'])
            
            # Adicionar informações espectrais
            bright_stars['spectral_type'] = bright_stars['magnitude'].apply(self.estimate_spectral_type)
            bright_stars['color_info'] = bright_stars['spectral_type'].apply(self.get_spectral_info)
            bright_stars['ra_degrees'] = bright_stars['ra_hours'] * 15
            
            # Adicionar nomes de estrelas famosas
            star_names = self.get_famous_star_names()
            bright_stars['proper_name'] = bright_stars.index.map(star_names)
            
            self.stars_df = bright_stars
            print(f"Catálogo otimizado carregado com {len(bright_stars)} estrelas brilhantes")
            
        except Exception as e:
            print(f"Erro ao carregar catálogo: {e}")
            self.create_minimal_catalog()
    
    def create_minimal_catalog(self):
        """Catálogo mínimo com estrelas principais"""
        minimal_data = {
            'ra_hours': [6.75, 14.66, 18.62, 5.60, 7.58, 12.90, 16.49, 20.69, 10.90, 13.42],
            'dec_degrees': [-16.72, -60.84, 38.78, 7.41, 28.03, 11.97, 36.46, 45.28, 11.97, -11.17],
            'magnitude': [1.46, -0.74, 0.03, 0.87, 1.14, 2.23, 1.25, 2.02, 1.85, 2.06],
            'spectral_type': ['A', 'F', 'A', 'M', 'G', 'K', 'A', 'A', 'K', 'B'],
            'proper_name': ['Sirius', 'Canopus', 'Vega', 'Betelgeuse', 'Capella', 'Arcturus', 'Altair', 'Deneb', 'Regulus', 'Spica']
        }
        
        self.stars_df = pd.DataFrame(minimal_data)
        self.stars_df['ra_degrees'] = self.stars_df['ra_hours'] * 15
        self.stars_df['color_info'] = self.stars_df['spectral_type'].apply(self.get_spectral_info)
    
    def get_famous_star_names(self):
        """Retorna dicionário expandido com nomes de estrelas famosas"""
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
            49669: "Bellatrix",   # Gamma Orionis
            27989: "Elnath",      # Beta Tauri
        }
    
    def estimate_spectral_type(self, magnitude):
        """Estima tipo espectral mais preciso baseado na magnitude"""
        # Distribuição mais realista dos tipos espectrais
        if magnitude < -1:
            return 'O'
        elif magnitude < 0:
            return 'B'
        elif magnitude < 1:
            return 'A'
        elif magnitude < 2:
            return 'F'
        elif magnitude < 2.5:
            return 'G'
        elif magnitude < 3.5:
            return 'K'
        else:
            return 'M'
    
    def get_spectral_info(self, spectral_type):
        """Retorna informações completas do tipo espectral"""
        if isinstance(spectral_type, str) and len(spectral_type) > 0:
            return self.spectral_colors.get(spectral_type[0], self.spectral_colors['G'])
        return self.spectral_colors['G']
    
    def angular_distance(self, ra1, dec1, ra2, dec2):
        """Calcula distância angular entre duas posições"""
        ra1, dec1, ra2, dec2 = map(math.radians, [ra1, dec1, ra2, dec2])
        
        cos_dist = (math.sin(dec1) * math.sin(dec2) + 
                   math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2))
        
        cos_dist = max(-1, min(1, cos_dist))
        return math.degrees(math.acos(cos_dist))
    
    def get_top_celestial_objects(self, zenith_ra, zenith_dec, birth_datetime, latitude, longitude, count=25):
        """Obtém as 25 estrelas mais relevantes próximas ao zênite para um céu mais realista"""
        objects = []
        
        # Apenas estrelas próximas ao zênite
        if self.stars_df is not None and not self.stars_df.empty:
            # Calcular distâncias ao zênite
            distances = []
            for _, star in self.stars_df.iterrows():
                dist = self.angular_distance(zenith_ra, zenith_dec, 
                                           star['ra_degrees'], star['dec_degrees'])
                distances.append(dist)
            
            self.stars_df['distance_to_zenith'] = distances
            
            # Incluir TODAS as estrelas dentro de 90 graus, não apenas as com nomes
            visible_stars = self.stars_df[
                self.stars_df['distance_to_zenith'] <= 90
            ].copy()
            
            if not visible_stars.empty:
                # Priorizar por: 1) Proximidade ao zênite, 2) Brilho
                visible_stars['priority'] = (
                    (90 - visible_stars['distance_to_zenith']) * 10 +  # Proximidade
                    (6 - visible_stars['magnitude']) * 5  # Brilho
                )
                
                # Separar estrelas com nomes das sem nomes
                named_stars = visible_stars[visible_stars['proper_name'].notna()]
                unnamed_stars = visible_stars[visible_stars['proper_name'].isna()]
                
                # Pegar as top 15 estrelas com nomes
                top_named = named_stars.nlargest(15, 'priority') if not named_stars.empty else pd.DataFrame()
                
                # Pegar as top 10 estrelas sem nomes mais brilhantes
                top_unnamed = unnamed_stars.nlargest(10, 'priority') if not unnamed_stars.empty else pd.DataFrame()
                
                # Combinar ambas
                top_stars = pd.concat([top_named, top_unnamed])
                
                for _, star in top_stars.iterrows():
                    # Calcular cor mais realista baseada na magnitude e tipo espectral
                    color_info = self.calculate_realistic_star_color(star['magnitude'], star['spectral_type'])
                    
                    # Nome da estrela ou designação genérica
                    star_name = star['proper_name'] if pd.notna(star['proper_name']) else f"HIP {star.name}" if star.name else f"Estrela #{len(objects)+1}"
                    
                    objects.append({
                        'name': star_name,
                        'type': 'star',
                        'ra': star['ra_degrees'],
                        'dec': star['dec_degrees'],
                        'magnitude': star['magnitude'],
                        'distance_to_zenith': star['distance_to_zenith'],
                        'color': color_info['hex'],
                        'color_name': color_info['name'],
                        'temperature': color_info['temp'],
                        'spectral_type': star['spectral_type'],
                        'priority': star['priority'],
                        'brightness_factor': color_info['brightness_factor']
                    })
        
        # Ordenar por prioridade
        objects.sort(key=lambda x: x.get('priority', 0), reverse=True)
        return objects[:count]  # Limitar ao count solicitado
    
    def calculate_realistic_star_color(self, magnitude, spectral_type):
        """Calcula cor mais realista baseada na magnitude e tipo espectral com maior contraste"""
        # Obter informações espectrais básicas
        base_color = self.get_spectral_info(spectral_type)
        
        # Calcular fator de brilho baseado na magnitude (estrelas mais brilhantes = cores mais saturadas)
        # Magnitude menor = mais brilhante = fator maior
        brightness_factor = max(0.3, min(1.0, (6 - magnitude) / 6))
        
        # Converter hex para RGB
        hex_color = base_color['hex'].lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # Converter para HSV para manipular saturação e valor
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        # Ajustar saturação e valor baseado na magnitude
        # Estrelas mais brilhantes ficam mais saturadas e claras
        s = min(1.0, s + brightness_factor * 0.4)  # Aumentar saturação
        v = min(1.0, v + brightness_factor * 0.3)  # Aumentar brilho
        
        # Adicionar variação baseada na temperatura para maior contraste
        temp = base_color['temp']
        if temp > 10000:  # Estrelas muito quentes - azul mais intenso
            h = 0.67  # Azul puro
            s = min(1.0, s + 0.3)
        elif temp > 7000:  # Estrelas quentes - azul-branco
            h = 0.6
            s = min(1.0, s + 0.2)
        elif temp > 6000:  # Estrelas como o Sol - branco-amarelo
            h = 0.15
            s = min(1.0, s + 0.1)
        elif temp > 4000:  # Estrelas frias - laranja
            h = 0.08
            s = min(1.0, s + 0.2)
        else:  # Estrelas muito frias - vermelho
            h = 0.0
            s = min(1.0, s + 0.3)
        
        # Converter de volta para RGB
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        
        # Converter para hex
        final_hex = f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
        
        # Determinar nome da cor baseado na temperatura e brilho
        color_names = {
            'very_hot': 'Azul Estelar Intenso',
            'hot': 'Branco-Azulado Brilhante', 
            'warm': 'Amarelo Solar Radiante',
            'cool': 'Laranja Cósmico',
            'cold': 'Vermelho Profundo'
        }
        
        if temp > 10000:
            color_name = color_names['very_hot']
        elif temp > 7000:
            color_name = color_names['hot']
        elif temp > 6000:
            color_name = color_names['warm']
        elif temp > 4000:
            color_name = color_names['cool']
        else:
            color_name = color_names['cold']
        
        # Adicionar indicador de brilho ao nome
        if magnitude < 1.0:
            color_name += " (Superbrilhante)"
        elif magnitude < 2.0:
            color_name += " (Muito Brilhante)"
        elif magnitude < 3.0:
            color_name += " (Brilhante)"
        
        return {
            'hex': final_hex,
            'name': color_name,
            'temp': temp,
            'brightness_factor': brightness_factor
        }
    
    def generate_modern_sky_data(self, zenith_ra, zenith_dec, zenith_star, birth_datetime, latitude, longitude):
        """Gera dados do céu moderno com a constelação real"""
        
        # Estrela principal (zenith)
        stars = [{
            'name': zenith_star['name'],
            'ra': zenith_star['ra_degrees'],
            'dec': zenith_star['dec_degrees'],
            'magnitude': zenith_star['magnitude'],
            'isZenith': True,
            'x': 0,  # Centro do canvas
            'y': 0,
            'size': self._calculate_star_size(zenith_star['magnitude']),
            'color': zenith_star.get('color', '#ffffff')
        }]
        
        # Adicionar estrelas da constelação
        if 'constellation_stars' in zenith_star:
            constellation_stars = zenith_star['constellation_stars']
            
            # Converter coordenadas das estrelas da constelação para posições relativas
            zenith_ra_rad = math.radians(zenith_ra)
            zenith_dec_rad = math.radians(zenith_dec)
            
            for const_star in constellation_stars:
                if const_star['name'] != zenith_star['name']:  # Não duplicar a estrela principal
                    # Calcular posição relativa à estrela do zênite
                    ra_rad = math.radians(const_star['ra'])
                    dec_rad = math.radians(const_star['dec'])
                    
                    # Projeção estereográfica simplificada
                    delta_ra = ra_rad - zenith_ra_rad
                    
                    # Fator de escala para caber no canvas (ajustável)
                    scale = 100
                    
                    x = scale * math.sin(delta_ra) * math.cos(dec_rad)
                    y = scale * (math.sin(dec_rad) * math.cos(zenith_dec_rad) - 
                               math.cos(dec_rad) * math.sin(zenith_dec_rad) * math.cos(delta_ra))
                    
                    stars.append({
                        'name': const_star['name'],
                        'ra': const_star['ra'],
                        'dec': const_star['dec'],
                        'magnitude': const_star['mag'],
                        'isZenith': False,
                        'x': x,
                        'y': -y,  # Inverter Y para corresponder ao canvas
                        'size': self._calculate_star_size(const_star['mag']),
                        'color': self._get_star_color_by_magnitude(const_star['mag'])
                    })
        
        # Adicionar algumas estrelas de fundo fracas para ambiente
        random.seed(f"{zenith_ra}{zenith_dec}")  # Seed consistente
        
        for i in range(15):  # Menos estrelas de fundo
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(150, 280)  # Mais distantes do centro
            
            stars.append({
                'name': f'background-{i}',
                'ra': 0,
                'dec': 0,
                'magnitude': random.uniform(5, 7),
                'isZenith': False,
                'x': distance * math.cos(angle),
                'y': distance * math.sin(angle),
                'size': random.uniform(0.5, 1.5),
                'color': '#666666'
            })
        
        # Linhas da constelação
        constellation_lines = []
        
        # Definir conexões básicas para algumas constelações conhecidas
        constellation_patterns = {
            'Orion': [
                ['Betelgeuse', 'Bellatrix'],
                ['Betelgeuse', 'Alnitak'],
                ['Bellatrix', 'Alnilam'],
                ['Alnitak', 'Alnilam'],
                ['Alnilam', 'Rigel'],
                ['Alnitak', 'Saiph'],
                ['Rigel', 'Saiph']
            ],
            'Ursa Major': [
                ['Dubhe', 'Merak'],
                ['Merak', 'Phecda'],
                ['Phecda', 'Megrez'],
                ['Megrez', 'Alioth'],
                ['Alioth', 'Mizar'],
                ['Mizar', 'Alkaid'],
                ['Megrez', 'Dubhe']
            ],
            'Leo': [
                ['Regulus', 'Algieba'],
                ['Algieba', 'Zosma'],
                ['Zosma', 'Denebola'],
                ['Denebola', 'Theta Leo'],
                ['Theta Leo', 'Regulus'],
                ['Algieba', 'Adhafera']
            ],
            'Scorpius': [
                ['Antares', 'Tau Sco'],
                ['Tau Sco', 'Epsilon Sco'],
                ['Epsilon Sco', 'Mu Sco'],
                ['Mu Sco', 'Zeta Sco'],
                ['Antares', 'Sigma Sco'],
                ['Sigma Sco', 'Alpha Sco']
            ],
            'Cygnus': [
                ['Deneb', 'Sadr'],
                ['Sadr', 'Gienah'],
                ['Sadr', 'Delta Cyg'],
                ['Sadr', 'Albireo']
            ]
        }
        
        # Se temos um padrão para esta constelação, usar
        constellation_name = zenith_star.get('constellation', '')
        if constellation_name in constellation_patterns:
            pattern = constellation_patterns[constellation_name]
            
            # Criar mapa de nomes para índices
            star_indices = {star['name']: i for i, star in enumerate(stars)}
            
            for connection in pattern:
                star1_name, star2_name = connection
                if star1_name in star_indices and star2_name in star_indices:
                    constellation_lines.append({
                        'from': star_indices[star1_name],
                        'to': star_indices[star2_name]
                    })
        else:
            # Conectar estrelas mais brilhantes da constelação genericamente
            bright_stars = [i for i, star in enumerate(stars) 
                           if star['magnitude'] < 4 and not star['name'].startswith('background')]
            
            if len(bright_stars) > 1:
                # Conectar estrelas próximas
                for i in range(len(bright_stars)):
                    for j in range(i + 1, len(bright_stars)):
                        star1 = stars[bright_stars[i]]
                        star2 = stars[bright_stars[j]]
                        
                        # Calcular distância
                        dist = math.sqrt((star1['x'] - star2['x'])**2 + (star1['y'] - star2['y'])**2)
                        
                        # Conectar apenas estrelas próximas
                        if dist < 150:  # Threshold ajustável
                            constellation_lines.append({
                                'from': bright_stars[i],
                                'to': bright_stars[j]
                            })
        
        return {
            'stars': stars,
            'constellation_lines': constellation_lines,
            'projection_info': {
                'center_ra': zenith_ra,
                'center_dec': zenith_dec,
                'fov': 30,  # Campo de visão em graus
                'rotation': self._calculate_rotation(birth_datetime, latitude, longitude)
            },
            'constellation_name': constellation_name,
            'total_stars': len(stars)
        }

    def _get_star_color_by_magnitude(self, magnitude):
        """Retorna cor baseada na magnitude"""
        if magnitude < 0:
            return '#E6F3FF'  # Azul muito brilhante
        elif magnitude < 1:
            return '#D6E7FF'  # Azul brilhante  
        elif magnitude < 2:
            return '#FFFFFF'  # Branco
        elif magnitude < 3:
            return '#FFF7E6'  # Branco-amarelado
        elif magnitude < 4:
            return '#FFE4B5'  # Amarelado
        else:
            return '#888888'  # Cinza para estrelas fracas

    def _calculate_star_size(self, magnitude):
        """Calcula tamanho baseado na magnitude"""
        if magnitude < -4:  # Vênus no máximo brilho
            return 30
        elif magnitude < -2:  # Júpiter, Marte
            return 25
        elif magnitude < 2:  # Saturno
            return 20
        else:  # Urano, Netuno (mais fracos)
            return 15

    def _calculate_rotation(self, birth_datetime, latitude, longitude):
        """Calcula rotação do céu baseada na data e localização"""
        # Implemente a lógica para calcular a rotação do céu com base na data e localização
        # Isso pode envolver cálculos astronômicos complexos
        return 0  # Placeholder, implemente a lógica real

    def calculate_visual_size(self, magnitude, obj_type):
        """Calcula tamanho visual baseado na magnitude e tipo com proporcionalidade adequada"""
        if obj_type == 'sun':
            # Sol é o maior objeto visível
            return 50
        elif obj_type == 'moon':
            # Lua é o segundo maior
            return 35
        elif obj_type == 'planet':
            # Planetas variam por magnitude, mas são maiores que estrelas
            if magnitude < -4:  # Vênus no máximo brilho
                return 30
            elif magnitude < -2:  # Júpiter, Marte
                return 25
            elif magnitude < 2:  # Saturno
                return 20
            else:  # Urano, Netuno (mais fracos)
                return 15
        else:
            # Estrelas: escala logarítmica inversa baseada na magnitude
            base_size = 18
            size = base_size * (10 ** (-magnitude / 2.5))
            return max(6, min(size, 30)) 