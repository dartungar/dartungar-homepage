def calculate_tariff(point_a, point_b, direction=0, vehicle_type='oslik'):
	'''primitive tariff calculator with hard-coded values'''
	
	# coefficents for calculating tariff
	coeff = [1.3, 0.7, 1, 1]
	price_km = {'tent20': 17, 'ref20': 34, 'tank20': 18, 'oslik': 1}
	price_hours = {'tent20': 1703, 'ref20': 1800, 'tank20': 1500, 'oslik': 1}

	# getting distance from Google Maps Distance Matrix API
	distance = get_distance_from_googlemaps(point_a, point_b)

	# calculating average time in travel
	hours_travel = distance / 60
	hours_total = hours_travel + 3

	# if vehicle is tank trailer, it's always a round trip (coefficient = 2)
	coeff_final = 2 if vehicle_type == 'tank20' else coeff[direction]

	# a primitive tariff calculation
	tariff = (distance * price_km[vehicle_type] + hours_total * price_hours[vehicle_type]) * coeff_final
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