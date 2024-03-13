from flask import Flask, request, render_template, redirect, make_response

app = Flask(__name__)


@app.route('/')
def show_request_data():
    """Show the main attributes of the request object."""

    print(f'\ntype of request: {type(request)}\n')

    return render_template('base.html')


@app.route('/response')
def show_response():
    """Show a response object and the request object."""

    rendered = render_template('base.html')
    print(f'\ntype of rendered: {type(rendered)}')

    response = make_response(rendered)
    print(f'type of response: {type(response)}\n')

    return render_template('response.html', response=response, next='/form/GET')


@app.route('/form/<method>')
def show_get_form(method):
    """Show a GET/POST form and the request object."""

    return render_template('form.html', method=method.upper())


@app.route('/form/submit', methods=['GET', 'POST'])
def handle_get_form():
    """Show the form data and the request object.
    
    This function demonstrates why you might want to know information about
    the request, itself.  I.e. a route that handles two different request
    methods."""

    if request.method == 'GET':
        print(f'\ntype of request.args: {type(request.args)}\n')

        form_data = {'name': request.args.get('name'),
                     'quest': request.args.get('quest'),
                     'color': request.args.get('color'),
                     'grenade': request.args.getlist('grenade'),
                     'next': '/form/POST'}

    else:
        print(f'\ntype of request.form: {type(request.form)}\n')

        form_data = {'name': request.form.get('name'),
                     'quest': request.form.get('quest'),
                     'color': request.form.get('color'),
                     'grenade': request.form.getlist('grenade'),
                     'next': '/redirect'}

    return render_template('form-output.html', **form_data)


@app.route('/redirect')
def demo_redirect():
    """Show a redirect response and the request object."""

    redirect_obj = redirect('/response')
    print(f'\ntype of redirect: {type(redirect_obj)}\n')

    return render_template('response.html',
                           response=redirect_obj, next='#')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')