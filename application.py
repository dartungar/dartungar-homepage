from flask import Flask, render_template, request

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
def apps_calculate():
	if request.method == 'GET':
		return render_template('apps.html')
	else:
		return render_template('calculate.html')





if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7700)