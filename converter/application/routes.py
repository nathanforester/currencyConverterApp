from flask import Flask, jsonify, Response, message_flashed 
import sys
from flask import jsonify
from flask import jsonify
import json
from flask import json
from datetime import datetime

app = Flask(__name__)


@app.route('/result/<convertedCurrency>', methods=['GET', 'POST'])
def convertedCurrency(convertedCurrency):
    try:
        convertedCurrency = int(float(convertedCurrency))
    except ValueError:
        return "ValueError: enter a number"
    if convertedCurrency < 0:
        return 'Please enter at least 1'
    else:
        convertedCurrency = convertedCurrency * 1.25
    return str(convertedCurrency)
    