# main.py

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='C:/Users/ADRIAN/PycharmProjects/pythonProject5')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index2.html')

@app.route('/portfolio')
def portfolio():
    return render_template('index3.html')

@app.route('/contact')
def contact():
    return render_template('index4.html')
if __name__ == '__main__':
    app.run(debug=True)
