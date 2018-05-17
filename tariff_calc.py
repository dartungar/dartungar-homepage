def calculate_tariff(point_a, point_b, direction=1, vehicle_type='oslik'):
	'''primitive tariff calculator with hard-coded values'''
	
	# coefficents for calculating tariff
	coeff = [1.3, 0.7, 1, 1]
	price = {'tent20': 35, 'ref20': 38, 'tank20': 90, 'oslik': 1}

	# getting distance from Google Maps Distance Matrix API
	distance = get_distance_from_googlemaps(point_a, point_b)

	# a primitive tariff calculation
	tariff = distance * coeff[direction] * price[vehicle_type]
	tariff = round(tariff, -2)

	return tariff


# function to calculate distance between two or more points
# using Google Distance Matrix API
def get_distance_from_googlemaps(a, b):
	'''sends points A and B to Google Maps Distance Matrix API
		and gets the distance between from returned data'''
		
	import googlemaps

	# api key is stored in a txt file
	# I will find a way to store it more secure
	with open('gmaps_api.txt') as file:
		api_key = file.read()

	# setting up google maps client
	gmaps = googlemaps.Client(key=api_key)

	# getting distance matrix for points a and b
	matrix = gmaps.distance_matrix(a, b)

	# getting distance for distance matrix
	# as kilometers
	# (should find a way to process JSON results more reliably?..)
	distance_km = round(matrix['rows'][0]['elements'][0]['distance']['value'] / 1000)
	return distance_km