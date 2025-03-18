from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulacion')
def croquis():
    return render_template('croquis.html')

@app.route('/x')
def croquis2():
    return render_template('croquis2.html')



if __name__ == '__main__':
    app.run(debug=True)
