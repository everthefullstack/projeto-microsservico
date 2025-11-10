from math import radians, sin, cos, sqrt, atan2


#calcula a distância entre dois pontos na superfície da Terra usando a fórmula de Haversine
def calcular_latitude_longitude(lat1, lon1, lat2, lon2):
    # Converte todos os valores para float
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)

    R = 6371  # raio da Terra em km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c
