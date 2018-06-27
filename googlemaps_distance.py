# function to calculate distance between two or more points
# using Google Distance Matrix API


def get_distance_from_googlemaps(a, b, api_key):
    '''sends points A and B too Google Maps Distance Matrix API
            and gets the distance between from returned data'''
    import googlemaps

    # setting up google maps client
    gmaps = googlemaps.Client(key=api_key)

    # getting distance matrix for points a and b
    matrix = gmaps.distance_matrix(a, b)

    # getting distance for distance matrix
    # as kilometers
    distance_km = round(matrix['rows'][0]['elements']
                        [0]['distance']['value'] / 1000)
    return distance_km
