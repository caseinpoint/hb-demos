from flask import Flask, request, render_template, redirect, make_response

app = Flask(__name__)


def get_request_dict(rqst):
    request_data = {'req_method': rqst.method,
                    'req_protocol': rqst.scheme,
                    'req_url': rqst.url,
                    'req_headers': rqst.headers}

    if len(rqst.form) > 0:
        request_data['req_body'] = rqst.form

    return request_data


def get_response_dict(template=None, rdrct=None, **kwargs):
    if template is not None:
        rendered = render_template(template, **kwargs)
        res = make_response(rendered)
    elif rdrct is not None:
        res = rdrct

    res_data = {'res_protocol': 'http',
                'res_code': res.status,
                'res_headers': res.headers,
                'res_body': res.get_data(as_text=True)}
    return res_data


@app.route('/')
def show_request_data():
    request_data = get_request_dict(rqst=request)

    return render_template('base.html', **request_data)


@app.route('/get-form')
def show_get_form():
    request_data = get_request_dict(rqst=request)

    return render_template('get-form.html', **request_data)


@app.route('/handle-get-form')
def handle_get_form():
    request_data = get_request_dict(rqst=request)
    form_data = {'name': request.args.get('name'),
                 'quest': request.args.get('quest'),
                 'color': request.args.get('color'),
                 'next': '/post-form'}

    return render_template('form-output.html', **request_data, **form_data)


@app.route('/post-form')
def show_post_form():
    request_data = get_request_dict(rqst=request)

    return render_template('post-form.html', **request_data)


@app.route('/handle-post-form', methods=['POST'])
def handle_post_form():
    request_data = get_request_dict(rqst=request)
    form_data = {'name': request.form.get('name'),
                 'quest': request.form.get('quest'),
                 'color': request.form.get('color'),
                 'next': '/response'}
    
    return render_template('form-output.html', **request_data, **form_data)


@app.route('/response')
def show_response():
    request_data = get_request_dict(rqst=request)
    response_data = get_response_dict(template='base.html',
                                      rdrct=None,
                                      **request_data)

    return render_template('response.html', **request_data, **response_data)


@app.route('/redirect')
def demo_redirect():
    request_data = get_request_dict(rqst=request)
    response_data = get_response_dict(template=None,
                                      rdrct=redirect('/response'),
                                      **request_data)

    return render_template('response.html', **request_data, **response_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')