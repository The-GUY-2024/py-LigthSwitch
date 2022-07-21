from distutils.log import debug
import os
from re import template
import RPi.GPIO as GPIO
from flask import Flask, render_template, Response
import datetime

GPIO.setmode(GPIO.BCM)
dataPin=[i for i in range(2,28)]
for dp in dataPin: GPIO.setup(dp,GPIO.IN)

data=[]

templateData={
    'title':'Room Ligth-Py',
    'data':data,
}



app=Flask(__name__)

@app.route('/')
def index():
    templateData={
        'title':'Room Ligth-Py',
        'data':data,
    }
    return render_template('index.html', **templateData)

@app.route('/<actionid>')
def handleRequest(actionid):
    print("Button pressed: {}".format(actionid));
    
    return "ok 200"


if __name__ == '__main__':

    app.run(debug=True, port=5000, host='0.0.0.0', threaded=True)
    