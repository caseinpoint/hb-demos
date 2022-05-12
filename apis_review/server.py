from flask import Flask, request, render_template, jsonify
from jinja2 import StrictUndefined
from requests import get
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = environ['APP_SECRET']
app.jinja_env.undefined = StrictUndefined

GOOGLE_API = environ['GOOGLE_API']


@app.route('/')
def index():
    """Display the index."""

    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    """Display and handle form."""

    if request.method == 'GET':
        return render_template('form.html')

    else:
        search_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
        parameters = {
            'key': GOOGLE_API,
            'query': request.form.get('query'),
            'location': '37.8210207,-122.248357',
            'radius': 5000
        }

        response = get(search_url, params=parameters)
        results = response.json()['results']

        photos_url = f'https://maps.googleapis.com/maps/api/place/photo?key={GOOGLE_API}&maxheight=400&maxwidth=400&photo_reference='

        return render_template('form-results.html',
                               results=results,
                               photos_url=photos_url)


@app.route('/ajax')
def ajax():
    """Display AJAX page."""

    return render_template('ajax.html')


@app.route('/places.json')
def handle_ajax():
    """Return Places API search JSON."""

    search_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    parameters = {
        'key': GOOGLE_API,
        'query': request.args.get('query'),
        'location': '37.8210207,-122.248357',
        'radius': 5000
    }

    response = get(search_url, params=parameters)

    results = {
        'results': response.json()['results'],
        'photos_url': f'https://maps.googleapis.com/maps/api/place/photo?key={GOOGLE_API}&maxheight=400&maxwidth=400&photo_reference='
    }
    return jsonify(results)


@app.route('/autocomplete')
def autocomplete():
    """Display autocomplete page."""

    return render_template('autocomplete.html')


@app.route('/autocomplete.json')
def handle_autocomplete():
    """Return Autocomplete API JSON."""

    query = request.args.get('query')

    auto_url = 'https://maps.googleapis.com/maps/api/place/queryautocomplete/json'
    parameters = {
        'key': GOOGLE_API,
        'input': query,
        'location': '37.8210207,-122.248357',
        'radius': 10000,
        'offset': len(query)
    }

    response = get(auto_url, params=parameters)
    predictions = response.json()['predictions']

    descriptions = []
    for prediction in predictions:
        descriptions.append(prediction['description'])
    print(descriptions)

    return jsonify(descriptions)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
