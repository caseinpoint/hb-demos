from flask import Flask, request, render_template, redirect, make_response

app = Flask(__name__)


@app.route('/')
def show_request_data():
    """Show the main attributes of the request object."""

    return render_template('base.html', request=request)


@app.route('/form/<method>')
def show_get_form(method):
    """Show a GET/POST form and the request object."""

    return render_template('form.html', request=request, method=method.upper())


@app.route('/form/submit', methods=['GET', 'POST'])
def handle_get_form():
    """Show the form data and the request object.
    
    This function demonstrates why you might want to know information about
    the request, itself.  I.e. a route that handles two different request
    methods."""

    if request.method == 'GET':
        form_data = {'name': request.args.get('name'),
                     'quest': request.args.get('quest'),
                     'color': request.args.get('color'),
                     'grenade': request.args.getlist('grenade'),
                     'next': '/form/POST'}

    else:
        form_data = {'name': request.form.get('name'),
                     'quest': request.form.get('quest'),
                     'color': request.form.get('color'),
                     'grenade': request.form.getlist('grenade'),
                     'next': '/response'}

    return render_template('form-output.html', request=request, **form_data)


@app.route('/response')
def show_response():
    """Show a response object and the request object."""

    rendered = render_template('base.html', request=request)
    response = make_response(rendered)

    return render_template('response.html', request=request, response=response)


@app.route('/redirect')
def demo_redirect():
    """Show a redirect response and the request object."""

    return render_template('response.html', request=request,
                           response=redirect('/response'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')