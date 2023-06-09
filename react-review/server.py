from flask import Flask, render_template, send_file
from pathlib import Path
from time import sleep

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/api/cards.json')
def get_cards():
	# simulate slow api
	sleep(4)

	file_path = Path('./static/json/cards.json')
	return send_file(file_path, mimetype='application/json')


if __name__ == '__main__':
	app.run(debug=True)
