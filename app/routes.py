# import some functions and classes from external packages
from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

# tell program what naming convention to use to identify I/O pins
GPIO.setmode(GPIO.BCM)
# suppress GPIO warninga
GPIO.setwarnings(False)
# tell Python that pin 18 will be used to output information
GPIO.setup(18,GPIO.OUT)

# initialuse the web app
app = Flask(__name__)

# define some 'routes' or 'views' in the app
@app.route('/')
def home():
    return render_template('index.html', status='off')

@app.route('/on')
def on():
    # Task 1b: put code here to turn light ON
    GPIO.output(18,GPIO.HIGH)
    return render_template('index.html', status='on')

@app.route('/off')
def off():
    # Task 1b: put code here to turn light OFF
    GPIO.output(18,GPIO.LOW)
    return render_template('index.html', status='off')

if __name__ == "__main__":
    app.run()
