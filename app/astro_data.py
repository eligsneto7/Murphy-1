"""
Astro Data para Murphy-1
Funções para gerar dados astronômicos e astrológicos
"""

from datetime import datetime
import random


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
    """Gera curiosidades sobre a estrela"""
    # Calcular idade estimada (muito simplificado)
    age_millions = distance_ly * 10  # Estimativa grosseira
    
    # Determinar era de nascimento
    if age_millions > 10000:
        birth_era = "Era Primordial do Universo"
    elif age_millions > 5000:
        birth_era = "Era das Primeiras Galáxias"
    elif age_millions > 1000:
        birth_era = "Era Pré-Solar"
    else:
        birth_era = "Era Contemporânea"
    
    # Mensagem temporal
    temporal_messages = [
        f"Esta estrela brilha há {age_millions} milhões de anos",
        f"Quando {star_name} nasceu, o universo era muito diferente",
        f"A luz que vemos hoje começou sua jornada há {distance_ly} anos"
    ]
    
    # História da estrela
    histories = [
        f"{star_name} é uma estrela fascinante com características únicas que a tornam especial no cosmos.",
        f"Localizada a {distance_ly} anos-luz de distância, {star_name} é um farol luminoso em nossa galáxia.",
        f"Com sua magnitude de {magnitude}, {star_name} é uma das estrelas mais notáveis do céu noturno."
    ]
    
    # Fatos interessantes
    facts = [
        f"Está localizada a {distance_ly} anos-luz da Terra",
        f"Sua magnitude aparente é {magnitude}",
        f"Pertence à classe espectral {spectral_class}",
        f"A luz que vemos hoje saiu da estrela há {distance_ly} anos",
        f"É aproximadamente {age_millions} milhões de anos mais antiga que nosso Sol"
    ]
    
    return {
        'age_formatted': f"{age_millions} milhões de anos",
        'birth_era': birth_era,
        'temporal_message': random.choice(temporal_messages),
        'history': random.choice(histories),
        'fun_facts': random.sample(facts, min(3, len(facts))),
        'timeline_comparison': {
            'comparisons': [
                f"Quando {star_name} nasceu, a Terra ainda não existia",
                f"Esta estrela testemunhou a formação do Sistema Solar",
                f"A luz de {star_name} viajou por {distance_ly} anos para chegar até nós"
            ],
            'era_when_light_started': f"Há {distance_ly} anos"
        }
    }


def get_astrology_data(birth_date, birth_time, latitude, longitude):
    """Gera dados astrológicos completos"""
    from app.astrology_calculator import AstrologyCalculator
    
    # Converter para datetime se necessário
    if isinstance(birth_date, str):
        birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    else:
        birth_datetime = datetime.combine(birth_date, birth_time)
    
    # Usar o calculador de astrologia existente
    calculator = AstrologyCalculator()
    return calculator.generate_cosmic_profile(birth_datetime, latitude, longitude)


