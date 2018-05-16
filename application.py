from flask import Flask, render_template, redirect, request
from seofy import import_spice, seofy_text
from tariff_calc import calculate_tariff 

# configure Flask
app = Flask(__name__)

# main page - TODO
@app.route('/')
def index():
	return render_template('index.html')

# blog - TODO
@app.route('/blog/')
def blog():
	return render_template('blog.html')

# a page for my wife
@app.route('/kotusenichki/')
def kotusenichki():
	return render_template('kotusenichki.html')


# my apps catalogue - TODO
@app.route('/apps/', methods=['GET', 'POST'])
def apps():
	return render_template('apps.html')

# tariff calculator
@app.route('/apps/calc/', methods=['GET', 'POST'])
def calc():
	# if data is submitted via form, calculate the tariff
	if request.method == 'POST':
		# determine if user wants halyava
		# using request.form.get to avoid errors if 'taxes' is unchecked
		taxes = request.form.get('taxes', 0)
		# if he does not want halyava, calculate an honest tariff ...
		if taxes:
			# ... based on distance, direction and the type of vehicle
			tariff = calculate_tariff(
				distance=int(request.form['kilometers']), 
				direction=int(request.form['direction']), 
				vehicle_type=request.form['vehicle-type'])
			# output page with calculated tariff
			return render_template('calculated_tariff.html', tariff=tariff)	
		else:
			# if user wants halyava, guide him to the right path :)
			return redirect('https://nalog.ru/', code=302)
	# generate page with forms
	else:
		return render_template('calc.html')

# SEO phrases generator
@app.route('/apps/seofy/', methods=['GET', 'POST'])
def seofy():
	# if data is submitted, generate SEO phrases
	if request.method == 'POST':
		# import phrases to spice up user input
		spice = import_spice('static/spice.txt')
		# get user input from textarea
		seofied_text = seofy_text(request.form['raw_text'], spice)
		# generate SEO phrases
		return render_template('seofied_text.html', seofied_text=seofied_text)
	# 
	else:
		return render_template('seofy.html')

@app.errorhandler(400)
def bad_request(e):
	return render_template('error.html', error='Неправильный запрос!'), 400

@app.errorhandler(404)
def not_found(e):
	return render_template('error.html', error='Нет такой страницы!'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('error.html', error='Что-то пошло не так!'), 500

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7700)