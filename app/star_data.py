"""
Star Data - Dados detalhados de estrelas conhecidas e constelações
"""

# Dados precisos de estrelas conhecidas com nomes próprios
NAMED_STARS = {
    'Sirius': {
        'hip': 32349,
        'constellation': 'Canis Major',
        'magnitude': -1.46,
        'distance_ly': 8.6,
        'spectral_class': 'A1V',
        'ra_degrees': 101.287,
        'dec_degrees': -16.716,
        'age_billion_years': 0.242,
        'mass_solar': 2.02,
        'temperature_k': 9940,
        'history': """Sirius, a estrela mais brilhante do céu noturno, foi reverenciada por civilizações antigas. 
        Para os egípcios, seu surgimento helíaco marcava a inundação anual do Nilo. É um sistema binário, 
        com uma anã branca companheira (Sirius B) descoberta em 1862. Conhecida como 'Estrela do Cão' pelos gregos.""",
        'constellation_stars': [
            {'name': 'Sirius', 'ra': 101.287, 'dec': -16.716, 'mag': -1.46},
            {'name': 'Mirzam', 'ra': 95.674, 'dec': -17.956, 'mag': 1.98},
            {'name': 'Wezen', 'ra': 107.098, 'dec': -26.393, 'mag': 1.84},
            {'name': 'Adhara', 'ra': 104.656, 'dec': -28.972, 'mag': 1.50},
            {'name': 'Aludra', 'ra': 111.023, 'dec': -29.303, 'mag': 2.45}
        ]
    },
    'Vega': {
        'hip': 91262,
        'constellation': 'Lyra',
        'magnitude': 0.03,
        'distance_ly': 25.04,
        'spectral_class': 'A0V',
        'ra_degrees': 279.234,
        'dec_degrees': 38.784,
        'age_billion_years': 0.455,
        'mass_solar': 2.135,
        'temperature_k': 9602,
        'history': """Vega foi a estrela polar há 12.000 anos e voltará a sê-la em 13.727 d.C. devido à precessão. 
        Foi a primeira estrela fotografada (1850) e a primeira a ter seu espectro registrado. Serviu como 
        padrão de magnitude zero. Carl Sagan escolheu Vega como origem do sinal alienígena em 'Contato'.""",
        'constellation_stars': [
            {'name': 'Vega', 'ra': 279.234, 'dec': 38.784, 'mag': 0.03},
            {'name': 'Sheliak', 'ra': 282.520, 'dec': 33.363, 'mag': 3.25},
            {'name': 'Sulafat', 'ra': 284.736, 'dec': 32.690, 'mag': 3.24},
            {'name': 'Delta Lyr', 'ra': 283.626, 'dec': 36.899, 'mag': 4.30}
        ]
    },
    'Arcturus': {
        'hip': 69673,
        'constellation': 'Boötes',
        'magnitude': -0.05,
        'distance_ly': 36.7,
        'spectral_class': 'K1.5III',
        'ra_degrees': 213.915,
        'dec_degrees': 19.182,
        'age_billion_years': 7.1,
        'mass_solar': 1.08,
        'temperature_k': 4286,
        'history': """Arcturus é uma das estrelas mais antigas do halo galáctico, possivelmente capturada de uma 
        galáxia anã absorvida pela Via Láctea. Em 1933, sua luz captada 40 anos antes foi usada para abrir 
        a Feira Mundial de Chicago. Move-se rapidamente pelo céu, deslocando-se um diâmetro lunar a cada 800 anos.""",
        'constellation_stars': [
            {'name': 'Arcturus', 'ra': 213.915, 'dec': 19.182, 'mag': -0.05},
            {'name': 'Izar', 'ra': 221.247, 'dec': 27.074, 'mag': 2.37},
            {'name': 'Muphrid', 'ra': 208.671, 'dec': 18.398, 'mag': 2.68},
            {'name': 'Seginus', 'ra': 218.019, 'dec': 38.308, 'mag': 3.03}
        ]
    },
    'Capella': {
        'hip': 24608,
        'constellation': 'Auriga',
        'magnitude': 0.08,
        'distance_ly': 42.9,
        'spectral_class': 'G3III',
        'ra_degrees': 79.172,
        'dec_degrees': 45.998,
        'age_billion_years': 0.590,
        'mass_solar': 2.69,
        'temperature_k': 4970,
        'history': """Capella é um complexo sistema de seis estrelas. As duas principais são gigantes amarelas 
        que orbitam uma à outra a cada 104 dias. Na mitologia, representa Amalteia, a cabra que amamentou Zeus. 
        É a estrela mais brilhante mais próxima do polo norte celeste, visível durante todo o ano no hemisfério norte.""",
        'constellation_stars': [
            {'name': 'Capella', 'ra': 79.172, 'dec': 45.998, 'mag': 0.08},
            {'name': 'Menkalinan', 'ra': 89.882, 'dec': 44.948, 'mag': 1.90},
            {'name': 'Mahasim', 'ra': 74.248, 'dec': 33.166, 'mag': 2.69},
            {'name': 'Haedus', 'ra': 76.629, 'dec': 41.076, 'mag': 3.75}
        ]
    },
    'Rigel': {
        'hip': 24436,
        'constellation': 'Orion',
        'magnitude': 0.13,
        'distance_ly': 860,
        'spectral_class': 'B8Ia',
        'ra_degrees': 78.634,
        'dec_degrees': -8.202,
        'age_billion_years': 0.008,
        'mass_solar': 21,
        'temperature_k': 11000,
        'history': """Rigel é uma supergigante azul 40.000 vezes mais luminosa que o Sol. Seu nome vem do árabe 
        'Rijl Jauza al Yusra', significando 'o pé esquerdo de Órion'. É um sistema múltiplo com pelo menos 
        quatro estrelas. Apesar de ser Beta Orionis, geralmente é mais brilhante que Betelgeuse (Alpha).""",
        'constellation_stars': [
            {'name': 'Rigel', 'ra': 78.634, 'dec': -8.202, 'mag': 0.13},
            {'name': 'Betelgeuse', 'ra': 88.793, 'dec': 7.407, 'mag': 0.50},
            {'name': 'Bellatrix', 'ra': 81.283, 'dec': 6.350, 'mag': 1.64},
            {'name': 'Alnilam', 'ra': 84.053, 'dec': -1.202, 'mag': 1.70},
            {'name': 'Alnitak', 'ra': 85.190, 'dec': -1.943, 'mag': 1.77}
        ]
    },
    'Procyon': {
        'hip': 37279,
        'constellation': 'Canis Minor',
        'magnitude': 0.37,
        'distance_ly': 11.5,
        'spectral_class': 'F5IV',
        'ra_degrees': 114.826,
        'dec_degrees': 5.225,
        'age_billion_years': 1.87,
        'mass_solar': 1.50,
        'temperature_k': 6530,
        'history': """Procyon, 'antes do cão' em grego, nasce antes de Sirius. É a oitava estrela mais brilhante 
        e uma das mais próximas. Como Sirius, tem uma anã branca companheira. Faz parte do Triângulo de Inverno 
        com Sirius e Betelgeuse. Os babilônios a chamavam de 'Estrela da Travessia das Águas'.""",
        'constellation_stars': [
            {'name': 'Procyon', 'ra': 114.826, 'dec': 5.225, 'mag': 0.37},
            {'name': 'Gomeisa', 'ra': 111.788, 'dec': 8.289, 'mag': 2.90}
        ]
    },
    'Betelgeuse': {
        'hip': 27989,
        'constellation': 'Orion',
        'magnitude': 0.50,
        'distance_ly': 548,
        'spectral_class': 'M1Ia',
        'ra_degrees': 88.793,
        'dec_degrees': 7.407,
        'age_billion_years': 0.010,
        'mass_solar': 18,
        'temperature_k': 3500,
        'history': """Betelgeuse é uma supergigante vermelha nos estágios finais de sua vida. Se estivesse no 
        lugar do Sol, engoliria as órbitas de todos os planetas até Júpiter. Pode explodir como supernova 
        a qualquer momento (astronomicamente falando). Seu nome vem do árabe 'Bait al-Jauza', 'casa de Órion'.""",
        'constellation_stars': [
            {'name': 'Betelgeuse', 'ra': 88.793, 'dec': 7.407, 'mag': 0.50},
            {'name': 'Rigel', 'ra': 78.634, 'dec': -8.202, 'mag': 0.13},
            {'name': 'Bellatrix', 'ra': 81.283, 'dec': 6.350, 'mag': 1.64},
            {'name': 'Alnilam', 'ra': 84.053, 'dec': -1.202, 'mag': 1.70},
            {'name': 'Alnitak', 'ra': 85.190, 'dec': -1.943, 'mag': 1.77}
        ]
    },
    'Altair': {
        'hip': 97649,
        'constellation': 'Aquila',
        'magnitude': 0.77,
        'distance_ly': 16.7,
        'spectral_class': 'A7V',
        'ra_degrees': 297.696,
        'dec_degrees': 8.868,
        'age_billion_years': 1.2,
        'mass_solar': 1.79,
        'temperature_k': 7377,
        'history': """Altair gira tão rapidamente (uma rotação a cada 9 horas) que é achatada nos polos. 
        Seu nome vem do árabe 'an-nasr at-ta'ir', 'a águia voadora'. Faz parte do Triângulo de Verão com 
        Vega e Deneb. Na mitologia chinesa, representa o pastor na história de amor dos Tanabata.""",
        'constellation_stars': [
            {'name': 'Altair', 'ra': 297.696, 'dec': 8.868, 'mag': 0.77},
            {'name': 'Tarazed', 'ra': 296.565, 'dec': 10.613, 'mag': 2.72},
            {'name': 'Alshain', 'ra': 298.828, 'dec': 6.407, 'mag': 3.71}
        ]
    },
    'Aldebaran': {
        'hip': 21421,
        'constellation': 'Taurus',
        'magnitude': 0.85,
        'distance_ly': 66.6,
        'spectral_class': 'K5III',
        'ra_degrees': 68.980,
        'dec_degrees': 16.509,
        'age_billion_years': 6.4,
        'mass_solar': 1.16,
        'temperature_k': 3910,
        'history': """Aldebaran, 'o seguidor' em árabe, segue as Plêiades pelo céu. É o 'olho do touro' em 
        Taurus. Foi uma das quatro 'estrelas reais' da Pérsia antiga. A sonda Pioneer 10, lançada em 1972, 
        chegará às proximidades de Aldebaran em cerca de 2 milhões de anos.""",
        'constellation_stars': [
            {'name': 'Aldebaran', 'ra': 68.980, 'dec': 16.509, 'mag': 0.85},
            {'name': 'Elnath', 'ra': 81.573, 'dec': 28.608, 'mag': 1.68},
            {'name': 'Alcyone', 'ra': 56.871, 'dec': 24.105, 'mag': 2.87},
            {'name': 'Tianguan', 'ra': 84.411, 'dec': 21.143, 'mag': 3.00}
        ]
    },
    'Spica': {
        'hip': 65474,
        'constellation': 'Virgo',
        'magnitude': 0.97,
        'distance_ly': 250,
        'spectral_class': 'B1III',
        'ra_degrees': 201.298,
        'dec_degrees': -11.161,
        'age_billion_years': 0.012,
        'mass_solar': 11.43,
        'temperature_k': 25300,
        'history': """Spica é uma estrela binária próxima cujas componentes orbitam a cada 4 dias. Seu nome 
        significa 'espiga de trigo' que a deusa Virgo segura. Foi observando Spica que Hiparco descobriu a 
        precessão dos equinócios em 2 a.C. É uma das estrelas mais quentes visíveis a olho nu.""",
        'constellation_stars': [
            {'name': 'Spica', 'ra': 201.298, 'dec': -11.161, 'mag': 0.97},
            {'name': 'Zavijava', 'ra': 177.674, 'dec': 1.765, 'mag': 3.61},
            {'name': 'Porrima', 'ra': 190.415, 'dec': -1.449, 'mag': 2.74},
            {'name': 'Vindemiatrix', 'ra': 195.544, 'dec': 10.959, 'mag': 2.83}
        ]
    },
    'Antares': {
        'hip': 80763,
        'constellation': 'Scorpius',
        'magnitude': 1.09,
        'distance_ly': 604,
        'spectral_class': 'M1.5Iab',
        'ra_degrees': 247.352,
        'dec_degrees': -26.432,
        'age_billion_years': 0.011,
        'mass_solar': 15,
        'temperature_k': 3400,
        'history': """Antares, 'rival de Marte' em grego, compete com o planeta em cor avermelhada. É uma das 
        maiores estrelas conhecidas - 700 vezes o diâmetro do Sol. Tem uma companheira azul-esverdeada que 
        orbita a cada 2.500 anos. No final da vida, explodirá numa supernova visível durante o dia.""",
        'constellation_stars': [
            {'name': 'Antares', 'ra': 247.352, 'dec': -26.432, 'mag': 1.09},
            {'name': 'Shaula', 'ra': 263.402, 'dec': -37.104, 'mag': 1.63},
            {'name': 'Sargas', 'ra': 264.330, 'dec': -42.998, 'mag': 1.87},
            {'name': 'Dschubba', 'ra': 240.083, 'dec': -22.622, 'mag': 2.32}
        ]
    },
    'Pollux': {
        'hip': 37826,
        'constellation': 'Gemini',
        'magnitude': 1.14,
        'distance_ly': 33.8,
        'spectral_class': 'K0III',
        'ra_degrees': 116.329,
        'dec_degrees': 28.026,
        'age_billion_years': 0.724,
        'mass_solar': 1.91,
        'temperature_k': 4666,
        'history': """Pollux é a estrela mais brilhante de Gêmeos, apesar de ser Beta Geminorum. Com Castor, 
        representa os gêmeos mitológicos. É a estrela mais próxima do Sol com um planeta confirmado. 
        Diferente de Castor (um sistema sêxtuplo), Pollux é uma estrela solitária gigante laranja.""",
        'constellation_stars': [
            {'name': 'Pollux', 'ra': 116.329, 'dec': 28.026, 'mag': 1.14},
            {'name': 'Castor', 'ra': 113.650, 'dec': 31.888, 'mag': 1.57},
            {'name': 'Alhena', 'ra': 99.428, 'dec': 16.399, 'mag': 1.90},
            {'name': 'Tejat', 'ra': 95.740, 'dec': 22.514, 'mag': 2.88}
        ]
    },
    'Fomalhaut': {
        'hip': 113368,
        'constellation': 'Piscis Austrinus',
        'magnitude': 1.16,
        'distance_ly': 25.1,
        'spectral_class': 'A3V',
        'ra_degrees': 344.413,
        'dec_degrees': -29.622,
        'age_billion_years': 0.44,
        'mass_solar': 1.92,
        'temperature_k': 8590,
        'history': """Fomalhaut, 'boca do peixe austral' em árabe, é cercada por um disco de detritos onde 
        foi fotografado um dos primeiros exoplanetas (Fomalhaut b). É a estrela mais brilhante do céu de 
        outono no hemisfério norte. Na Pérsia antiga, era uma das quatro 'Guardiãs do Céu'.""",
        'constellation_stars': [
            {'name': 'Fomalhaut', 'ra': 344.413, 'dec': -29.622, 'mag': 1.16},
            {'name': 'Epsilon PsA', 'ra': 336.020, 'dec': -27.044, 'mag': 4.17},
            {'name': 'Delta PsA', 'ra': 343.987, 'dec': -32.540, 'mag': 4.20}
        ]
    },
    'Deneb': {
        'hip': 102098,
        'constellation': 'Cygnus',
        'magnitude': 1.25,
        'distance_ly': 2616,
        'spectral_class': 'A2Ia',
        'ra_degrees': 310.358,
        'dec_degrees': 45.280,
        'age_billion_years': 0.010,
        'mass_solar': 19,
        'temperature_k': 8525,
        'history': """Deneb é uma das estrelas mais luminosas da galáxia - 200.000 vezes mais que o Sol. 
        Seu nome significa 'cauda' em árabe, marcando a cauda do Cisne. Será a estrela polar em 12.000 d.C. 
        Forma o Triângulo de Verão com Vega e Altair. Apesar da distância, é a 19ª estrela mais brilhante.""",
        'constellation_stars': [
            {'name': 'Deneb', 'ra': 310.358, 'dec': 45.280, 'mag': 1.25},
            {'name': 'Albireo', 'ra': 292.680, 'dec': 27.960, 'mag': 3.18},
            {'name': 'Sadr', 'ra': 305.557, 'dec': 40.257, 'mag': 2.20},
            {'name': 'Gienah', 'ra': 305.253, 'dec': 33.970, 'mag': 2.46}
        ]
    },
    'Regulus': {
        'hip': 49669,
        'constellation': 'Leo',
        'magnitude': 1.35,
        'distance_ly': 79.3,
        'spectral_class': 'B8IVn',
        'ra_degrees': 152.093,
        'dec_degrees': 11.967,
        'age_billion_years': 0.25,
        'mass_solar': 3.8,
        'temperature_k': 12460,
        'history': """Regulus, 'pequeno rei' em latim, marca o coração do Leão. É um sistema quádruplo. 
        A estrela principal gira tão rápido (uma vez a cada 16 horas) que tem forma oblata extrema. 
        Era uma das quatro 'estrelas reais' da Pérsia. Está quase exatamente na eclíptica.""",
        'constellation_stars': [
            {'name': 'Regulus', 'ra': 152.093, 'dec': 11.967, 'mag': 1.35},
            {'name': 'Denebola', 'ra': 177.265, 'dec': 14.572, 'mag': 2.14},
            {'name': 'Algieba', 'ra': 154.993, 'dec': 19.842, 'mag': 2.28},
            {'name': 'Zosma', 'ra': 168.527, 'dec': 20.524, 'mag': 2.56}
        ]
    }
}

# Função para buscar estrela nomeada mais próxima
def find_nearest_named_star(ra_degrees, dec_degrees):
    """Encontra a estrela com nome próprio mais próxima das coordenadas dadas"""
    import math
    
    def angular_distance(ra1, dec1, ra2, dec2):
        """Calcula distância angular entre duas posições"""
        ra1, dec1, ra2, dec2 = map(math.radians, [ra1, dec1, ra2, dec2])
        
        cos_dist = (math.sin(dec1) * math.sin(dec2) + 
                   math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2))
        
        cos_dist = max(-1, min(1, cos_dist))
        return math.degrees(math.acos(cos_dist))
    
    nearest_star = None
    min_distance = float('inf')
    
    for star_name, star_data in NAMED_STARS.items():
        dist = angular_distance(ra_degrees, dec_degrees, 
                              star_data['ra_degrees'], star_data['dec_degrees'])
        
        if dist < min_distance:
            min_distance = dist
            nearest_star = star_name
    
    return nearest_star, min_distance, NAMED_STARS[nearest_star] 