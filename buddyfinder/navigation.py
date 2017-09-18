import math


def haversine_formula_distance(coord1, coord2):
    """
    Formula for calculating the shortest distance as-the-crow-flies over the earth's surface. Code based on the blog
    post at http://www.movable-type.co.uk/scripts/latlong.html.
    :param coord1: Two-element tuple containing coordinates for first point in degrees.
    :param coord2: Two-element tuple containing coordinates for second point in degrees.
    :return: Distance in kilometers between the two points.
    """

    # Constant for average radius of the earth in kilometers
    r = 6371

    # Coordinates are in degrees, so convert to radians and calculate deltas
    lat_1, long_1 = coord1
    lat_2, long_2 = coord2
    phi_1 = math.radians(lat_1)
    phi_2 = math.radians(lat_2)
    delta_phi = math.radians(lat_2 - lat_1)
    delta_lambda = math.radians(long_2 - long_1)

    # a = sin^2(Δφ/2) + cos(φ1) * cos(φ2) + sin^2(Δλ/2)
    # c = 2 * atan2(√a, √(1-a))
    # d = r * c
    a = math.sin(delta_phi / 2)**2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c
    return d
