from flask import Flask, render_template, request
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
	if request.method == 'GET':
		return render_template('apps.html')
	else:
		kilometers = request.form['kilometers']
		direction = request.form['direction']
		tariff = calculate_tariff(int(kilometers), int(direction))
		return render_template('calculate.html', tariff=tariff)
	


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7700)