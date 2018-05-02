def calculate_tariff(kilometers, direction=1):
	coeff = [1.3, 0.7, 1, 1]
	tariff = kilometers * coeff[direction]
	return tariff