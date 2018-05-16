def calculate_tariff(distance=1, direction=1, vehicle_type='oslik'):
	'''primitive tariff calculator with hard-coded values'''

	coeff = [1.3, 0.7, 1, 1]
	price = {'tent20': 35, 'ref20': 38, 'tank20': 90, 'oslik': 1}
	# как примитивно! надо 
	tariff = distance * coeff[direction] * price[vehicle_type]
	tariff = round(tariff, -2)

	return tariff