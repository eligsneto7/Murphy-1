"""
Astro Data para Murphy-1
Funções para gerar dados astronômicos e astrológicos
"""

from datetime import datetime, timedelta
import random
import math
import ephem

# Combine all event lists into a single ASTRONOMICAL_EVENTS list
RECURRING_EVENTS = [
    # Chuvas de meteoros principais
    {'date_range': [(1, 1, 1, 5)], 'event': 'Chuva de meteoros Quadrântidas', 'type': 'meteoros', 'intensity': 'intensa'},
    {'date_range': [(4, 16, 4, 25)], 'event': 'Chuva de meteoros Líridas', 'type': 'meteoros', 'intensity': 'moderada'},
    {'date_range': [(5, 4, 5, 17)], 'event': 'Chuva de meteoros Eta Aquáridas (restos do Cometa Halley)', 'type': 'meteoros', 'intensity': 'moderada'},
    {'date_range': [(7, 17, 8, 24)], 'event': 'Chuva de meteoros Delta Aquáridas', 'type': 'meteoros', 'intensity': 'fraca'},
    {'date_range': [(8, 11, 8, 13)], 'event': 'Chuva de meteoros Perseidas (Lágrimas de São Lourenço)', 'type': 'meteoros', 'intensity': 'intensa'},
    {'date_range': [(10, 8, 10, 10)], 'event': 'Chuva de meteoros Dracônidas', 'type': 'meteoros', 'intensity': 'variável'},
    {'date_range': [(10, 21, 10, 22)], 'event': 'Chuva de meteoros Oriônidas (também do Halley)', 'type': 'meteoros', 'intensity': 'moderada'},
    {'date_range': [(11, 5, 11, 12)], 'event': 'Chuva de meteoros Táuridas Sul', 'type': 'meteoros', 'intensity': 'fraca'},
    {'date_range': [(11, 12, 11, 20)], 'event': 'Chuva de meteoros Táuridas Norte', 'type': 'meteoros', 'intensity': 'fraca'},
    {'date_range': [(11, 17, 11, 18)], 'event': 'Chuva de meteoros Leônidas', 'type': 'meteoros', 'intensity': 'variável'},
    {'date_range': [(12, 13, 12, 14)], 'event': 'Chuva de meteoros Gemínidas', 'type': 'meteoros', 'intensity': 'intensa'},
    {'date_range': [(12, 22, 12, 23)], 'event': 'Chuva de meteoros Úrsidas', 'type': 'meteoros', 'intensity': 'fraca'},
    
    # Equinócios e solstícios
    {'date_range': [(3, 19, 3, 21)], 'event': 'Equinócio de Outono (Hemisfério Sul) - dia e noite iguais', 'type': 'equinócio', 'intensity': 'significativo'},
    {'date_range': [(6, 20, 6, 22)], 'event': 'Solstício de Inverno (Hemisfério Sul) - noite mais longa', 'type': 'solstício', 'intensity': 'significativo'},
    {'date_range': [(9, 22, 9, 24)], 'event': 'Equinócio de Primavera (Hemisfério Sul) - renovação', 'type': 'equinócio', 'intensity': 'significativo'},
    {'date_range': [(12, 20, 12, 22)], 'event': 'Solstício de Verão (Hemisfério Sul) - dia mais longo', 'type': 'solstício', 'intensity': 'significativo'},
    
    # Fenômenos lunares
    {'date_range': [(1, 31, 1, 31)], 'event': 'Superlua Azul (rara lua cheia dupla no mês)', 'type': 'lunar', 'intensity': 'raro'},
    {'date_range': [(2, 29, 2, 29)], 'event': 'nascimento em ano bissexto - dia extra do calendário', 'type': 'calendário', 'intensity': 'especial'},
    
    # Constelações zodiacais
    {'date_range': [(3, 21, 4, 19)], 'event': 'Sol em Áries - início do ano astrológico', 'type': 'zodíaco', 'intensity': 'astrológico'},
    {'date_range': [(4, 20, 5, 20)], 'event': 'Sol em Touro - constelação do Touro celeste', 'type': 'zodíaco', 'intensity': 'astrológico'},
    {'date_range': [(5, 21, 6, 20)], 'event': 'Sol em Gêmeos - os gêmeos Castor e Pollux', 'type': 'zodíaco', 'intensity': 'astrológico'},
    {'date_range': [(6, 21, 7, 22)], 'event': 'Sol em Câncer - aglomerado da Colmeia visível', 'type': 'zodíaco', 'intensity': 'astrológico'},
    {'date_range': [(7, 23, 8, 22)], 'event': 'Sol em Leão - próximo a Regulus', 'type': 'zodíaco', 'intensity': 'astrológico'},
    {'date_range': [(8, 23, 9, 22)], 'event': 'Sol em Virgem - próximo a Spica', 'type': 'zodíaco', 'intensity': 'astrológico'},
    {'date_range': [(9, 23, 10, 22)], 'event': 'Sol em Libra - equilíbrio celestial', 'type': 'zodíaco', 'intensity': 'astrológico'},
    {'date_range': [(10, 23, 11, 21)], 'event': 'Sol em Escorpião - próximo a Antares', 'type': 'zodíaco', 'intensity': 'astrológico'},
    {'date_range': [(11, 22, 12, 21)], 'event': 'Sol em Sagitário - centro galáctico', 'type': 'zodíaco', 'intensity': 'astrológico'},
    
    # Fenômenos raros
    {'date_range': [(2, 14, 2, 14)], 'event': 'alinhamento de Vênus e Júpiter no Dia dos Namorados', 'type': 'conjunção', 'intensity': 'romântico'},
    {'date_range': [(5, 5, 5, 5)], 'event': 'pico da chuva Eta Aquáridas no 05/05', 'type': 'numerologia', 'intensity': 'místico'},
    {'date_range': [(7, 7, 7, 7)], 'event': 'dia 07/07 - alinhamento numérico especial', 'type': 'numerologia', 'intensity': 'místico'},
    {'date_range': [(8, 8, 8, 8)], 'event': 'Portal do Leão 08/08 - energia cósmica intensa', 'type': 'místico', 'intensity': 'espiritual'},
    {'date_range': [(9, 9, 9, 9)], 'event': 'dia 09/09 - portal numerológico', 'type': 'numerologia', 'intensity': 'místico'},
    {'date_range': [(11, 11, 11, 11)], 'event': 'Portal 11/11 - alinhamento energético', 'type': 'místico', 'intensity': 'espiritual'},
    {'date_range': [(12, 12, 12, 12)], 'event': 'dia 12/12 - conclusão de ciclo anual', 'type': 'numerologia', 'intensity': 'místico'},
]

