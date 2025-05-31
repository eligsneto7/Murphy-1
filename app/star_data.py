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
    },
    'Achernar': {
        'hip': 7588,
        'constellation': 'Eridanus',
        'magnitude': 0.46,
        'distance_ly': 139,
        'spectral_class': 'B6Vep',
        'ra_degrees': 24.429,
        'dec_degrees': -57.237,
        'age_billion_years': 0.037,
        'mass_solar': 6.7,
        'temperature_k': 15000,
        'history': """Achernar marca o fim do rio celestial Eridanus. É a estrela mais achatada conhecida, 
        girando tão rápido que seu diâmetro equatorial é 56% maior que o polar. Visível apenas do hemisfério sul, 
        era desconhecida dos antigos gregos e romanos. Seu nome vem do árabe 'ākhir an-nahr', 'fim do rio'.""",
        'constellation_stars': [
            {'name': 'Achernar', 'ra': 24.429, 'dec': -57.237, 'mag': 0.46},
            {'name': 'Cursa', 'ra': 76.962, 'dec': -5.086, 'mag': 2.79},
            {'name': 'Zaurak', 'ra': 59.507, 'dec': -13.509, 'mag': 2.95}
        ]
    },
    'Hadar': {
        'hip': 68702,
        'constellation': 'Centaurus',
        'magnitude': 0.61,
        'distance_ly': 390,
        'spectral_class': 'B1III',
        'ra_degrees': 210.956,
        'dec_degrees': -60.373,
        'age_billion_years': 0.014,
        'mass_solar': 10.5,
        'temperature_k': 25000,
        'history': """Hadar, também conhecida como Agena, é a segunda estrela mais brilhante de Centaurus. 
        É um sistema triplo de estrelas azuis massivas. Junto com Alpha Centauri, aponta para o Cruzeiro do Sul. 
        Seu nome árabe significa 'solo' ou 'chão', referindo-se à sua baixa altitude no céu árabe.""",
        'constellation_stars': [
            {'name': 'Hadar', 'ra': 210.956, 'dec': -60.373, 'mag': 0.61},
            {'name': 'Rigil Kentaurus', 'ra': 219.902, 'dec': -60.834, 'mag': -0.27},
            {'name': 'Menkent', 'ra': 211.671, 'dec': -36.370, 'mag': 2.06}
        ]
    },
    'Acrux': {
        'hip': 60718,
        'constellation': 'Crux',
        'magnitude': 0.77,
        'distance_ly': 320,
        'spectral_class': 'B0.5IV',
        'ra_degrees': 186.650,
        'dec_degrees': -63.099,
        'age_billion_years': 0.016,
        'mass_solar': 17.8,
        'temperature_k': 28000,
        'history': """Acrux é a estrela mais brilhante do Cruzeiro do Sul e a 13ª mais brilhante do céu. 
        É um sistema múltiplo de estrelas azuis quentes. Fundamental para navegação no hemisfério sul, 
        aparece em várias bandeiras nacionais. Não tem nome tradicional próprio - Acrux é uma contração de 'Alpha Crucis'.""",
        'constellation_stars': [
            {'name': 'Acrux', 'ra': 186.650, 'dec': -63.099, 'mag': 0.77},
            {'name': 'Gacrux', 'ra': 187.791, 'dec': -57.113, 'mag': 1.64},
            {'name': 'Becrux', 'ra': 191.930, 'dec': -59.689, 'mag': 1.25},
            {'name': 'Delta Crucis', 'ra': 183.786, 'dec': -58.749, 'mag': 2.80}
        ]
    },
    'Alnilam': {
        'hip': 26311,
        'constellation': 'Orion',
        'magnitude': 1.70,
        'distance_ly': 2000,
        'spectral_class': 'B0Ia',
        'ra_degrees': 84.053,
        'dec_degrees': -1.202,
        'age_billion_years': 0.005,
        'mass_solar': 30,
        'temperature_k': 25000,
        'history': """Alnilam é a estrela central do Cinturão de Órion. Uma supergigante azul 375.000 vezes 
        mais luminosa que o Sol. Está perdendo massa através de ventos estelares poderosos. Seu nome vem do 
        árabe 'an-niẓām', significando 'corda de pérolas'. Eventualmente explodirá como supernova.""",
        'constellation_stars': [
            {'name': 'Alnilam', 'ra': 84.053, 'dec': -1.202, 'mag': 1.70},
            {'name': 'Alnitak', 'ra': 85.190, 'dec': -1.943, 'mag': 1.77},
            {'name': 'Mintaka', 'ra': 83.002, 'dec': -0.299, 'mag': 2.23}
        ]
    },
    'Alioth': {
        'hip': 62956,
        'constellation': 'Ursa Major',
        'magnitude': 1.77,
        'distance_ly': 82.6,
        'spectral_class': 'A1III-IVp',
        'ra_degrees': 193.507,
        'dec_degrees': 55.960,
        'age_billion_years': 0.30,
        'mass_solar': 2.91,
        'temperature_k': 9020,
        'history': """Alioth é a estrela mais brilhante da Ursa Maior, apesar de ser Epsilon. É uma estrela 
        peculiar com campo magnético variável. Faz parte do asterismo do Arado/Grande Carro. Na China antiga, 
        era parte da constelação 'Beidou', o Arado do Norte, usado para navegação.""",
        'constellation_stars': [
            {'name': 'Alioth', 'ra': 193.507, 'dec': 55.960, 'mag': 1.77},
            {'name': 'Dubhe', 'ra': 165.932, 'dec': 61.751, 'mag': 1.79},
            {'name': 'Alkaid', 'ra': 206.885, 'dec': 49.313, 'mag': 1.86},
            {'name': 'Mizar', 'ra': 200.981, 'dec': 54.926, 'mag': 2.27}
        ]
    },
    'Algieba': {
        'hip': 50583,
        'constellation': 'Leo',
        'magnitude': 2.28,
        'distance_ly': 130,
        'spectral_class': 'K0III',
        'ra_degrees': 154.993,
        'dec_degrees': 19.842,
        'age_billion_years': 1.0,
        'mass_solar': 2.0,
        'temperature_k': 4470,
        'history': """Algieba, 'a juba' em árabe, é um belo sistema binário de gigantes douradas visível 
        com pequenos telescópios. As duas estrelas orbitam-se mutuamente a cada 510 anos. É um dos sistemas 
        binários mais bonitos para observadores amadores, com contraste de cores douradas.""",
        'constellation_stars': [
            {'name': 'Algieba', 'ra': 154.993, 'dec': 19.842, 'mag': 2.28},
            {'name': 'Regulus', 'ra': 152.093, 'dec': 11.967, 'mag': 1.35},
            {'name': 'Denebola', 'ra': 177.265, 'dec': 14.572, 'mag': 2.14}
        ]
    },
    'Castor': {
        'hip': 36850,
        'constellation': 'Gemini',
        'magnitude': 1.57,
        'distance_ly': 51,
        'spectral_class': 'A1V',
        'ra_degrees': 113.650,
        'dec_degrees': 31.888,
        'age_billion_years': 0.370,
        'mass_solar': 2.76,
        'temperature_k': 9230,
        'history': """Castor é um complexo sistema sêxtuplo - seis estrelas ligadas gravitacionalmente. 
        Na mitologia, representa um dos gêmeos com Pollux. Foi uma das primeiras estrelas descobertas como 
        binária (1678). As seis estrelas formam três pares binários que orbitam um centro comum.""",
        'constellation_stars': [
            {'name': 'Castor', 'ra': 113.650, 'dec': 31.888, 'mag': 1.57},
            {'name': 'Pollux', 'ra': 116.329, 'dec': 28.026, 'mag': 1.14},
            {'name': 'Alhena', 'ra': 99.428, 'dec': 16.399, 'mag': 1.90}
        ]
    },
    'Bellatrix': {
        'hip': 25336,
        'constellation': 'Orion',
        'magnitude': 1.64,
        'distance_ly': 250,
        'spectral_class': 'B2III',
        'ra_degrees': 81.283,
        'dec_degrees': 6.350,
        'age_billion_years': 0.025,
        'mass_solar': 8.6,
        'temperature_k': 21500,
        'history': """Bellatrix, 'a guerreira' em latim, marca o ombro esquerdo de Órion. Também conhecida 
        como 'Estrela Amazona'. Evoluirá para uma gigante laranja em alguns milhões de anos. Na astrologia 
        medieval, era associada com sucesso militar e honras civis.""",
        'constellation_stars': [
            {'name': 'Bellatrix', 'ra': 81.283, 'dec': 6.350, 'mag': 1.64},
            {'name': 'Betelgeuse', 'ra': 88.793, 'dec': 7.407, 'mag': 0.50},
            {'name': 'Rigel', 'ra': 78.634, 'dec': -8.202, 'mag': 0.13}
        ]
    },
    'Elnath': {
        'hip': 25428,
        'constellation': 'Taurus',
        'magnitude': 1.68,
        'distance_ly': 134,
        'spectral_class': 'B7III',
        'ra_degrees': 81.573,
        'dec_degrees': 28.608,
        'age_billion_years': 0.100,
        'mass_solar': 5.0,
        'temperature_k': 13600,
        'history': """Elnath marca o chifre norte do Touro. É compartilhada entre Taurus e Auriga, sendo 
        Beta Tauri e Gamma Aurigae. Seu nome vem do árabe 'an-naţħ', significando 'o que chifra'. 
        É uma estrela de mercúrio-manganês com composição química peculiar.""",
        'constellation_stars': [
            {'name': 'Elnath', 'ra': 81.573, 'dec': 28.608, 'mag': 1.68},
            {'name': 'Aldebaran', 'ra': 68.980, 'dec': 16.509, 'mag': 0.85},
            {'name': 'Alcyone', 'ra': 56.871, 'dec': 24.105, 'mag': 2.87}
        ]
    },
    'Miaplacidus': {
        'hip': 45238,
        'constellation': 'Carina',
        'magnitude': 1.68,
        'distance_ly': 111,
        'spectral_class': 'A1III',
        'ra_degrees': 138.300,
        'dec_degrees': -69.717,
        'age_billion_years': 0.260,
        'mass_solar': 3.5,
        'temperature_k': 8600,
        'history': """Miaplacidus é a segunda estrela mais brilhante de Carina. Seu nome significa 'águas 
        calmas', possivelmente corrompido do árabe 'miyāh', águas. Importante para navegação no hemisfério 
        sul. Está evoluindo para fora da sequência principal, tornando-se uma gigante.""",
        'constellation_stars': [
            {'name': 'Miaplacidus', 'ra': 138.300, 'dec': -69.717, 'mag': 1.68},
            {'name': 'Canopus', 'ra': 95.988, 'dec': -52.696, 'mag': -0.74},
            {'name': 'Avior', 'ra': 125.628, 'dec': -59.509, 'mag': 1.86}
        ]
    },
    'Alnair': {
        'hip': 109268,
        'constellation': 'Grus',
        'magnitude': 1.74,
        'distance_ly': 101,
        'spectral_class': 'B6V',
        'ra_degrees': 332.058,
        'dec_degrees': -46.961,
        'age_billion_years': 0.100,
        'mass_solar': 4.0,
        'temperature_k': 13500,
        'history': """Alnair, 'a brilhante' em árabe, é a estrela alpha da constelação do Grou. 
        Relativamente próxima e quente, é usada como padrão para calibração de instrumentos astronômicos. 
        O Grou é uma constelação moderna do hemisfério sul, criada no século XVI.""",
        'constellation_stars': [
            {'name': 'Alnair', 'ra': 332.058, 'dec': -46.961, 'mag': 1.74},
            {'name': 'Beta Gruis', 'ra': 340.667, 'dec': -46.885, 'mag': 2.15},
            {'name': 'Gamma Gruis', 'ra': 328.482, 'dec': -37.365, 'mag': 3.01}
        ]
    },
    'Mirfak': {
        'hip': 15863,
        'constellation': 'Perseus',
        'magnitude': 1.80,
        'distance_ly': 590,
        'spectral_class': 'F5Ib',
        'ra_degrees': 51.081,
        'dec_degrees': 49.861,
        'age_billion_years': 0.041,
        'mass_solar': 8.5,
        'temperature_k': 6350,
        'history': """Mirfak, 'cotovelo' em árabe, é a estrela mais brilhante de Perseus. É uma supergigante 
        amarela rodeada por um aglomerado estelar. Na mitologia, marca o cotovelo do herói Perseus segurando 
        a cabeça da Medusa. É 5000 vezes mais luminosa que o Sol.""",
        'constellation_stars': [
            {'name': 'Mirfak', 'ra': 51.081, 'dec': 49.861, 'mag': 1.80},
            {'name': 'Algol', 'ra': 47.042, 'dec': 40.956, 'mag': 2.12},
            {'name': 'Gamma Per', 'ra': 45.190, 'dec': 53.506, 'mag': 2.93}
        ]
    },
    'Dubhe': {
        'hip': 54061,
        'constellation': 'Ursa Major',
        'magnitude': 1.79,
        'distance_ly': 123,
        'spectral_class': 'G9III',
        'ra_degrees': 165.932,
        'dec_degrees': 61.751,
        'age_billion_years': 1.1,
        'mass_solar': 4.25,
        'temperature_k': 4660,
        'history': """Dubhe, do árabe 'dubb', urso, marca as costas da Ursa Maior. Com Merak, forma os 
        'Ponteiros' que apontam para Polaris. É um sistema binário com uma anã laranja companheira. 
        Fundamental para navegação no hemisfério norte através dos séculos.""",
        'constellation_stars': [
            {'name': 'Dubhe', 'ra': 165.932, 'dec': 61.751, 'mag': 1.79},
            {'name': 'Merak', 'ra': 165.460, 'dec': 56.383, 'mag': 2.37},
            {'name': 'Alioth', 'ra': 193.507, 'dec': 55.960, 'mag': 1.77}
        ]
    },
    'Wezen': {
        'hip': 34444,
        'constellation': 'Canis Major',
        'magnitude': 1.84,
        'distance_ly': 1800,
        'spectral_class': 'F8Ia',
        'ra_degrees': 107.098,
        'dec_degrees': -26.393,
        'age_billion_years': 0.017,
        'mass_solar': 17,
        'temperature_k': 5900,
        'history': """Wezen, 'o peso' em árabe, é uma das estrelas mais luminosas conhecidas - 82.000 vezes 
        o Sol. Uma supergigante amarela nos estágios finais de evolução. Apesar da enorme distância, é 
        facilmente visível. Pode já ter iniciado a fusão de hélio em seu núcleo.""",
        'constellation_stars': [
            {'name': 'Wezen', 'ra': 107.098, 'dec': -26.393, 'mag': 1.84},
            {'name': 'Sirius', 'ra': 101.287, 'dec': -16.716, 'mag': -1.46},
            {'name': 'Adhara', 'ra': 104.656, 'dec': -28.972, 'mag': 1.50}
        ]
    },
    'Alkaid': {
        'hip': 67301,
        'constellation': 'Ursa Major',
        'magnitude': 1.86,
        'distance_ly': 104,
        'spectral_class': 'B3V',
        'ra_degrees': 206.885,
        'dec_degrees': 49.313,
        'age_billion_years': 0.010,
        'mass_solar': 6.1,
        'temperature_k': 15540,
        'history': """Alkaid marca o fim da cauda da Ursa Maior. Ao contrário das outras estrelas do Arado, 
        não pertence ao grupo móvel da Ursa Maior. Seu nome vem do árabe 'qā'id bināt na'sh', 'líder das 
        filhas do caixão'. É uma das estrelas mais quentes do Arado.""",
        'constellation_stars': [
            {'name': 'Alkaid', 'ra': 206.885, 'dec': 49.313, 'mag': 1.86},
            {'name': 'Mizar', 'ra': 200.981, 'dec': 54.926, 'mag': 2.27},
            {'name': 'Alioth', 'ra': 193.507, 'dec': 55.960, 'mag': 1.77}
        ]
    },
    'Avior': {
        'hip': 41037,
        'constellation': 'Carina',
        'magnitude': 1.86,
        'distance_ly': 630,
        'spectral_class': 'K3III',
        'ra_degrees': 125.628,
        'dec_degrees': -59.509,
        'age_billion_years': 0.040,
        'mass_solar': 9.0,
        'temperature_k': 3900,
        'history': """Avior é uma das estrelas de navegação do hemisfério sul. Seu nome foi criado pela 
        RAF na década de 1930 para navegação aérea. É um sistema binário de uma gigante laranja e uma 
        estrela azul quente. A combinação produz uma cor amarelada característica.""",
        'constellation_stars': [
            {'name': 'Avior', 'ra': 125.628, 'dec': -59.509, 'mag': 1.86},
            {'name': 'Canopus', 'ra': 95.988, 'dec': -52.696, 'mag': -0.74},
            {'name': 'Miaplacidus', 'ra': 138.300, 'dec': -69.717, 'mag': 1.68}
        ]
    },
    'Sargas': {
        'hip': 86228,
        'constellation': 'Scorpius',
        'magnitude': 1.87,
        'distance_ly': 270,
        'spectral_class': 'F1II',
        'ra_degrees': 264.330,
        'dec_degrees': -42.998,
        'age_billion_years': 0.031,
        'mass_solar': 5.7,
        'temperature_k': 7200,
        'history': """Sargas é uma das estrelas que formam o 'ferrão' do Escorpião. Seu nome vem do sumério 
        e babilônico. É uma estrela evoluída saindo da sequência principal. Junto com Shaula, marca o ferrão 
        do Escorpião, uma das formas mais reconhecíveis do zodíaco.""",
        'constellation_stars': [
            {'name': 'Sargas', 'ra': 264.330, 'dec': -42.998, 'mag': 1.87},
            {'name': 'Shaula', 'ra': 263.402, 'dec': -37.104, 'mag': 1.63},
            {'name': 'Antares', 'ra': 247.352, 'dec': -26.432, 'mag': 1.09}
        ]
    },
    'Kaus Australis': {
        'hip': 90185,
        'constellation': 'Sagittarius',
        'magnitude': 1.85,
        'distance_ly': 140,
        'spectral_class': 'B9.5III',
        'ra_degrees': 276.043,
        'dec_degrees': -34.385,
        'age_billion_years': 0.232,
        'mass_solar': 3.5,
        'temperature_k': 9960,
        'history': """Kaus Australis marca a ponta sul do arco do Arqueiro. O nome combina o árabe 'qaws' 
        (arco) com o latim 'australis' (sul). É a estrela mais brilhante de Sagitário. Faz parte do asterismo 
        do 'Bule de Chá', popular entre observadores do céu.""",
        'constellation_stars': [
            {'name': 'Kaus Australis', 'ra': 276.043, 'dec': -34.385, 'mag': 1.85},
            {'name': 'Kaus Media', 'ra': 275.248, 'dec': -29.828, 'mag': 2.70},
            {'name': 'Kaus Borealis', 'ra': 271.452, 'dec': -25.422, 'mag': 2.81}
        ]
    },
    'Alhena': {
        'hip': 31681,
        'constellation': 'Gemini',
        'magnitude': 1.90,
        'distance_ly': 109,
        'spectral_class': 'A1.5IV',
        'ra_degrees': 99.428,
        'dec_degrees': 16.399,
        'age_billion_years': 0.300,
        'mass_solar': 2.8,
        'temperature_k': 9260,
        'history': """Alhena marca o pé de Pollux em Gêmeos. Seu nome vem do árabe 'al-han'ah', significando 
        'a marca' (no pescoço do camelo, na astronomia árabe). É uma estrela subgigante começando a evoluir 
        para gigante. Tem um espectro peculiar sugerindo uma companheira próxima.""",
        'constellation_stars': [
            {'name': 'Alhena', 'ra': 99.428, 'dec': 16.399, 'mag': 1.90},
            {'name': 'Pollux', 'ra': 116.329, 'dec': 28.026, 'mag': 1.14},
            {'name': 'Castor', 'ra': 113.650, 'dec': 31.888, 'mag': 1.57}
        ]
    },
    'Peacock': {
        'hip': 100751,
        'constellation': 'Pavo',
        'magnitude': 1.91,
        'distance_ly': 179,
        'spectral_class': 'B2IV',
        'ra_degrees': 306.412,
        'dec_degrees': -56.735,
        'age_billion_years': 0.048,
        'mass_solar': 5.9,
        'temperature_k': 17700,
        'history': """Peacock é a estrela alpha do Pavão, constelação do hemisfério sul. Seu nome em inglês 
        foi atribuído pela RAF para navegação. É uma estrela azul-branca evoluindo para gigante. O Pavão 
        é uma das constelações de aves do sul criadas no século XVI.""",
        'constellation_stars': [
            {'name': 'Peacock', 'ra': 306.412, 'dec': -56.735, 'mag': 1.91},
            {'name': 'Beta Pavonis', 'ra': 322.156, 'dec': -66.203, 'mag': 3.42},
            {'name': 'Delta Pavonis', 'ra': 306.174, 'dec': -66.182, 'mag': 3.56}
        ]
    },
    'Mirzam': {
        'hip': 30324,
        'constellation': 'Canis Major',
        'magnitude': 1.98,
        'distance_ly': 500,
        'spectral_class': 'B1II-III',
        'ra_degrees': 95.675,
        'dec_degrees': -17.956,
        'age_billion_years': 0.012,
        'mass_solar': 13.5,
        'temperature_k': 23150,
        'history': """Mirzam, 'o arauto' em árabe, nasce antes de Sirius, anunciando sua chegada. É uma 
        estrela variável Beta Cephei, pulsando a cada 6 horas. Uma gigante azul muito quente e luminosa, 
        é 26.000 vezes mais brilhante que o Sol. Importante na astronomia árabe antiga.""",
        'constellation_stars': [
            {'name': 'Mirzam', 'ra': 95.675, 'dec': -17.956, 'mag': 1.98},
            {'name': 'Sirius', 'ra': 101.287, 'dec': -16.716, 'mag': -1.46},
            {'name': 'Wezen', 'ra': 107.098, 'dec': -26.393, 'mag': 1.84}
        ]
    },
    'Alphard': {
        'hip': 46390,
        'constellation': 'Hydra',
        'magnitude': 2.00,
        'distance_ly': 177,
        'spectral_class': 'K3II',
        'ra_degrees': 141.897,
        'dec_degrees': -8.659,
        'age_billion_years': 0.420,
        'mass_solar': 3.0,
        'temperature_k': 4120,
        'history': """Alphard, 'a solitária' em árabe, é a única estrela brilhante em Hydra, a maior 
        constelação do céu. Por isso também é chamada 'Cor Hydrae', coração da serpente. É uma gigante 
        laranja 780 vezes mais luminosa que o Sol. Tem bário anormalmente alto em sua atmosfera.""",
        'constellation_stars': [
            {'name': 'Alphard', 'ra': 141.897, 'dec': -8.659, 'mag': 2.00},
            {'name': 'Gamma Hya', 'ra': 199.730, 'dec': -23.171, 'mag': 3.00},
            {'name': 'Pi Hya', 'ra': 209.403, 'dec': -26.683, 'mag': 3.27}
        ]
    },
    'Hamal': {
        'hip': 9884,
        'constellation': 'Aries',
        'magnitude': 2.00,
        'distance_ly': 65.8,
        'spectral_class': 'K1III',
        'ra_degrees': 31.793,
        'dec_degrees': 23.463,
        'age_billion_years': 3.4,
        'mass_solar': 1.5,
        'temperature_k': 4480,
        'history': """Hamal, 'a cabeça do carneiro' em árabe, marcava o equinócio vernal há 2000 anos. 
        Por isso Áries é a primeira constelação do zodíaco. É uma gigante laranja com um planeta gigante 
        confirmado. Na antiguidade, era uma das estrelas mais importantes para calendários.""",
        'constellation_stars': [
            {'name': 'Hamal', 'ra': 31.793, 'dec': 23.463, 'mag': 2.00},
            {'name': 'Sheratan', 'ra': 28.660, 'dec': 20.808, 'mag': 2.64},
            {'name': 'Mesarthim', 'ra': 30.975, 'dec': 19.294, 'mag': 3.86}
        ]
    },
    'Diphda': {
        'hip': 3419,
        'constellation': 'Cetus',
        'magnitude': 2.04,
        'distance_ly': 96.3,
        'spectral_class': 'K0III',
        'ra_degrees': 10.897,
        'dec_degrees': -17.987,
        'age_billion_years': 1.0,
        'mass_solar': 2.8,
        'temperature_k': 4800,
        'history': """Diphda, 'a segunda rã' em árabe, é a estrela mais brilhante de Cetus, a Baleia. 
        Também chamada Deneb Kaitos, 'cauda da baleia'. É uma gigante laranja com atividade cromosférica 
        incomum. Importante para navegação, sendo uma das 57 estrelas de navegação selecionadas.""",
        'constellation_stars': [
            {'name': 'Diphda', 'ra': 10.897, 'dec': -17.987, 'mag': 2.04},
            {'name': 'Menkar', 'ra': 45.570, 'dec': 4.090, 'mag': 2.53},
            {'name': 'Gamma Ceti', 'ra': 40.825, 'dec': 3.236, 'mag': 3.47}
        ]
    },
    'Nunki': {
        'hip': 92855,
        'constellation': 'Sagittarius',
        'magnitude': 2.05,
        'distance_ly': 228,
        'spectral_class': 'B2.5V',
        'ra_degrees': 283.816,
        'dec_degrees': -26.297,
        'age_billion_years': 0.031,
        'mass_solar': 7.8,
        'temperature_k': 20400,
        'history': """Nunki é uma das estrelas do asterismo do 'Bule de Chá' em Sagitário. Seu nome é 
        de origem babilônica, representando a cidade sagrada de Eridu. É a segunda estrela mais brilhante 
        da constelação. Marca o ombro do Arqueiro na figura mitológica.""",
        'constellation_stars': [
            {'name': 'Nunki', 'ra': 283.816, 'dec': -26.297, 'mag': 2.05},
            {'name': 'Kaus Australis', 'ra': 276.043, 'dec': -34.385, 'mag': 1.85},
            {'name': 'Ascella', 'ra': 285.653, 'dec': -29.880, 'mag': 2.60}
        ]
    },
    'Menkent': {
        'hip': 68933,
        'constellation': 'Centaurus',
        'magnitude': 2.06,
        'distance_ly': 61.0,
        'spectral_class': 'K0III',
        'ra_degrees': 211.671,
        'dec_degrees': -36.370,
        'age_billion_years': 0.8,
        'mass_solar': 1.27,
        'temperature_k': 4980,
        'history': """Menkent, 'ombro do Centauro' em árabe, é uma gigante laranja próxima. Apesar de ser 
        uma das estrelas mais brilhantes de Centaurus, não tem designação Bayer alpha ou beta. É similar 
        ao que nosso Sol será em bilhões de anos quando evoluir para gigante.""",
        'constellation_stars': [
            {'name': 'Menkent', 'ra': 211.671, 'dec': -36.370, 'mag': 2.06},
            {'name': 'Hadar', 'ra': 210.956, 'dec': -60.373, 'mag': 0.61},
            {'name': 'Alpha Centauri', 'ra': 219.902, 'dec': -60.834, 'mag': -0.27}
        ]
    },
    'Saiph': {
        'hip': 27366,
        'constellation': 'Orion',
        'magnitude': 2.09,
        'distance_ly': 650,
        'spectral_class': 'B0.5Ia',
        'ra_degrees': 86.939,
        'dec_degrees': -9.670,
        'age_billion_years': 0.011,
        'mass_solar': 15.5,
        'temperature_k': 26500,
        'history': """Saiph marca o pé esquerdo de Órion. Seu nome vem do árabe 'saif al jabbar', 'espada 
        do gigante'. Apesar de ter a mesma magnitude aparente de Bellatrix, é muito mais distante e luminosa. 
        É 57.000 vezes mais brilhante que o Sol e eventualmente explodirá como supernova.""",
        'constellation_stars': [
            {'name': 'Saiph', 'ra': 86.939, 'dec': -9.670, 'mag': 2.09},
            {'name': 'Rigel', 'ra': 78.634, 'dec': -8.202, 'mag': 0.13},
            {'name': 'Bellatrix', 'ra': 81.283, 'dec': 6.350, 'mag': 1.64}
        ]
    },
    'Alphecca': {
        'hip': 76267,
        'constellation': 'Corona Borealis',
        'magnitude': 2.23,
        'distance_ly': 74.7,
        'spectral_class': 'A0V',
        'ra_degrees': 233.672,
        'dec_degrees': 26.715,
        'age_billion_years': 0.314,
        'mass_solar': 2.58,
        'temperature_k': 9700,
        'history': """Alphecca, 'a brilhante do prato quebrado' em árabe, é a joia da Coroa Boreal. Também 
        chamada Gemma, 'jóia' em latim. É um sistema binário eclipsante. Na mitologia, a coroa foi dada 
        por Dionísio a Ariadne. É similar a Vega em muitos aspectos.""",
        'constellation_stars': [
            {'name': 'Alphecca', 'ra': 233.672, 'dec': 26.715, 'mag': 2.23},
            {'name': 'Nusakan', 'ra': 229.279, 'dec': 29.106, 'mag': 3.68},
            {'name': 'Gamma CrB', 'ra': 234.870, 'dec': 26.295, 'mag': 3.84}
        ]
    },
    'Almach': {
        'hip': 9640,
        'constellation': 'Andromeda',
        'magnitude': 2.10,
        'distance_ly': 350,
        'spectral_class': 'K3II',
        'ra_degrees': 30.975,
        'dec_degrees': 42.330,
        'age_billion_years': 0.080,
        'mass_solar': 5.0,
        'temperature_k': 4250,
        'history': """Almach é um dos mais belos sistemas múltiplos para telescópios pequenos, com contraste 
        de cores dourada e azul-esverdeada. O nome vem do árabe 'al-'anāq', referindo-se a um animal do 
        deserto. Marca o pé de Andrômeda na figura mitológica.""",
        'constellation_stars': [
            {'name': 'Almach', 'ra': 30.975, 'dec': 42.330, 'mag': 2.10},
            {'name': 'Mirach', 'ra': 17.433, 'dec': 35.621, 'mag': 2.06},
            {'name': 'Alpheratz', 'ra': 2.097, 'dec': 29.091, 'mag': 2.06}
        ]
    },
    'Caph': {
        'hip': 746,
        'constellation': 'Cassiopeia',
        'magnitude': 2.27,
        'distance_ly': 54.7,
        'spectral_class': 'F2III',
        'ra_degrees': 2.295,
        'dec_degrees': 59.150,
        'age_billion_years': 1.09,
        'mass_solar': 1.91,
        'temperature_k': 7079,
        'history': """Caph, 'a mão' em árabe, marca o canto superior direito do 'W' de Cassiopeia. É uma 
        estrela variável Delta Scuti com pequenas pulsações. Historicamente usada para navegação no 
        hemisfério norte. Gira rapidamente, completando uma rotação em apenas 1.12 dias.""",
        'constellation_stars': [
            {'name': 'Caph', 'ra': 2.295, 'dec': 59.150, 'mag': 2.27},
            {'name': 'Schedar', 'ra': 10.127, 'dec': 56.537, 'mag': 2.23},
            {'name': 'Gamma Cas', 'ra': 14.177, 'dec': 60.717, 'mag': 2.47}
        ]
    },
    'Izar': {
        'hip': 72105,
        'constellation': 'Boötes',
        'magnitude': 2.37,
        'distance_ly': 203,
        'spectral_class': 'K0II',
        'ra_degrees': 221.247,
        'dec_degrees': 27.074,
        'age_billion_years': 0.037,
        'mass_solar': 4.6,
        'temperature_k': 4550,
        'history': """Izar, 'o véu' em árabe, é uma das mais belas estrelas duplas do céu. Também chamada 
        Pulcherrima, 'a mais bela' em latim, por seu contraste laranja e azul-esverdeado. As duas estrelas 
        orbitam-se a cada mil anos. Foi uma das primeiras duplas descobertas por telescópio.""",
        'constellation_stars': [
            {'name': 'Izar', 'ra': 221.247, 'dec': 27.074, 'mag': 2.37},
            {'name': 'Arcturus', 'ra': 213.915, 'dec': 19.182, 'mag': -0.05},
            {'name': 'Muphrid', 'ra': 208.671, 'dec': 18.398, 'mag': 2.68}
        ]
    },
    'Schedar': {
        'hip': 3179,
        'constellation': 'Cassiopeia',
        'magnitude': 2.23,
        'distance_ly': 549,
        'spectral_class': 'K0II',
        'ra_degrees': 10.127,
        'dec_degrees': 56.537,
        'age_billion_years': 0.040,
        'mass_solar': 4.5,
        'temperature_k': 4530,
        'history': """Schedar, 'o peito' em árabe, é a estrela alpha de Cassiopeia apesar de às vezes ser 
        mais fraca que Caph. É uma gigante laranja massiva. Marca o centro do 'W' ou 'M' de Cassiopeia, 
        dependendo da orientação. Possivelmente uma variável irregular.""",
        'constellation_stars': [
            {'name': 'Schedar', 'ra': 10.127, 'dec': 56.537, 'mag': 2.23},
            {'name': 'Caph', 'ra': 2.295, 'dec': 59.150, 'mag': 2.27},
            {'name': 'Gamma Cas', 'ra': 14.177, 'dec': 60.717, 'mag': 2.47}
        ]
    },
    'Dschubba': {
        'hip': 78401,
        'constellation': 'Scorpius',
        'magnitude': 2.32,
        'distance_ly': 443,
        'spectral_class': 'B0V',
        'ra_degrees': 240.083,
        'dec_degrees': -22.622,
        'age_billion_years': 0.011,
        'mass_solar': 14.5,
        'temperature_k': 28000,
        'history': """Dschubba, 'a fronte' em árabe, marca a cabeça do Escorpião. É um sistema múltiplo 
        complexo de estrelas azuis quentes. A estrela principal é 38.000 vezes mais luminosa que o Sol. 
        Ocasionalmente aumenta de brilho devido a ejeções de material de sua superfície.""",
        'constellation_stars': [
            {'name': 'Dschubba', 'ra': 240.083, 'dec': -22.622, 'mag': 2.32},
            {'name': 'Antares', 'ra': 247.352, 'dec': -26.432, 'mag': 1.09},
            {'name': 'Graffias', 'ra': 241.359, 'dec': -19.805, 'mag': 2.62}
        ]
    },
    'Merak': {
        'hip': 53910,
        'constellation': 'Ursa Major',
        'magnitude': 2.37,
        'distance_ly': 79.7,
        'spectral_class': 'A1IVps',
        'ra_degrees': 165.460,
        'dec_degrees': 56.383,
        'age_billion_years': 0.500,
        'mass_solar': 2.7,
        'temperature_k': 9000,
        'history': """Merak, 'os lombos' do urso em árabe, forma com Dubhe os famosos 'Ponteiros' que 
        apontam para Polaris. É membro do Grupo Móvel da Ursa Maior, estrelas que nasceram juntas e 
        se movem juntas pelo espaço. É cercada por um disco de poeira, possivelmente formando planetas.""",
        'constellation_stars': [
            {'name': 'Merak', 'ra': 165.460, 'dec': 56.383, 'mag': 2.37},
            {'name': 'Dubhe', 'ra': 165.932, 'dec': 61.751, 'mag': 1.79},
            {'name': 'Phecda', 'ra': 178.458, 'dec': 53.695, 'mag': 2.44}
        ]
    },
    'Etamin': {
        'hip': 87833,
        'constellation': 'Draco',
        'magnitude': 2.23,
        'distance_ly': 154,
        'spectral_class': 'K5III',
        'ra_degrees': 269.152,
        'dec_degrees': 51.489,
        'age_billion_years': 1.55,
        'mass_solar': 1.72,
        'temperature_k': 3930,
        'history': """Etamin, também Eltanin, 'a grande serpente' em árabe, é a estrela mais brilhante 
        de Draco. Foi observada por James Bradley em 1728 para descobrir a aberração da luz, provando 
        o movimento da Terra. Passará muito próxima do Sol (28 anos-luz) em 1.5 milhões de anos.""",
        'constellation_stars': [
            {'name': 'Etamin', 'ra': 269.152, 'dec': 51.489, 'mag': 2.23},
            {'name': 'Rastaban', 'ra': 262.608, 'dec': 52.301, 'mag': 2.79},
            {'name': 'Thuban', 'ra': 211.097, 'dec': 64.376, 'mag': 3.65}
        ]
    },
    'Enif': {
        'hip': 107315,
        'constellation': 'Pegasus',
        'magnitude': 2.39,
        'distance_ly': 690,
        'spectral_class': 'K2Ib',
        'ra_degrees': 326.047,
        'dec_degrees': 9.875,
        'age_billion_years': 0.020,
        'mass_solar': 12,
        'temperature_k': 4460,
        'history': """Enif, 'o nariz' em árabe, marca o focinho de Pégaso. É uma supergigante laranja 
        12 vezes mais massiva que o Sol. Tem erupções dramáticas, chegando a brilhar como estrela de 
        primeira magnitude. É 6.700 vezes mais luminosa que o Sol e tem um envelope estendido de gás.""",
        'constellation_stars': [
            {'name': 'Enif', 'ra': 326.047, 'dec': 9.875, 'mag': 2.39},
            {'name': 'Markab', 'ra': 346.190, 'dec': 15.205, 'mag': 2.48},
            {'name': 'Scheat', 'ra': 345.944, 'dec': 28.083, 'mag': 2.42}
        ]
    },
    'Nashira': {
        'hip': 106985,
        'constellation': 'Capricornus',
        'magnitude': 3.68,
        'distance_ly': 139,
        'spectral_class': 'G9III',
        'ra_degrees': 325.023,
        'dec_degrees': -16.662,
        'age_billion_years': 0.100,
        'mass_solar': 2.5,
        'temperature_k': 4900,
        'history': """Nashira, 'a portadora de boas novas' em árabe, é uma gigante amarela em Capricórnio. 
        Tem propriedades químicas peculiares com excesso de bário e estrôncio. É parte do asterismo que 
        forma o 'triângulo' ou 'barco' de Capricórnio. Historicamente importante na astrologia persa.""",
        'constellation_stars': [
            {'name': 'Nashira', 'ra': 325.023, 'dec': -16.662, 'mag': 3.68},
            {'name': 'Deneb Algedi', 'ra': 326.760, 'dec': -16.127, 'mag': 2.87},
            {'name': 'Dabih', 'ra': 305.253, 'dec': -14.781, 'mag': 3.08}
        ]
    },
    'Alpheratz': {
        'hip': 677,
        'constellation': 'Andromeda',
        'magnitude': 2.06,
        'distance_ly': 97,
        'spectral_class': 'B8IVpMnHg',
        'ra_degrees': 2.097,
        'dec_degrees': 29.091,
        'age_billion_years': 0.060,
        'mass_solar': 3.8,
        'temperature_k': 13800,
        'history': """Alpheratz, 'o umbigo do cavalo' em árabe, é compartilhada entre Andrômeda e Pégaso. 
        Marca o canto nordeste do Grande Quadrado de Pégaso. É uma estrela de mercúrio-manganês com 
        abundâncias químicas anômalas. Foi transferida de Pégaso para Andrômeda oficialmente em 1930.""",
        'constellation_stars': [
            {'name': 'Alpheratz', 'ra': 2.097, 'dec': 29.091, 'mag': 2.06},
            {'name': 'Mirach', 'ra': 17.433, 'dec': 35.621, 'mag': 2.06},
            {'name': 'Almach', 'ra': 30.975, 'dec': 42.330, 'mag': 2.10}
        ]
    },
    'Mirach': {
        'hip': 5447,
        'constellation': 'Andromeda',
        'magnitude': 2.06,
        'distance_ly': 199,
        'spectral_class': 'M0III',
        'ra_degrees': 17.433,
        'dec_degrees': 35.621,
        'age_billion_years': 0.600,
        'mass_solar': 2.5,
        'temperature_k': 3800,
        'history': """Mirach, 'o cinto' em árabe, é uma gigante vermelha fria. É usada como guia para 
        encontrar a Galáxia de Andrômeda, que fica próxima no céu. Tem uma pequena galáxia elíptica 
        companheira conhecida como 'Fantasma de Mirach'. É 1.900 vezes mais luminosa que o Sol.""",
        'constellation_stars': [
            {'name': 'Mirach', 'ra': 17.433, 'dec': 35.621, 'mag': 2.06},
            {'name': 'Alpheratz', 'ra': 2.097, 'dec': 29.091, 'mag': 2.06},
            {'name': 'Almach', 'ra': 30.975, 'dec': 42.330, 'mag': 2.10}
        ]
    },
    'Algol': {
        'hip': 14576,
        'constellation': 'Perseus',
        'magnitude': 2.12,
        'distance_ly': 90,
        'spectral_class': 'B8V',
        'ra_degrees': 47.042,
        'dec_degrees': 40.956,
        'age_billion_years': 0.300,
        'mass_solar': 3.17,
        'temperature_k': 13000,
        'history': """Algol, 'a estrela do demônio' em árabe, é o protótipo das variáveis eclipsantes. 
        A cada 2.87 dias, diminui de brilho quando sua companheira passa na frente. Conhecida como 
        maléfica desde a antiguidade. Representa o olho da Medusa na mitologia. 'Algol' deu origem 
        à palavra 'álcool'.""",
        'constellation_stars': [
            {'name': 'Algol', 'ra': 47.042, 'dec': 40.956, 'mag': 2.12},
            {'name': 'Mirfak', 'ra': 51.081, 'dec': 49.861, 'mag': 1.80},
            {'name': 'Gamma Per', 'ra': 45.190, 'dec': 53.506, 'mag': 2.93}
        ]
    },
    'Denebola': {
        'hip': 57632,
        'constellation': 'Leo',
        'magnitude': 2.14,
        'distance_ly': 36.2,
        'spectral_class': 'A3Va',
        'ra_degrees': 177.265,
        'dec_degrees': 14.572,
        'age_billion_years': 0.100,
        'mass_solar': 1.75,
        'temperature_k': 8500,
        'history': """Denebola, 'cauda do leão' em árabe, marca a cauda de Leo. É uma estrela variável 
        Delta Scuti com pequenas pulsações. Gira rapidamente, uma vez a cada 15 horas. Tem um excesso 
        de radiação infravermelha, sugerindo um disco de poeira circunstelar, possivelmente formando planetas.""",
        'constellation_stars': [
            {'name': 'Denebola', 'ra': 177.265, 'dec': 14.572, 'mag': 2.14},
            {'name': 'Regulus', 'ra': 152.093, 'dec': 11.967, 'mag': 1.35},
            {'name': 'Algieba', 'ra': 154.993, 'dec': 19.842, 'mag': 2.28}
        ]
    },
    'Sadr': {
        'hip': 100453,
        'constellation': 'Cygnus',
        'magnitude': 2.20,
        'distance_ly': 1832,
        'spectral_class': 'F8Ib',
        'ra_degrees': 305.557,
        'dec_degrees': 40.257,
        'age_billion_years': 0.012,
        'mass_solar': 12,
        'temperature_k': 5790,
        'history': """Sadr, 'o peito' em árabe, marca o centro da cruz do Cisne. É uma supergigante 
        amarela 65.000 vezes mais luminosa que o Sol. Está cercada por uma nebulosa de emissão difusa. 
        Apesar da grande distância, é facilmente visível, demonstrando sua enorme luminosidade real.""",
        'constellation_stars': [
            {'name': 'Sadr', 'ra': 305.557, 'dec': 40.257, 'mag': 2.20},
            {'name': 'Deneb', 'ra': 310.358, 'dec': 45.280, 'mag': 1.25},
            {'name': 'Albireo', 'ra': 292.680, 'dec': 27.960, 'mag': 3.18}
        ]
    },
    'Scheat': {
        'hip': 113881,
        'constellation': 'Pegasus',
        'magnitude': 2.42,
        'distance_ly': 196,
        'spectral_class': 'M2.5II-III',
        'ra_degrees': 345.944,
        'dec_degrees': 28.083,
        'age_billion_years': 0.100,
        'mass_solar': 2.1,
        'temperature_k': 3689,
        'history': """Scheat, 'a perna' em árabe, marca o canto noroeste do Grande Quadrado de Pégaso. 
        É uma gigante vermelha irregular variável. Perdeu massa significativa e está cercada por uma 
        concha de gás expandido. É uma das estrelas mais vermelhas visíveis a olho nu.""",
        'constellation_stars': [
            {'name': 'Scheat', 'ra': 345.944, 'dec': 28.083, 'mag': 2.42},
            {'name': 'Markab', 'ra': 346.190, 'dec': 15.205, 'mag': 2.48},
            {'name': 'Alpheratz', 'ra': 2.097, 'dec': 29.091, 'mag': 2.06}
        ]
    },
    'Mizar': {
        'hip': 65378,
        'constellation': 'Ursa Major',
        'magnitude': 2.27,
        'distance_ly': 82.9,
        'spectral_class': 'A2Vp',
        'ra_degrees': 200.981,
        'dec_degrees': 54.926,
        'age_billion_years': 0.370,
        'mass_solar': 2.2,
        'temperature_k': 8720,
        'history': """Mizar forma com Alcor o mais famoso par de estrelas do céu, usado como teste de 
        visão desde a antiguidade. É ela mesma um sistema quádruplo. Foi a primeira estrela dupla 
        descoberta com telescópio (1617) e a primeira binária espectroscópica fotografada (1889).""",
        'constellation_stars': [
            {'name': 'Mizar', 'ra': 200.981, 'dec': 54.926, 'mag': 2.27},
            {'name': 'Alkaid', 'ra': 206.885, 'dec': 49.313, 'mag': 1.86},
            {'name': 'Alioth', 'ra': 193.507, 'dec': 55.960, 'mag': 1.77}
        ]
    },
    'Ruchbah': {
        'hip': 6686,
        'constellation': 'Cassiopeia',
        'magnitude': 2.65,
        'distance_ly': 99.4,
        'spectral_class': 'A5IV',
        'ra_degrees': 21.454,
        'dec_degrees': 60.235,
        'age_billion_years': 0.600,
        'mass_solar': 2.0,
        'temperature_k': 7980,
        'history': """Ruchbah, 'o joelho' em árabe, é a estrela delta de Cassiopeia. É uma binária 
        eclipsante com pequenas variações. Marca o joelho da rainha Cassiopeia na figura mitológica. 
        Tem uma companheira anã que a orbita a cada 460 dias, causando eclipses parciais.""",
        'constellation_stars': [
            {'name': 'Ruchbah', 'ra': 21.454, 'dec': 60.235, 'mag': 2.65},
            {'name': 'Schedar', 'ra': 10.127, 'dec': 56.537, 'mag': 2.23},
            {'name': 'Caph', 'ra': 2.295, 'dec': 59.150, 'mag': 2.27}
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