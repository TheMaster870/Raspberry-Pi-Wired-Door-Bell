#Import statements
import RPi.GPIO as GPIO
import time
import requests

#URL to sent the POST request
url = "Enter_URL_Here"
#The message JSON object and it's value
data = {"message" : "Door bell"}

#Setup the GPIO pin
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Continuously check the pin
while True:
	input_state = GPIO.input(18)
	if input_state == False:
                #Print that the button has been pressed
		print("Button Pressed")
		#Send the POST request to the stored url and body data
		x = requests.post(url, json = data)
		#Print out any respose
		print(x.text)
		#Sleep to allow the button to be released
		time.sleep(0.2)