HISTORICAL_EVENTS_BY_DECADE = {
    1940: [
        {'year': 1945, 'month': 8, 'day': 6, 'event': 'detonação da primeira bomba atômica mudou a humanidade', 'type': 'nuclear'},
        {'year': 1947, 'month': 7, 'day': 8, 'event': 'Incidente de Roswell despertou interesse por OVNIs', 'type': 'mistério'},
        {'year': 1947, 'month': 10, 'day': 14, 'event': 'Chuck Yeager quebrou a barreira do som', 'type': 'aviação'},
    ],
    1950: [
        {'year': 1957, 'month': 10, 'day': 4, 'event': 'lançamento do Sputnik 1 iniciou a Era Espacial', 'type': 'espacial'},
        {'year': 1958, 'month': 1, 'day': 31, 'event': 'lançamento do Explorer 1 descobriu os cinturões de Van Allen', 'type': 'espacial'},
        {'year': 1959, 'month': 9, 'day': 14, 'event': 'Luna 2 foi o primeiro objeto humano a tocar a Lua', 'type': 'lunar'},
    ],
    1960: [
        {'year': 1961, 'month': 4, 'day': 12, 'event': 'Yuri Gagarin se tornou o primeiro humano no espaço', 'type': 'espacial'},
        {'year': 1962, 'month': 2, 'day': 20, 'event': 'John Glenn foi o primeiro americano a orbitar a Terra', 'type': 'espacial'},
        {'year': 1963, 'month': 6, 'day': 16, 'event': 'Valentina Tereshkova foi a primeira mulher no espaço', 'type': 'espacial'},
        {'year': 1965, 'month': 3, 'day': 18, 'event': 'Alexei Leonov fez a primeira caminhada espacial', 'type': 'espacial'},
        {'year': 1967, 'month': 1, 'day': 27, 'event': 'tragédia da Apollo 1 mudou a segurança espacial', 'type': 'espacial'},
        {'year': 1969, 'month': 7, 'day': 20, 'event': 'Neil Armstrong pisou na Lua - "Um pequeno passo..."', 'type': 'lunar'},
    ],
    1970: [
        {'year': 1970, 'month': 4, 'day': 13, 'event': 'explosão da Apollo 13 - "Houston, we have a problem"', 'type': 'espacial'},
        {'year': 1971, 'month': 11, 'day': 14, 'event': 'Mariner 9 se tornou primeira sonda a orbitar Marte', 'type': 'planetário'},
        {'year': 1973, 'month': 11, 'day': 3, 'event': 'Mariner 10 foi lançada para estudar Mercúrio', 'type': 'planetário'},
        {'year': 1975, 'month': 7, 'day': 17, 'event': 'acoplamento Apollo-Soyuz simbolizou détente espacial', 'type': 'espacial'},
        {'year': 1976, 'month': 7, 'day': 20, 'event': 'Viking 1 pousou em Marte procurando vida', 'type': 'planetário'},
        {'year': 1977, 'month': 8, 'day': 20, 'event': 'lançamento da Voyager 2 para os planetas externos', 'type': 'espacial'},
        {'year': 1977, 'month': 9, 'day': 5, 'event': 'lançamento da Voyager 1 rumo ao espaço interestelar', 'type': 'espacial'},
        {'year': 1979, 'month': 3, 'day': 5, 'event': 'Voyager 1 descobriu vulcões ativos em Io', 'type': 'planetário'},
    ],
    1980: [
        {'year': 1981, 'month': 4, 'day': 12, 'event': 'primeiro voo do ônibus espacial Columbia', 'type': 'espacial'},
        {'year': 1983, 'month': 6, 'day': 18, 'event': 'Sally Ride foi a primeira americana no espaço', 'type': 'espacial'},
        {'year': 1986, 'month': 1, 'day': 24, 'event': 'Voyager 2 fez encontro histórico com Urano', 'type': 'planetário'},
        {'year': 1986, 'month': 1, 'day': 28, 'event': 'tragédia do Challenger comoveu o mundo', 'type': 'espacial'},
        {'year': 1986, 'month': 3, 'day': 6, 'event': 'passagem do Cometa Halley próximo à Terra', 'type': 'cometa'},
        {'year': 1987, 'month': 2, 'day': 23, 'event': 'Supernova 1987A explodiu visível a olho nu', 'type': 'supernova'},
        {'year': 1989, 'month': 3, 'day': 13, 'event': 'tempestade solar massiva causou blackout em Quebec', 'type': 'solar'},
        {'year': 1989, 'month': 8, 'day': 25, 'event': 'Voyager 2 chegou a Netuno', 'type': 'planetário'},
    ],
    1990: [
        {'year': 1990, 'month': 4, 'day': 24, 'event': 'lançamento do Telescópio Espacial Hubble', 'type': 'espacial'},
        {'year': 1992, 'month': 10, 'day': 6, 'event': 'descoberta do primeiro exoplaneta confirmado', 'type': 'descoberta'},
        {'year': 1994, 'month': 7, 'day': 16, 'event': 'Cometa Shoemaker-Levy 9 colidiu com Júpiter', 'type': 'impacto'},
        {'year': 1995, 'month': 12, 'day': 7, 'event': 'Galileo entrou em órbita de Júpiter', 'type': 'planetário'},
        {'year': 1996, 'month': 8, 'day': 7, 'event': 'anúncio de possível vida em meteorito marciano', 'type': 'vida'},
        {'year': 1997, 'month': 3, 'day': 23, 'event': 'Cometa Hale-Bopp no periélio - mais brilhante do século', 'type': 'cometa'},
        {'year': 1997, 'month': 7, 'day': 4, 'event': 'Mars Pathfinder pousou em Marte', 'type': 'planetário'},
        {'year': 1998, 'month': 11, 'day': 20, 'event': 'início da construção da ISS', 'type': 'espacial'},
        {'year': 1999, 'month': 8, 'day': 11, 'event': 'último eclipse solar total do milênio', 'type': 'eclipse'},
    ],
    2000: [
        {'year': 2001, 'month': 2, 'day': 12, 'event': 'sonda NEAR pousou no asteroide Eros', 'type': 'asteroide'},
        {'year': 2001, 'month': 4, 'day': 28, 'event': 'Dennis Tito foi o primeiro turista espacial', 'type': 'espacial'},
        {'year': 2003, 'month': 2, 'day': 1, 'event': 'tragédia do Columbia na reentrada', 'type': 'espacial'},
        {'year': 2003, 'month': 8, 'day': 27, 'event': 'maior aproximação de Marte em 60.000 anos', 'type': 'planetário'},
        {'year': 2003, 'month': 10, 'day': 15, 'event': 'China lançou primeiro taikonauta Yang Liwei', 'type': 'espacial'},
        {'year': 2004, 'month': 1, 'day': 4, 'event': 'Spirit pousou em Marte', 'type': 'planetário'},
        {'year': 2005, 'month': 1, 'day': 14, 'event': 'Huygens pousou em Titã', 'type': 'planetário'},
        {'year': 2006, 'month': 1, 'day': 19, 'event': 'New Horizons lançada rumo a Plutão', 'type': 'espacial'},
        {'year': 2006, 'month': 8, 'day': 24, 'event': 'Plutão foi reclassificado como planeta anão', 'type': 'planetário'},
        {'year': 2007, 'month': 10, 'day': 24, 'event': 'Cometa Holmes teve explosão visível a olho nu', 'type': 'cometa'},
    ],
    2010: [
        {'year': 2011, 'month': 3, 'day': 18, 'event': 'MESSENGER entrou em órbita de Mercúrio', 'type': 'planetário'},
        {'year': 2011, 'month': 7, 'day': 21, 'event': 'último voo do ônibus espacial (Atlantis)', 'type': 'espacial'},
        {'year': 2012, 'month': 5, 'day': 20, 'event': 'eclipse solar anular formou "anel de fogo"', 'type': 'eclipse'},
        {'year': 2012, 'month': 6, 'day': 6, 'event': 'último trânsito de Vênus do século XXI', 'type': 'trânsito'},
        {'year': 2012, 'month': 8, 'day': 6, 'event': 'Curiosity pousou em Marte', 'type': 'planetário'},
        {'year': 2013, 'month': 2, 'day': 15, 'event': 'meteoro de Chelyabinsk explodiu sobre a Rússia', 'type': 'meteoro'},
        {'year': 2014, 'month': 11, 'day': 12, 'event': 'Philae pousou no cometa 67P', 'type': 'cometa'},
        {'year': 2015, 'month': 7, 'day': 14, 'event': 'New Horizons sobrevoou Plutão', 'type': 'planetário'},
        {'year': 2016, 'month': 2, 'day': 11, 'event': 'detecção de ondas gravitacionais confirmada', 'type': 'descoberta'},
        {'year': 2017, 'month': 8, 'day': 21, 'event': 'Grande Eclipse Americano atravessou os EUA', 'type': 'eclipse'},
        {'year': 2017, 'month': 10, 'day': 19, 'event': '\'Oumuamua primeiro objeto interestelar detectado', 'type': 'interestelar'},
        {'year': 2019, 'month': 1, 'day': 3, 'event': 'Chang\'e 4 pousou no lado oculto da Lua', 'type': 'lunar'},
        {'year': 2019, 'month': 4, 'day': 10, 'event': 'primeira imagem de buraco negro revelada', 'type': 'descoberta'},
    ],
    2020: [
        {'year': 2020, 'month': 5, 'day': 30, 'event': 'SpaceX lançou primeiros astronautas comerciais', 'type': 'espacial'},
        {'year': 2020, 'month': 7, 'day': 23, 'event': 'Cometa NEOWISE visível a olho nu', 'type': 'cometa'},
        {'year': 2020, 'month': 12, 'day': 21, 'event': 'Grande Conjunção Júpiter-Saturno "Estrela de Belém"', 'type': 'conjunção'},
        {'year': 2021, 'month': 2, 'day': 18, 'event': 'Perseverance pousou em Marte', 'type': 'planetário'},
        {'year': 2021, 'month': 4, 'day': 19, 'event': 'Ingenuity voou em Marte - primeiro voo em outro planeta', 'type': 'planetário'},
        {'year': 2021, 'month': 7, 'day': 11, 'event': 'Richard Branson foi ao espaço com Virgin Galactic', 'type': 'turismo'},
        {'year': 2021, 'month': 12, 'day': 25, 'event': 'Telescópio James Webb foi lançado', 'type': 'espacial'},
        {'year': 2022, 'month': 7, 'day': 12, 'event': 'primeiras imagens do James Webb reveladas', 'type': 'espacial'},
        {'year': 2022, 'month': 11, 'day': 16, 'event': 'Artemis I lançada - retorno à Lua', 'type': 'lunar'},
        {'year': 2023, 'month': 4, 'day': 20, 'event': 'Starship explodiu em primeiro voo orbital', 'type': 'espacial'},
    ]
}

