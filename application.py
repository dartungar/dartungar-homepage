from flask import Flask, render_template, request
from seofy import import_spice, seofy_text
from tariff_calc import calculate_tariff 

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/blog/')
def blog():
	return render_template('blog.html')

@app.route('/kotusenichki/')
def kotusenichki():
	return render_template('kotusenichki.html')

@app.route('/apps/', methods=['GET', 'POST'])
def apps():
	return render_template('apps.html')

@app.route('/apps/calc/', methods=['GET', 'POST'])
def calc():
	if request.method == 'GET':
		return render_template('calc.html')
	else:
		tariff = calculate_tariff(int(request.form['kilometers']), int(request.form['direction']))
		return render_template('calculated_tariff.html', tariff=tariff)	

@app.route('/apps/seofy/', methods=['GET', 'POST'])
def seofy():
	if request.method == 'GET':
		return render_template('seofy.html')
	else:
		spice = import_spice('static/spice.txt')
		seofied_text = seofy_text(request.form['raw_text'], spice)
		return render_template('seofied_text.html', seofied_text=seofied_text)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7700)