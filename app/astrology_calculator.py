import math
from datetime import datetime
import pytz

class AstrologyCalculator:
    def __init__(self):
        # Signos do zodíaco com datas aproximadas
        self.zodiac_signs = [
            {'name': 'Áries', 'symbol': '♈', 'start': (3, 21), 'end': (4, 19), 'element': 'Fogo', 'quality': 'Cardeal'},
            {'name': 'Touro', 'symbol': '♉', 'start': (4, 20), 'end': (5, 20), 'element': 'Terra', 'quality': 'Fixo'},
            {'name': 'Gêmeos', 'symbol': '♊', 'start': (5, 21), 'end': (6, 20), 'element': 'Ar', 'quality': 'Mutável'},
            {'name': 'Câncer', 'symbol': '♋', 'start': (6, 21), 'end': (7, 22), 'element': 'Água', 'quality': 'Cardeal'},
            {'name': 'Leão', 'symbol': '♌', 'start': (7, 23), 'end': (8, 22), 'element': 'Fogo', 'quality': 'Fixo'},
            {'name': 'Virgem', 'symbol': '♍', 'start': (8, 23), 'end': (9, 22), 'element': 'Terra', 'quality': 'Mutável'},
            {'name': 'Libra', 'symbol': '♎', 'start': (9, 23), 'end': (10, 22), 'element': 'Ar', 'quality': 'Cardeal'},
            {'name': 'Escorpião', 'symbol': '♏', 'start': (10, 23), 'end': (11, 21), 'element': 'Água', 'quality': 'Fixo'},
            {'name': 'Sagitário', 'symbol': '♐', 'start': (11, 22), 'end': (12, 21), 'element': 'Fogo', 'quality': 'Mutável'},
            {'name': 'Capricórnio', 'symbol': '♑', 'start': (12, 22), 'end': (1, 19), 'element': 'Terra', 'quality': 'Cardeal'},
            {'name': 'Aquário', 'symbol': '♒', 'start': (1, 20), 'end': (2, 18), 'element': 'Ar', 'quality': 'Fixo'},
            {'name': 'Peixes', 'symbol': '♓', 'start': (2, 19), 'end': (3, 20), 'element': 'Água', 'quality': 'Mutável'}
        ]
        
        # Características dos signos
        self.sign_traits = {
            'Áries': {
                'personality': 'Pioneiro, corajoso, energético e impulsivo',
                'strengths': 'Liderança natural, determinação, coragem',
                'challenges': 'Impaciência, impulsividade, teimosia',
                'cosmic_message': 'Sua energia ardente ilumina novos caminhos no cosmos'
            },
            'Touro': {
                'personality': 'Estável, prático, sensual e determinado',
                'strengths': 'Persistência, lealdade, senso prático',
                'challenges': 'Teimosia, resistência a mudanças, materialismo',
                'cosmic_message': 'Sua força terrena ecoa através das eras cósmicas'
            },
            'Gêmeos': {
                'personality': 'Comunicativo, versátil, curioso e adaptável',
                'strengths': 'Inteligência, comunicação, adaptabilidade',
                'challenges': 'Inconstância, superficialidade, nervosismo',
                'cosmic_message': 'Sua mente dual navega entre as estrelas do conhecimento'
            },
            'Câncer': {
                'personality': 'Emotivo, intuitivo, protetor e nostálgico',
                'strengths': 'Intuição, empatia, cuidado com outros',
                'challenges': 'Sensibilidade excessiva, mudanças de humor, apego',
                'cosmic_message': 'Sua sensibilidade lunar conecta você aos ciclos cósmicos'
            },
            'Leão': {
                'personality': 'Criativo, generoso, orgulhoso e dramático',
                'strengths': 'Criatividade, generosidade, liderança carismática',
                'challenges': 'Orgulho, necessidade de atenção, arrogância',
                'cosmic_message': 'Seu brilho solar irradia majestade através do universo'
            },
            'Virgem': {
                'personality': 'Analítico, perfeccionista, prático e modesto',
                'strengths': 'Atenção aos detalhes, organização, senso de serviço',
                'challenges': 'Perfeccionismo, crítica excessiva, preocupação',
                'cosmic_message': 'Sua precisão terrena ordena o caos cósmico'
            },
            'Libra': {
                'personality': 'Diplomático, harmonioso, indeciso e charmoso',
                'strengths': 'Diplomacia, senso de justiça, charme natural',
                'challenges': 'Indecisão, dependência, superficialidade',
                'cosmic_message': 'Seu equilíbrio harmoniza as forças opostas do cosmos'
            },
            'Escorpião': {
                'personality': 'Intenso, misterioso, transformador e magnético',
                'strengths': 'Intensidade, intuição, capacidade de transformação',
                'challenges': 'Ciúme, vingança, obsessão',
                'cosmic_message': 'Sua profundidade aquática mergulha nos mistérios estelares'
            },
            'Sagitário': {
                'personality': 'Aventureiro, filosófico, otimista e livre',
                'strengths': 'Otimismo, filosofia, amor pela liberdade',
                'challenges': 'Imprudência, exagero, falta de tato',
                'cosmic_message': 'Sua flecha ígnea aponta para horizontes cósmicos infinitos'
            },
            'Capricórnio': {
                'personality': 'Ambicioso, disciplinado, responsável e tradicional',
                'strengths': 'Disciplina, responsabilidade, ambição saudável',
                'challenges': 'Rigidez, pessimismo, materialismo',
                'cosmic_message': 'Sua determinação terrena escala as montanhas do tempo'
            },
            'Aquário': {
                'personality': 'Inovador, independente, humanitário e excêntrico',
                'strengths': 'Originalidade, humanitarismo, visão futurista',
                'challenges': 'Frieza emocional, rebeldia, distanciamento',
                'cosmic_message': 'Sua visão aérea antecipa as revoluções cósmicas'
            },
            'Peixes': {
                'personality': 'Intuitivo, compassivo, sonhador e sensível',
                'strengths': 'Compaixão, intuição, criatividade',
                'challenges': 'Escapismo, confusão, vitimização',
                'cosmic_message': 'Sua alma aquática flui com as marés cósmicas eternas'
            }
        }
    
    def calculate_sun_sign(self, birth_date):
        """Calcula o signo solar baseado na data de nascimento"""
        month = birth_date.month
        day = birth_date.day
        
        for sign in self.zodiac_signs:
            start_month, start_day = sign['start']
            end_month, end_day = sign['end']
            
            # Verificar se a data está dentro do período do signo
            if start_month == end_month:
                # Signo dentro do mesmo mês
                if month == start_month and start_day <= day <= end_day:
                    return sign
            else:
                # Signo que cruza meses (ex: Capricórnio)
                if (month == start_month and day >= start_day) or \
                   (month == end_month and day <= end_day):
                    return sign
        
        return self.zodiac_signs[0]  # Fallback para Áries
    
    def calculate_ascendant(self, birth_datetime, latitude, longitude):
        """Calcula o ascendente baseado na hora e local de nascimento (simplificado)"""
        # Cálculo simplificado do ascendente
        # Em uma implementação real, seria necessário usar efemérides precisas
        
        hour = birth_datetime.hour + birth_datetime.minute / 60.0
        
        # Ajustar pela longitude (aproximação)
        local_sidereal_time = (hour + longitude / 15.0) % 24
        
        # Calcular ascendente baseado no tempo sideral local (simplificado)
        ascendant_degree = (local_sidereal_time * 15) % 360
        ascendant_sign_index = int(ascendant_degree / 30)
        
        return self.zodiac_signs[ascendant_sign_index]
    
    def calculate_lunar_phase(self, birth_date):
        """Calcula a fase lunar aproximada na data de nascimento"""
        # Cálculo simplificado da fase lunar
        # Baseado no ciclo lunar de aproximadamente 29.5 dias
        
        # Data de referência para lua nova (aproximada)
        reference_date = datetime(2000, 1, 6)  # Luna nova conhecida
        days_since_reference = (birth_date - reference_date).days
        
        # Calcular posição no ciclo lunar
        lunar_cycle = 29.53058867  # Período sinódico da lua em dias
        phase_position = (days_since_reference % lunar_cycle) / lunar_cycle
        
        if phase_position < 0.125:
            return {'name': 'Lua Nova', 'symbol': '🌑', 'meaning': 'Novos começos e potencial oculto'}
        elif phase_position < 0.375:
            return {'name': 'Lua Crescente', 'symbol': '🌒', 'meaning': 'Crescimento e manifestação'}
        elif phase_position < 0.625:
            return {'name': 'Lua Cheia', 'symbol': '🌕', 'meaning': 'Plenitude e iluminação'}
        else:
            return {'name': 'Lua Minguante', 'symbol': '🌘', 'meaning': 'Liberação e transformação'}
    
    def generate_cosmic_profile(self, birth_datetime, latitude, longitude):
        """Gera perfil astrológico completo"""
        sun_sign = self.calculate_sun_sign(birth_datetime)
        ascendant = self.calculate_ascendant(birth_datetime, latitude, longitude)
        lunar_phase = self.calculate_lunar_phase(birth_datetime)
        
        # Calcular elemento dominante
        elements = [sun_sign['element'], ascendant['element']]
        element_count = {}
        for element in elements:
            element_count[element] = element_count.get(element, 0) + 1
        
        dominant_element = max(element_count, key=element_count.get)
        
        # Gerar mensagem cósmica personalizada
        cosmic_message = self.generate_personalized_cosmic_message(sun_sign, ascendant, lunar_phase)
        
        return {
            'sun_sign': sun_sign,
            'ascendant': ascendant,
            'lunar_phase': lunar_phase,
            'dominant_element': dominant_element,
            'cosmic_message': cosmic_message,
            'personality_traits': self.sign_traits.get(sun_sign['name'], {}),
            'birth_chart_summary': self.generate_birth_chart_summary(sun_sign, ascendant, dominant_element)
        }
    
    def generate_personalized_cosmic_message(self, sun_sign, ascendant, lunar_phase):
        """Gera mensagem cósmica personalizada"""
        base_message = self.sign_traits[sun_sign['name']]['cosmic_message']
        
        ascendant_influence = f"Com ascendente em {ascendant['name']}, você projeta {ascendant['element'].lower()} ao mundo."
        lunar_influence = f"Nascido sob a {lunar_phase['name']}, sua alma carrega a energia de {lunar_phase['meaning'].lower()}."
        
        return f"{base_message} {ascendant_influence} {lunar_influence}"
    
    def generate_birth_chart_summary(self, sun_sign, ascendant, dominant_element):
        """Gera resumo do mapa astral"""
        element_meanings = {
            'Fogo': 'paixão, energia e iniciativa',
            'Terra': 'praticidade, estabilidade e materialização',
            'Ar': 'comunicação, intelecto e conexões',
            'Água': 'emoção, intuição e profundidade'
        }
        
        return {
            'core_identity': f"Sol em {sun_sign['name']} - Sua essência é {sun_sign['element'].lower()}",
            'outer_expression': f"Ascendente em {ascendant['name']} - Você se apresenta com energia {ascendant['element'].lower()}",
            'elemental_focus': f"Elemento dominante: {dominant_element} - Sua jornada enfatiza {element_meanings[dominant_element]}"
        } 