SOLAR_EVENTS = [
    {'year': 1859, 'month': 9, 'day': 1, 'event': 'Evento Carrington - maior tempestade solar registrada', 'type': 'solar', 'category': 'solar'},
    {'year': 1921, 'month': 5, 'day': 15, 'event': 'Grande Tempestade Geomagnética de 1921', 'type': 'solar', 'category': 'solar'},
    {'year': 1989, 'month': 3, 'day': 13, 'event': 'tempestade solar causou blackout em Quebec', 'type': 'solar', 'category': 'solar'},
    {'year': 2003, 'month': 10, 'day': 28, 'event': 'explosão solar X17.2 - Halloween Storm', 'type': 'solar', 'category': 'solar'},
    {'year': 2012, 'month': 7, 'day': 23, 'event': 'super tempestade solar passou perto da Terra', 'type': 'solar', 'category': 'solar'},
]

COMET_EVENTS = [
    {'year': 1910, 'month': 5, 'day': 19, 'event': 'passagem do Cometa Halley causou pânico mundial', 'type': 'cometa', 'category': 'comet'},
    {'year': 1965, 'month': 10, 'day': 20, 'event': 'Cometa Ikeya-Seki - mais brilhante do século XX', 'type': 'cometa', 'category': 'comet'},
    {'year': 1996, 'month': 3, 'day': 22, 'event': 'Cometa Hyakutake passou muito próximo da Terra', 'type': 'cometa', 'category': 'comet'},
    {'year': 1997, 'month': 4, 'day': 1, 'event': 'Cometa Hale-Bopp no auge - visível por 18 meses', 'type': 'cometa', 'category': 'comet'},
    {'year': 2007, 'month': 1, 'day': 12, 'event': 'Cometa McNaught - mais brilhante em 40 anos', 'type': 'cometa', 'category': 'comet'},
]

