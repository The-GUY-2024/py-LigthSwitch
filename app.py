from distutils.log import debug
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

#Create a Dictionary called pins to store the pin information

pins = {
    4 : {'name' : 'GPIO 4', 'state' : GPIO.LOW}
}

#Set each pin as an output and make it low :

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
#For each pin read the pin state and store it 
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)
    #put the pin dictionary into the template data 
    templateData = {
        'pins' : pins
        }
    
    #pass the template data into the template main & return it to the terminal 
    return render_template('main.html', **templateData)


#The function below is executed when someone request a URL with the pin number and action in it 
#This is the communication part of this application
@app.route("/<changePin>/<action>")
def action(changePin, action):
    
    #Convert the pin from the URL into an integer:
    changePin = int(changePin)
    
    #Get the device name for the pin being change:
    deviceName = pins[changePin]['name']
    
    #If the action part of the Url is "(ON)", execute the code indented below:
    if (action == "on"):
        
        #set the pin high
        GPIO.output(changePin, GPIO.HIGH)
        
        #Save the status message to be passed into the template:
        message = "Turned " + deviceName + " on."
    if (action == "off"):
        GPIO.output(changePin, GPIO.LOW)
        message = "Turned " + deviceName + " off."
        
        
    #For each pin in the list (Pins), read the pin state and store it in the pins
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)
        
    #Along with the pn dictionary, Put the message into the template
    templateData = {
        'pins': pins
    }
    
    return render_template('main.html', **templateData)

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=80, debug=True);