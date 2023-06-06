from flask import Flask, jsonify, Response, message_flashed 
import sys
from flask import jsonify
from flask import jsonify
import json
from flask import json
from datetime import datetime

app = Flask(__name__)


@app.route('/result/<converted>', methods=['GET', 'POST'])
def convertedCurrency(converted):
    try:
        converted = int(float(converted))
    except ValueError:
        return "ValueError: enter a number"
    if converted < 1:
        return 'Please enter at least 1'
    else:
        converted = converted * 1.25
    return str(converted)
    