RANDOM_EVENT_TEMPLATES = [
    'aumento incomum na atividade solar detectado',
    'alinhamento raro de Vênus, Marte e Júpiter',
    'descoberta de novo exoplaneta potencialmente habitável',
    'passagem do asteroide próximo à órbita terrestre',
    'aurora boreal visível em latitudes incomuns',
    'superlua especialmente brilhante e próxima',
    'conjunção planetária formando triângulo celeste',
    'máximo de manchas solares do ciclo de 11 anos',
    'descoberta de nova galáxia anã orbitando a Via Láctea',
    'detecção de sinal de rádio misterioso do espaço profundo',
    'eclipse lunar penumbral sutil',
    'chuva de meteoros esporádica inesperada',
    'descoberta de novo cometa por astrônomo amador',
    'ocultação de estrela brilhante pela Lua',
    'trânsito da ISS visível a olho nu',
    'flash de raios gama detectado de galáxia distante',
    'descoberta de água em lua de Júpiter',
    'formação de nova estrela em nebulosa próxima',
    'pulsar emitindo sinais incomuns detectado',
    'asteroide binário descoberto próximo à Terra'
]

# Consolidate all events into a single list for easier access
# This list can be used by other modules directly
ASTRONOMICAL_EVENTS = []
ASTRONOMICAL_EVENTS.extend(RECURRING_EVENTS)

# Add historical events, processing them to fit a common structure if needed
for decade, events_in_decade in HISTORICAL_EVENTS_BY_DECADE.items():
    for event_details in events_in_decade:
        ASTRONOMICAL_EVENTS.append({
            'event': event_details['event'],
            'type': event_details['type'],
            'year': event_details['year'],
            'month': event_details['month'],
            'day': event_details['day'],
            'category': 'historical' # Add a category to distinguish
        })

ASTRONOMICAL_EVENTS.extend(SOLAR_EVENTS) # Assuming solar events have a compatible structure or are processed
ASTRONOMICAL_EVENTS.extend(COMET_EVENTS) # Assuming comet events have a compatible structure

# For random events, we might want to keep them as templates or generate a few examples
# For now, let's add them as templates if they are to be used directly,
# or handle their generation within get_astronomical_coincidences if that's preferred.
# If ASTRONOMICAL_EVENTS is meant to be a static list, pre-generate some.
# Example:
# for i in range(5): # Add 5 random example events
#     ASTRONOMICAL_EVENTS.append({
#         'event': random.choice(RANDOM_EVENT_TEMPLATES),
#         'type': 'fenômeno_aleatório',
#         'category': 'random_placeholder'
#     })


def generate_cosmic_message(zenith_star):
    """Gera uma mensagem cósmica personalizada baseada na estrela do zênite"""
    star_name = zenith_star.get('name', 'sua estrela')
    constellation = zenith_star.get('constellation', 'uma constelação distante')
    
    messages = [
        f"No momento do seu nascimento, {star_name} brilhava diretamente acima de você, como um farol cósmico guiando sua jornada pela vida.",
        f"A luz de {star_name} em {constellation} testemunhou seus primeiros momentos neste mundo, criando uma conexão eterna entre você e o cosmos.",
        f"Enquanto você dava seus primeiros passos na Terra, {star_name} irradiava sua energia através do espaço-tempo, tecendo sua presença no tecido do universo.",
        f"No exato instante do seu nascimento, {star_name} ocupava a posição de honra no zênite celeste, marcando sua chegada com luz estelar."
    ]
    
    return random.choice(messages)


def generate_star_curiosities(star_name, distance_ly, magnitude, spectral_class):
    """Gera curiosidades sobre a estrela usando dados precisos"""
    from app.star_data_extended import NAMED_STARS
    
    # Se temos dados precisos para esta estrela
    if star_name in NAMED_STARS:
        star_data = NAMED_STARS[star_name]
        age_billion_years = star_data.get('age_billion_years', estimate_age_from_spectral(spectral_class))
        real_distance = star_data.get('distance_ly', distance_ly)
        history = star_data.get('history', f"{star_name} é uma estrela fascinante da classe {spectral_class}.")
        temperature = star_data.get('temperature_k', estimate_temperature_from_spectral(spectral_class))
        mass = star_data.get('mass_solar', estimate_mass_from_magnitude(magnitude))
    else:
        # Estimativas para estrelas genéricas
        age_billion_years = estimate_age_from_spectral(spectral_class)
        real_distance = distance_ly
        history = f"{star_name} é uma estrela fascinante da classe {spectral_class}."
        temperature = estimate_temperature_from_spectral(spectral_class)
        mass = estimate_mass_from_magnitude(magnitude)
    
    # Calcular idade em diferentes formatos
    age_millions = age_billion_years * 1000 if age_billion_years is not None else None
    age_years = age_billion_years * 1_000_000_000 if age_billion_years is not None else None
    
    # Determinar era de nascimento
    if age_billion_years is None:
        birth_era = "Era Desconhecida"
    elif age_billion_years > 12:
        birth_era = "Era Primordial do Universo"
    elif age_billion_years > 10:
        birth_era = "Era das Primeiras Galáxias"
    elif age_billion_years > 8:
        birth_era = "Era da Formação Galáctica"
    elif age_billion_years > 5:
        birth_era = "Era Pré-Solar"
    elif age_billion_years > 4.6:
        birth_era = "Era Pré-Sistema Solar"
    elif age_billion_years > 1:
        birth_era = "Era Solar (contemporânea ao Sol)"
    else:
        birth_era = "Era Moderna (estrela jovem)"
    
    # Mensagens temporais baseadas na idade real
    temporal_messages = []
    if age_billion_years is not None:
        if age_billion_years < 0.1:
            temporal_messages.append(f"{star_name} é uma estrela bebê em termos cósmicos")
        elif age_billion_years < 1:
            temporal_messages.append(f"{star_name} nasceu quando a vida já existia na Terra")
        elif age_billion_years < 4.6:
            temporal_messages.append(f"{star_name} é mais jovem que nosso Sol")
        elif age_billion_years > 10:
            temporal_messages.append(f"{star_name} é uma das estrelas mais antigas da galáxia")
        else:
            temporal_messages.append(f"{star_name} testemunhou a formação do Sistema Solar")
    else:
        temporal_messages.append(f"A idade de {star_name} é um mistério a ser desvendado.")
    
    # Fatos interessantes baseados em dados reais
    facts = []
    
    # Fatos sobre distância
    if real_distance is not None:
        if real_distance < 20:
            facts.append(f"É uma das 50 estrelas mais próximas da Terra")
        elif real_distance > 1000:
            facts.append(f"Sua luz viajou {real_distance:,.0f} anos para chegar até nós")
        else:
            facts.append(f"Está a {real_distance:.1f} anos-luz de distância")
    
    # Fatos sobre temperatura
    if temperature:
        if temperature > 20000:
            facts.append(f"Com {temperature:,}K, é mais quente que um raio")
        elif temperature > 10000:
            facts.append(f"Sua superfície de {temperature:,}K é azul-branca")
        elif temperature > 6000:
            facts.append(f"Temperatura similar ao Sol: {temperature:,}K")
        else:
            facts.append(f"Relativamente fria para uma estrela: {temperature:,}K")
    
    # Fatos sobre massa
    if mass:
        if mass > 10:
            facts.append(f"Com {mass:.1f} massas solares, terminará como supernova")
        elif mass > 2:
            facts.append(f"É {mass:.1f} vezes mais massiva que o Sol")
        elif mass < 0.5:
            facts.append(f"Anã vermelha que viverá trilhões de anos")
        else:
            facts.append(f"Massa similar ao Sol: {mass:.1f} massas solares")
    
    # Fatos sobre idade
    if age_billion_years is not None:
        if age_billion_years < 0.01:
            facts.append(f"Com apenas {age_millions:.0f} milhões de anos, ainda está se formando")
        elif age_billion_years > 10:
            facts.append(f"Nasceu apenas {13.8 - age_billion_years:.1f} bilhões de anos após o Big Bang")
    
    # Comparações temporais
    comparisons = []
    
    if age_billion_years is not None and age_billion_years > 4.6:
        comparisons.append(f"É {age_billion_years - 4.6:.1f} bilhões de anos mais velha que o Sol")
        comparisons.append(f"Quando {star_name} nasceu, o Sistema Solar não existia")
    elif age_billion_years is not None:
        comparisons.append(f"É {4.6 - age_billion_years:.1f} bilhões de anos mais jovem que o Sol")
    
    if real_distance is not None and real_distance < 100:
        comparisons.append(f"Sua luz começou a viagem quando {calculate_historical_event(real_distance)}")
    
    # Era quando a luz começou
    current_year = datetime.now().year
    light_start_year = current_year - int(real_distance) if real_distance is not None else current_year

    if real_distance is None:
        era_light = "em um passado desconhecido"
    elif light_start_year > 1900:
        era_light = f"em {light_start_year} (Era Moderna)"
    elif light_start_year > 1000:
        era_light = f"em {light_start_year} (Idade Média)"
    elif light_start_year > 0:
        era_light = f"em {light_start_year} d.C. (Era Clássica)"
    elif light_start_year > -3000:
        era_light = f"em {abs(light_start_year)} a.C. (Antigas Civilizações)"
    else:
        era_light = f"há {real_distance:,.0f} anos (Pré-História)"
    
    return {
        'age_formatted': f"{age_billion_years:.2f} bilhões de anos" if age_billion_years is not None else "Idade Desconhecida",
        'age_millions': f"{age_millions:,.0f} milhões de anos" if age_millions is not None else "Idade Desconhecida",
        'birth_era': birth_era,
        'temporal_message': temporal_messages[0] if temporal_messages else "Uma mensagem temporal aguarda.",
        'history': history,
        'fun_facts': facts[:4],
        'timeline_comparison': {
            'comparisons': comparisons,
            'era_when_light_started': era_light,
            'star_age_percent_of_universe': (age_billion_years / 13.8) * 100 if age_billion_years is not None else None
        },
        'real_age_billions': age_billion_years,
        'temperature_k': temperature,
        'mass_solar': mass
    }

