"""
Star Data Extended - Catálogo massivo de estrelas conhecidas
"""

# Importar o catálogo do star_data
from app.star_data import NAMED_STARS, find_nearest_named_star

# Exportar as funções
__all__ = ['NAMED_STARS', 'find_nearest_named_star']

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