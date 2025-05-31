"""
Constellation Data para Murphy-1
Dados das constelações e suas estrelas
"""

def get_constellation_data():
    """
    Retorna dados das constelações principais
    """
    return {
        'Orion': {
            'name': 'Órion',
            'stars': ['Betelgeuse', 'Rigel', 'Bellatrix'],
            'mythology': 'O grande caçador'
        },
        'Ursa Major': {
            'name': 'Ursa Maior',
            'stars': ['Dubhe', 'Merak', 'Phecda'],
            'mythology': 'A grande ursa'
        },
        'Lyra': {
            'name': 'Lira',
            'stars': ['Vega'],
            'mythology': 'A lira de Orfeu'
        },
        'Canis Major': {
            'name': 'Cão Maior',
            'stars': ['Sirius'],
            'mythology': 'O cão de Órion'
        }
    } 