def estimate_age_from_spectral(spectral_class):
    """Estima idade baseada na classe espectral"""
    if not spectral_class or not isinstance(spectral_class, str) or len(spectral_class) == 0:
        return 5.0
    
    spectral_type = spectral_class[0].upper()
    
    ages = {
        'O': 0.003,  # 3 milhões de anos
        'B': 0.01,   # 10 milhões de anos
        'A': 0.5,    # 500 milhões de anos
        'F': 3.0,    # 3 bilhões de anos
        'G': 5.0,    # 5 bilhões de anos (tipo Sol)
        'K': 10.0,   # 10 bilhões de anos
        'M': 15.0    # 15 bilhões de anos (podem viver trilhões)
    }
    
    return ages.get(spectral_type, 5.0)

def estimate_temperature_from_spectral(spectral_class):
    """Estima temperatura baseada na classe espectral"""
    if not spectral_class or not isinstance(spectral_class, str) or len(spectral_class) == 0:
        return 5778
    
    spectral_type = spectral_class[0].upper()
    
    temps = {
        'O': 30000,
        'B': 20000,
        'A': 8500,
        'F': 6500,
        'G': 5500,
        'K': 4000,
        'M': 3000
    }
    
    return temps.get(spectral_type, 5778)

def estimate_mass_from_magnitude(magnitude):
    """Estima massa baseada na magnitude (muito aproximado)"""
    if magnitude is None: return 1.0
    if magnitude < -1:
        return 20.0
    elif magnitude < 0:
        return 10.0
    elif magnitude < 1:
        return 3.0
    elif magnitude < 3:
        return 1.5
    elif magnitude < 5:
        return 1.0
    else:
        return 0.5

def calculate_historical_event(years_ago):
    """Retorna evento histórico baseado em anos atrás"""
    if years_ago is None: return "em um tempo imemorial"
    year = datetime.now().year - int(years_ago)
    
    events = {
        2020: "a pandemia de COVID-19 começava",
        2001: "aconteciam os ataques de 11 de setembro",
        1989: "caía o Muro de Berlim",
        1969: "o homem pisava na Lua",
        1945: "terminava a Segunda Guerra Mundial",
        1914: "começava a Primeira Guerra Mundial",
        1889: "era inaugurada a Torre Eiffel",
        1492: "Colombo chegava às Américas",
        1066: "ocorria a Batalha de Hastings",
        476: "caía o Império Romano do Ocidente",
        0: "nascia Cristo",
        -3000: "surgiam as primeiras civilizações",
        -10000: "começava a agricultura"
    }
    
    # Encontrar o evento mais próximo
    closest_year = min(events.keys(), key=lambda x: abs(x - year))
    
    if abs(year - closest_year) < 50:
        return events[closest_year]
    else:
        if year > 0:
            return f"estávamos no ano {year} d.C."
        else:
            return f"estávamos no ano {abs(year)} a.C."


def get_astrology_data(birth_date, birth_time, latitude, longitude):
    """Gera dados astrológicos completos"""
    from app.astrology_calculator import AstrologyCalculator
    
    # Converter para datetime se necessário
    if isinstance(birth_date, str):
        birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    else:
        birth_datetime = datetime.combine(birth_date, datetime.strptime(birth_time, "%H:%M").time())
    
    calculator = AstrologyCalculator()
    return calculator.generate_cosmic_profile(birth_datetime, latitude, longitude)