def get_astronomical_coincidences(birth_date, birth_time, latitude, longitude):
    """Busca eventos astronômicos relevantes próximos à data de nascimento"""
    from datetime import timedelta
    import random
    
    # Converter birth_date e birth_time para datetime
    if isinstance(birth_date, str):
        birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    else:
        birth_datetime = datetime.combine(birth_date, birth_time)
    
    year = birth_datetime.year
    month = birth_datetime.month
    day = birth_datetime.day
    
    # Base de eventos astronômicos por ano (repetitivos e únicos)
    recurring_events = [
        # Chuvas de meteoros
        {'date_range': [(1, 1, 1, 5)], 'event': 'Chuva de meteoros Quadrântidas', 'type': 'meteoros', 'intensity': 'intensa'},
        {'date_range': [(4, 16, 4, 25)], 'event': 'Chuva de meteoros Líridas', 'type': 'meteoros', 'intensity': 'moderada'},
        {'date_range': [(5, 4, 5, 17)], 'event': 'Chuva de meteoros Eta Aquáridas', 'type': 'meteoros', 'intensity': 'moderada'},
        {'date_range': [(7, 17, 8, 24)], 'event': 'Chuva de meteoros Delta Aquáridas', 'type': 'meteoros', 'intensity': 'fraca'},
        {'date_range': [(8, 11, 8, 13)], 'event': 'Chuva de meteoros Perseidas', 'type': 'meteoros', 'intensity': 'intensa'},
        {'date_range': [(10, 21, 10, 22)], 'event': 'Chuva de meteoros Oriônidas', 'type': 'meteoros', 'intensity': 'moderada'},
        {'date_range': [(11, 17, 11, 18)], 'event': 'Chuva de meteoros Leônidas', 'type': 'meteoros', 'intensity': 'variável'},
        {'date_range': [(12, 13, 12, 14)], 'event': 'Chuva de meteoros Gemínidas', 'type': 'meteoros', 'intensity': 'intensa'},
        
        # Equinócios e solstícios
        {'date_range': [(3, 19, 3, 21)], 'event': 'Equinócio de Outono (Hemisfério Sul)', 'type': 'equinócio', 'intensity': 'significativo'},
        {'date_range': [(6, 20, 6, 22)], 'event': 'Solstício de Inverno (Hemisfério Sul)', 'type': 'solstício', 'intensity': 'significativo'},
        {'date_range': [(9, 22, 9, 24)], 'event': 'Equinócio de Primavera (Hemisfério Sul)', 'type': 'equinócio', 'intensity': 'significativo'},
        {'date_range': [(12, 20, 12, 22)], 'event': 'Solstício de Verão (Hemisfério Sul)', 'type': 'solstício', 'intensity': 'significativo'},
    ]
    
    # Eventos históricos significativos por década
    historical_events = {
        1950: [
            {'year': 1957, 'month': 10, 'day': 4, 'event': 'lançamento do Sputnik 1, primeiro satélite artificial', 'type': 'espacial'},
            {'year': 1958, 'month': 1, 'day': 31, 'event': 'lançamento do Explorer 1, primeiro satélite americano', 'type': 'espacial'},
        ],
        1960: [
            {'year': 1961, 'month': 4, 'day': 12, 'event': 'Yuri Gagarin se tornou o primeiro humano no espaço', 'type': 'espacial'},
            {'year': 1965, 'month': 3, 'day': 18, 'event': 'primeira caminhada espacial por Alexei Leonov', 'type': 'espacial'},
            {'year': 1969, 'month': 7, 'day': 20, 'event': 'Neil Armstrong pisou na Lua pela primeira vez', 'type': 'lunar'},
        ],
        1970: [
            {'year': 1970, 'month': 4, 'day': 24, 'event': 'lançamento do primeiro satélite chinês', 'type': 'espacial'},
            {'year': 1971, 'month': 11, 'day': 14, 'event': 'Mariner 9 se tornou a primeira sonda a orbitar Marte', 'type': 'planetário'},
            {'year': 1977, 'month': 9, 'day': 5, 'event': 'lançamento da Voyager 1 rumo aos confins do Sistema Solar', 'type': 'espacial'},
        ],
        1980: [
            {'year': 1981, 'month': 4, 'day': 12, 'event': 'primeiro voo do ônibus espacial Columbia', 'type': 'espacial'},
            {'year': 1986, 'month': 1, 'day': 24, 'event': 'Voyager 2 fez seu encontro histórico com Urano', 'type': 'planetário'},
            {'year': 1986, 'month': 3, 'day': 6, 'event': 'passagem do Cometa Halley próximo à Terra', 'type': 'cometa'},
        ],
        1990: [
            {'year': 1990, 'month': 4, 'day': 24, 'event': 'lançamento do Telescópio Espacial Hubble', 'type': 'espacial'},
            {'year': 1995, 'month': 12, 'day': 7, 'event': 'Galileo entrou em órbita de Júpiter', 'type': 'planetário'},
            {'year': 1997, 'month': 7, 'day': 4, 'event': 'Mars Pathfinder pousou em Marte', 'type': 'planetário'},
        ],
        2000: [
            {'year': 2001, 'month': 2, 'day': 12, 'event': 'sonda NEAR pousou no asteroide Eros', 'type': 'asteroide'},
            {'year': 2003, 'month': 8, 'day': 27, 'event': 'maior aproximação de Marte em 60.000 anos', 'type': 'planetário'},
            {'year': 2006, 'month': 8, 'day': 24, 'event': 'Plutão foi reclassificado como planeta anão', 'type': 'planetário'},
        ],
        2010: [
            {'year': 2012, 'month': 8, 'day': 6, 'event': 'rover Curiosity pousou em Marte', 'type': 'planetário'},
            {'year': 2015, 'month': 7, 'day': 14, 'event': 'New Horizons fez o primeiro sobrevoo de Plutão', 'type': 'planetário'},
            {'year': 2017, 'month': 8, 'day': 21, 'event': 'Eclipse Solar Total atravessou os Estados Unidos', 'type': 'eclipse'},
            {'year': 2019, 'month': 4, 'day': 10, 'event': 'primeira imagem de um buraco negro foi revelada', 'type': 'descoberta'},
        ],
        2020: [
            {'year': 2020, 'month': 12, 'day': 21, 'event': 'Grande Conjunção de Júpiter e Saturno', 'type': 'conjunção'},
            {'year': 2021, 'month': 2, 'day': 18, 'event': 'rover Perseverance pousou em Marte', 'type': 'planetário'},
            {'year': 2022, 'month': 7, 'day': 12, 'event': 'primeiras imagens do Telescópio James Webb', 'type': 'espacial'},
        ]
    }
    
    # Tempestades solares significativas
    solar_storms = [
        {'year': 1859, 'month': 9, 'day': 1, 'event': 'Evento Carrington - maior tempestade solar registrada', 'type': 'solar'},
        {'year': 1921, 'month': 5, 'day': 15, 'event': 'Grande Tempestade Geomagnética', 'type': 'solar'},
        {'year': 1989, 'month': 3, 'day': 13, 'event': 'tempestade solar que causou blackout em Quebec', 'type': 'solar'},
        {'year': 2003, 'month': 10, 'day': 28, 'event': 'explosão solar X17.2, uma das maiores já registradas', 'type': 'solar'},
    ]
    
    coincidences = []
    
    # Verificar eventos recorrentes
    for event in recurring_events:
        for date_range in event['date_range']:
            start_month, start_day, end_month, end_day = date_range
            
            # Verificar se o nascimento está dentro do período
            if (month == start_month and day >= start_day) or \
               (month == end_month and day <= end_day) or \
               (start_month < month < end_month):
                days_diff = 0  # Durante o evento
                coincidences.append({
                    'event': event['event'],
                    'type': event['type'],
                    'days_diff': days_diff,
                    'during': True
                })
            else:
                # Verificar proximidade (até 7 dias antes ou depois)
                event_start = datetime(year, start_month, start_day)
                event_end = datetime(year, end_month, end_day)
                
                diff_start = (birth_datetime - event_start).days
                diff_end = (birth_datetime - event_end).days
                
                if -7 <= diff_start <= 7:
                    coincidences.append({
                        'event': event['event'],
                        'type': event['type'],
                        'days_diff': diff_start,
                        'during': False
                    })
                elif -7 <= diff_end <= 7:
                    coincidences.append({
                        'event': event['event'],
                        'type': event['type'],
                        'days_diff': diff_end,
                        'during': False
                    })
    
    # Verificar eventos históricos
    decade = (year // 10) * 10
    if decade in historical_events:
        for event in historical_events[decade]:
            if event['year'] == year:
                event_date = datetime(event['year'], event['month'], event['day'])
                diff = (birth_datetime - event_date).days
                
                if -30 <= diff <= 30:  # Dentro de 30 dias
                    coincidences.append({
                        'event': event['event'],
                        'type': event['type'],
                        'days_diff': diff,
                        'during': False,
                        'historical': True
                    })
    
    # Verificar tempestades solares
    for storm in solar_storms:
        if abs(storm['year'] - year) <= 2:  # Dentro de 2 anos
            storm_date = datetime(storm['year'], storm['month'], storm['day'])
            diff = (birth_datetime - storm_date).days
            
            if -365 <= diff <= 365:  # Dentro de 1 ano
                coincidences.append({
                    'event': storm['event'],
                    'type': storm['type'],
                    'days_diff': diff,
                    'during': False,
                    'historical': True
                })
    
    # Adicionar eventos astronômicos aleatórios baseados na data
    random.seed(f"{year}{month}{day}")  # Seed consistente para a mesma data
    
    random_events = [
        'aumento incomum na atividade solar',
        'alinhamento planetário raro',
        'descoberta de um novo exoplaneta',
        'passagem de um asteroide próximo à Terra',
        'aurora boreal visível em latitudes incomuns',
        'superlua especialmente brilhante',
        'conjunção planetária visível a olho nu',
        'máximo de atividade de manchas solares',
        'descoberta de uma nova galáxia próxima',
        'detecção de ondas gravitacionais'
    ]
    
    if random.random() > 0.7:  # 30% de chance
        days_offset = random.randint(-10, 10)
        coincidences.append({
            'event': random.choice(random_events),
            'type': 'fenômeno',
            'days_diff': days_offset,
            'during': False
        })
    
    # Ordenar por proximidade
    coincidences.sort(key=lambda x: abs(x['days_diff']))
    
    # Pegar o mais relevante
    if coincidences:
        best_match = coincidences[0]
        
        # Formatar mensagem
        if best_match['during']:
            timing = "durante"
        elif best_match['days_diff'] == 0:
            timing = "exatamente no dia do"
        elif best_match['days_diff'] > 0:
            days = abs(best_match['days_diff'])
            timing = f"{days} {'dia' if days == 1 else 'dias'} após"
        else:
            days = abs(best_match['days_diff'])
            timing = f"{days} {'dia' if days == 1 else 'dias'} antes do"
        
        return {
            'has_coincidence': True,
            'event': best_match['event'],
            'timing': timing,
            'type': best_match['type'],
            'is_historical': best_match.get('historical', False)
        }
    
    return {
        'has_coincidence': False
    } 