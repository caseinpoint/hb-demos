from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('search.html')

@app.route('/search')
def search():
	artist = request.args.get('artist')

	payload = {'term': artist,
           'media': 'music',
           'attribute': 'artistTerm',
           'entity': 'musicTrack'}

	res = requests.get('https://itunes.apple.com/search',
                   params=payload)
	
	res_data = res.json()

	return render_template('results.html', results=res_data['results'])


if __name__ == '__main__':
	app.run(debug=True)