def get_astronomical_coincidences(birth_date, birth_time, latitude, longitude):
    """Busca eventos astronômicos relevantes próximos à data de nascimento"""
    if isinstance(birth_date, str):
        birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    else:
        birth_datetime = datetime.combine(birth_date, datetime.strptime(birth_time, "%H:%M").time())
    
    year = birth_datetime.year
    month = birth_datetime.month
    day = birth_datetime.day
    
    coincidences = []
    
    # Process global ASTRONOMICAL_EVENTS
    for event_data in ASTRONOMICAL_EVENTS:
        if 'date_range' in event_data: # Recurring event
            for date_r in event_data['date_range']:
                start_month, start_day, end_month, end_day = date_r
                
                # Create datetime objects for comparison, handling year wrap-around for end_date if needed
                # This logic assumes date_range is within a single year or spans across year-end correctly.
                # For simplicity, let's assume ranges are within the same year for now.
                # More robust logic would handle ranges like (12, 15, 1, 10)
                event_period_start = datetime(year, start_month, start_day)
                event_period_end = datetime(year, end_month, end_day)
                birth_date_this_year = datetime(year, month, day)

                is_during = False
                if start_month <= end_month: # Typical case, e.g., April 16 to April 25
                    if event_period_start <= birth_date_this_year <= event_period_end:
                        is_during = True
                else: # Range wraps around year end, e.g., Dec 22 to Jan 5
                    if birth_date_this_year >= event_period_start or birth_date_this_year <= event_period_end:
                        is_during = True
                
                days_diff = 0
                if is_during:
                    coincidences.append({
                        'event': event_data['event'], 'type': event_data['type'],
                        'days_diff': 0, 'during': True
                    })
                    break # Matched this recurring event
                else: # Check proximity if not during
                    # Calculate difference to the start and end of the event period
                    # (More complex if we want to find closest day within the range)
                    diff_to_start = (birth_date_this_year - event_period_start).days
                    diff_to_end = (birth_date_this_year - event_period_end).days
                    
                    closest_diff = None
                    if abs(diff_to_start) < abs(diff_to_end):
                        closest_diff = diff_to_start
                    else:
                        closest_diff = diff_to_end
                    
                    if abs(closest_diff) <= 7: # Within 7 days
                         coincidences.append({
                            'event': event_data['event'], 'type': event_data['type'],
                            'days_diff': closest_diff, 'during': False
                        })
                         break # Added proximity match

        elif 'year' in event_data: # Dated event (historical, solar, comet)
            event_dt = datetime(event_data['year'], event_data['month'], event_data['day'])
            diff_days = (birth_datetime - event_dt).days
            
            proximity_window = 730 # Default to ~2 years for solar/comet/historical
            if event_data.get('category') == 'historical': proximity_window = 1825 # ~5 years for historical
            if event_data.get('type') == 'supernova': proximity_window = 3650 # ~10 years for supernova

            if abs(diff_days) <= proximity_window:
                coincidences.append({
                    'event': event_data['event'], 'type': event_data['type'],
                    'days_diff': diff_days, 'during': (diff_days == 0),
                    'historical': True # Mark as historical/dated
                })

    # Add random events using global templates
    random.seed(f"{year}{month}{day}") # Seed for consistent randomness per day
    if random.random() < 0.6: # 60% chance
        days_offset = random.randint(-15, 15)
        coincidences.append({
            'event': random.choice(RANDOM_EVENT_TEMPLATES),
            'type': 'fenômeno_aleatório', 'days_diff': days_offset, 'during': (days_offset==0)
        })
    if random.random() < 0.3: # 30% chance for a second one
        days_offset = random.randint(-30, 30)
        coincidences.append({
            'event': random.choice(RANDOM_EVENT_TEMPLATES),
            'type': 'descoberta_aleatória', 'days_diff': days_offset, 'during': (days_offset==0)
        })

    coincidences.sort(key=lambda x: (abs(x['days_diff']), x['event'])) # Sort by diff, then event name
    
    return coincidences[:3] if coincidences else [{
        'event': 'um período de calmaria cósmica incomum, perfeito para introspecção.',
        'type': 'raro', 'days_diff': 0, 'during': True
    }]

# ===== CÁLCULOS LUNARES AVANÇADOS =====
def calculate_moon_phase(birth_date, birth_time, latitude, longitude):
    """Calcula fase da lua e dados lunares para o momento do nascimento"""
    try:
        # Criar observador
        observer = ephem.Observer()
        observer.lat = str(latitude)
        observer.lon = str(longitude)
        observer.date = f"{birth_date} {birth_time}"
        
        # Lua
        moon = ephem.Moon()
        moon.compute(observer)
        
        # Calcular fase da lua (0 = nova, 1 = cheia)
        phase = moon.moon_phase
        
        # Determinar nome da fase
        if phase < 0.1:
            phase_name = "🌑 Lua Nova"
            phase_description = "Um novo começo, energia de renovação e potencial infinito"
            mystical_meaning = "Nascido sob a Lua Nova, você carrega o poder dos novos começos e da manifestação"
        elif phase < 0.25:
            phase_name = "🌒 Lua Crescente"
            phase_description = "Crescimento, expansão e construção de sonhos"
            mystical_meaning = "A energia crescente da lua reflete em sua natureza progressiva e ambiciosa"
        elif phase < 0.4:
            phase_name = "🌓 Quarto Crescente"
            phase_description = "Momento de decisões e superação de desafios"
            mystical_meaning = "Você possui a força para superar obstáculos e tomar decisões importantes"
        elif phase < 0.6:
            phase_name = "🌔 Lua Gibosa Crescente"
            phase_description = "Refinamento e preparação para a plenitude"
            mystical_meaning = "Sua alma busca constantemente o aperfeiçoamento e a evolução"
        elif phase < 0.75:
            phase_name = "🌕 Lua Cheia"
            phase_description = "Plenitude, intuição máxima e realização"
            mystical_meaning = "Nascido na Lua Cheia, você possui intuição poderosa e energia magnética"
        elif phase < 0.9:
            phase_name = "🌖 Lua Gibosa Minguante"
            phase_description = "Gratidão, compartilhamento e sabedoria"
            mystical_meaning = "Você é um guardião de sabedoria, destinado a ensinar e guiar outros"
        else:
            phase_name = "🌗 Quarto Minguante"
            phase_description = "Liberação, perdão e transformação"
            mystical_meaning = "Sua alma tem o dom da transformação e da cura de velhas feridas"
        
        # Distância da Terra
        distance_km = moon.earth_distance * 149597870.7  # Converter UA para km
        
        # Próxima lua cheia/nova
        next_full = ephem.next_full_moon(observer.date)
        next_new = ephem.next_new_moon(observer.date)
        
        return {
            'phase': phase,
            'phase_percentage': round(phase * 100, 1),
            'phase_name': phase_name,
            'phase_description': phase_description,
            'mystical_meaning': mystical_meaning,
            'distance_km': round(distance_km),
            'altitude': round(math.degrees(moon.alt), 1),
            'azimuth': round(math.degrees(moon.az), 1),
            'next_full_moon': str(next_full)[:10],
            'next_new_moon': str(next_new)[:10],
            'constellation': moon.constellation[1] if hasattr(moon, 'constellation') else 'N/A'
        }
        
    except Exception as e:
        print(f"Erro no cálculo lunar: {e}")
        return {
            'phase': 0.5,
            'phase_percentage': 50,
            'phase_name': "🌕 Lua Misteriosa",
            'phase_description': "Os segredos lunares aguardam para serem revelados",
            'mystical_meaning': "Sua conexão com a lua transcende o tempo e o espaço",
            'distance_km': 384400,
            'altitude': 45,
            'azimuth': 180,
            'next_full_moon': "Em breve",
            'next_new_moon': "Em breve",
            'constellation': 'Cósmica'
        }

