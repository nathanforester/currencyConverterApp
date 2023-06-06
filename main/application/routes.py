from flask import Flask
from application import app
import requests
from flask import render_template, request, redirect, url_for
import sys



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    formData = request.form.get('result')
    formData = str(formData)
    convertedCurrency = requests.post('http://converter:5001/result/' + formData)
    return render_template('convert.html', formData=formData, birthDate=convertedCurrency.text)

