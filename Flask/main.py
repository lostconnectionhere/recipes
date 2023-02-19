from flask import Flask, render_template
app = Flask(__name__)
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/')
def hello():
    return render_template('index.html')

app.run(host='0.0.0.0',port=8001)

