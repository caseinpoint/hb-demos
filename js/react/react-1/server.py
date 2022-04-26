from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/red-button')
def red_button():
    return render_template('red-button.html')

@app.route('/click-counter')
def click_counter():
    return render_template('click-counter.html')

@app.route('/no-react')
def no_react():
    return render_template('no-react.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