# ===== CÁLCULOS DE MARÉS =====
def calculate_tidal_influence(birth_date, birth_time, latitude, longitude):
    """Calcula influência das marés no momento do nascimento"""
    try:
        observer = ephem.Observer()
        observer.lat = str(latitude)
        observer.lon = str(longitude)
        observer.date = f"{birth_date} {birth_time}"
        
        # Lua e Sol para cálculo das marés
        moon = ephem.Moon()
        sun = ephem.Sun()
        moon.compute(observer)
        sun.compute(observer)
        
        # Força gravitacional da lua (simplificado)
        moon_distance = moon.earth_distance
        moon_force = 1 / (moon_distance ** 3)  # Lei do inverso do quadrado
        
        # Força gravitacional do sol
        sun_distance = sun.earth_distance
        sun_force = 0.46 / (sun_distance ** 3)  # Sol tem 0.46x a força das marés da lua
        
        # Combinação das forças
        total_force = moon_force + sun_force
        
        # Tipo de maré baseado na posição relativa
        moon_sun_angle = abs(moon.ra - sun.ra)
        if moon_sun_angle < 0.5 or moon_sun_angle > 5.8:
            tide_type = "🌊 Maré de Sizígia"
            tide_description = "Marés extremas - força gravitacional máxima"
            personal_influence = "Você nasceu sob influência gravitacional intensa, o que pode indicar uma personalidade magnética e impactante"
        elif 1.4 < moon_sun_angle < 1.8 or 4.6 < moon_sun_angle < 5.0:
            tide_type = "🌀 Maré de Quadratura"
            tide_description = "Marés moderadas - forças em equilíbrio"
            personal_influence = "As forças cósmicas em equilíbrio no seu nascimento sugerem uma natureza equilibrada e harmoniosa"
        else:
            tide_type = "🌊 Maré Mista"
            tide_description = "Marés variadas - influências cósmicas complexas"
            personal_influence = "A complexidade das forças cósmicas reflete em sua personalidade multifacetada e única"
        
        return {
            'type': tide_type,
            'description': tide_description,
            'personal_influence': personal_influence,
            'moon_force': round(moon_force * 1000, 2),
            'sun_force': round(sun_force * 1000, 2),
            'total_force': round(total_force * 1000, 2),
            'gravitational_intensity': 'Alta' if total_force > 0.003 else 'Moderada' if total_force > 0.002 else 'Suave'
        }
        
    except Exception as e:
        print(f"Erro no cálculo de marés: {e}")
        return {
            'type': "🌊 Maré Cósmica",
            'description': "Influências gravitacionais misteriosas",
            'personal_influence': "Você está conectado aos ritmos profundos do oceano cósmico",
            'moon_force': 2.5,
            'sun_force': 1.1,
            'total_force': 3.6,
            'gravitational_intensity': 'Mística'
        }

# ===== HORÓSCOPO E ASTROLOGIA =====
def calculate_astrological_profile(birth_date, birth_time, latitude, longitude):
    """Calcula perfil astrológico completo"""
    try:
        observer = ephem.Observer()
        observer.lat = str(latitude)
        observer.lon = str(longitude)
        observer.date = f"{birth_date} {birth_time}"
        
        # Calcular posições planetárias
        planets_data = {}
        
        planets = {
            'Sol': ephem.Sun(),
            'Lua': ephem.Moon(),
            'Mercúrio': ephem.Mercury(),
            'Vênus': ephem.Venus(),
            'Marte': ephem.Mars(),
            'Júpiter': ephem.Jupiter(),
            'Saturno': ephem.Saturn(),
            'Urano': ephem.Uranus(),
            'Netuno': ephem.Neptune()
        }
        
        for name, planet in planets.items():
            planet.compute(observer)
            constellation = planet.constellation[1] if hasattr(planet, 'constellation') else 'Desconhecida'
            
            planets_data[name] = {
                'constellation': constellation,
                'altitude': round(math.degrees(planet.alt), 1),
                'azimuth': round(math.degrees(planet.az), 1),
                'visible': planet.alt > 0
            }
        
        # Determinar signo solar (simplificado baseado na data)
        birth_dt = datetime.strptime(birth_date, "%Y-%m-%d")
        day_of_year = birth_dt.timetuple().tm_yday
        
        zodiac_signs = [
            (20, "♈ Áries", "Energia de fogo, liderança natural, pioneirismo"),
            (49, "♉ Touro", "Estabilidade terrena, determinação, sensualidade"),
            (80, "♊ Gêmeos", "Versatilidade mental, comunicação, curiosidade"),
            (111, "♋ Câncer", "Intuição emocional, proteção, sensibilidade"),
            (142, "♌ Leão", "Criatividade radiante, generosidade, liderança"),
            (173, "♍ Virgem", "Precisão analítica, serviço, perfeição"),
            (204, "♎ Libra", "Harmonia social, beleza, diplomacia"),
            (234, "♏ Escorpião", "Intensidade transformadora, mistério, paixão"),
            (265, "♐ Sagitário", "Expansão filosófica, aventura, sabedoria"),
            (296, "♑ Capricórnio", "Ambição estrutural, responsabilidade, tradição"),
            (326, "♒ Aquário", "Inovação humanitária, independência, visão futura"),
            (356, "♓ Peixes", "Intuição oceânica, compaixão, espiritualidade"),
            (366, "♈ Áries", "Energia de fogo, liderança natural, pioneirismo")  # Wraparound
        ]
        
        sun_sign = "♈ Áries"
        sun_description = "Energia cósmica única"
        
        for day_limit, sign, description in zodiac_signs:
            if day_of_year <= day_limit:
                sun_sign = sign
                sun_description = description
                break
        
        # Elemento e qualidade
        elements = {
            '♈': ('Fogo', 'Iniciação'),
            '♌': ('Fogo', 'Fixo'),
            '♐': ('Fogo', 'Mutável'),
            '♉': ('Terra', 'Fixo'),
            '♍': ('Terra', 'Mutável'),
            '♑': ('Terra', 'Iniciação'),
            '♊': ('Ar', 'Mutável'),
            '♎': ('Ar', 'Iniciação'),
            '♒': ('Ar', 'Fixo'),
            '♋': ('Água', 'Iniciação'),
            '♏': ('Água', 'Fixo'),
            '♓': ('Água', 'Mutável')
        }
        
        sign_symbol = sun_sign.split()[0]
        element, quality = elements.get(sign_symbol, ('Éter', 'Transcendente'))
        
        return {
            'sun_sign': sun_sign,
            'sun_description': sun_description,
            'element': element,
            'quality': quality,
            'planets': planets_data,
            'dominant_planet': max(planets_data.keys(), key=lambda p: planets_data[p]['altitude']),
            'astrological_summary': f"Nascido sob {sun_sign}, com elemento {element} dominante, você carrega a essência cósmica da {quality.lower()}."
        }
        
    except Exception as e:
        print(f"Erro no cálculo astrológico: {e}")
        return {
            'sun_sign': "⭐ Cósmico",
            'sun_description': "Energia estelar única que transcende classificações terrestres",
            'element': 'Éter',
            'quality': 'Transcendente',
            'planets': {},
            'dominant_planet': 'Estrela Zenital',
            'astrological_summary': "Sua essência cósmica vai além dos signos tradicionais, conectando-se diretamente às estrelas."
        }

# ===== EVENTOS ESTELARES HISTÓRICOS =====
def calculate_stellar_events(birth_date, birth_time):
    """Calcula eventos estelares significativos próximos à data de nascimento"""
    try:
        birth_dt = datetime.strptime(birth_date, "%Y-%m-%d")
        
        # Eventos astronômicos históricos marcantes
        historical_events = [
            (datetime(1969, 7, 20), "🚀 Primeira Caminhada Lunar", "A humanidade deu seus primeiros passos na Lua"),
            (datetime(1977, 8, 20), "🛸 Lançamento da Voyager", "Mensageiro da Terra rumo às estrelas"),
            (datetime(1990, 4, 24), "🔭 Lançamento do Hubble", "Olhos da humanidade no cosmos"),
            (datetime(1995, 12, 7), "🌍 Primeiro Exoplaneta", "Descoberta de mundos além do Sistema Solar"),
            (datetime(2012, 8, 5), "🤖 Curiosity em Marte", "Robô explorador alcança o Planeta Vermelho"),
            (datetime(2019, 4, 10), "⚫ Primeira Foto de Buraco Negro", "A humanidade vê o invisível"),
            (datetime(2021, 2, 18), "🚁 Helicóptero em Marte", "Primeiro voo em outro planeta"),
            (datetime(1986, 1, 28), "🚀 Desafio da Tragédia Challenger", "Lembrete da coragem dos exploradores espaciais"),
            (datetime(1997, 7, 4), "🛸 Mars Pathfinder", "Primeiro rover moderno em Marte"),
            (datetime(2003, 2, 1), "🛸 Columbia", "Honrando os heróis da exploração espacial")
        ]
        
        # Encontrar evento mais próximo
        closest_event = None
        min_diff = float('inf')
        
        for event_date, event_name, event_description in historical_events:
            diff = abs((birth_dt - event_date).days)
            if diff < min_diff:
                min_diff = diff
                closest_event = {
                    'name': event_name,
                    'description': event_description,
                    'date': event_date.strftime("%d/%m/%Y"),
                    'days_difference': min_diff,
                    'cosmic_connection': ""
                }
        
        if closest_event and min_diff <= 365:  # Evento no mesmo ano
            if min_diff <= 30:
                closest_event['cosmic_connection'] = f"Apenas {min_diff} dias separam seu nascimento deste marco cósmico. Uma sincronia extraordinária!"
            elif min_diff <= 90:
                closest_event['cosmic_connection'] = f"Nascido {min_diff} dias após este evento histórico, você carrega sua energia transformadora."
            else:
                closest_event['cosmic_connection'] = f"O mesmo ano cósmico que testemunhou {closest_event['name']} também celebrou seu nascimento."
        
        # Eventos astronômicos por período do ano
        seasonal_events = {
            'primavera': "🌸 Equinócio de Primavera - Renovação e crescimento cósmico",
            'verao': "☀️ Solstício de Verão - Energia solar máxima",
            'outono': "🍂 Equinócio de Outono - Equilíbrio e transformação",
            'inverno': "❄️ Solstício de Inverno - Introspecção e renascimento"
        }
        
        month = birth_dt.month
        if month in [3, 4, 5]:
            seasonal_event = seasonal_events['primavera']
        elif month in [6, 7, 8]:
            seasonal_event = seasonal_events['verao']
        elif month in [9, 10, 11]:
            seasonal_event = seasonal_events['outono']
        else:
            seasonal_event = seasonal_events['inverno']
        
        return {
            'historical_event': closest_event,
            'seasonal_energy': seasonal_event,
            'birth_year_significance': f"O ano de {birth_dt.year} marca um momento único na jornada cósmica da humanidade."
        }
        
    except Exception as e:
        print(f"Erro no cálculo de eventos estelares: {e}")
        return {
            'historical_event': {
                'name': "🌟 Evento Cósmico Único",
                'description': "Seu nascimento é um marco no tempo cósmico",
                'date': birth_date,
                'cosmic_connection': "Você é parte da grande narrativa do cosmos."
            },
            'seasonal_energy': "✨ Energia Cósmica Universal",
            'birth_year_significance': "Cada nascimento é um evento único no universo."
        }

__all__ = [
    'generate_cosmic_message', 
    'generate_star_curiosities', 
    'get_astrology_data',
    'get_astronomical_coincidences',
    'ASTRONOMICAL_EVENTS', # Export the global list
    'estimate_age_from_spectral', # Export helpers if used by other modules
    'estimate_temperature_from_spectral',
    'estimate_mass_from_magnitude',
    'calculate_historical_event',
    'calculate_moon_phase',
    'calculate_tidal_influence',
    'calculate_astrological_profile',
    'calculate_stellar_events'
] 