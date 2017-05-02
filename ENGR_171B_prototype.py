import io
import picamera
import cv2
import numpy
import RPi.GPIO as GPIO
import time
import os
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

def led_flash(pin):
	pin = int(pin)
	for i in range(0, 10):
		GPIO.output(pin, 1)
		time.sleep(0.05)
		GPIO.output(pin, 0)
		time.sleep(0.05)

# Define function for button press
def ledSwitch(channel):
	print('Button Pressed')
	GPIO.output(5,1)
	GPIO.output(6,1)	
	#Create a memory stream so photos doesn't need to be saved in a file
	stream = io.BytesIO()

	#Get the picture (low resolution, so it should be quite fast)
	#Here you can also specify other parameters (e.g.:rotate the image)
	with picamera.PiCamera() as camera:
	    camera.resolution = (720, 540)
	    camera.capture(stream, format='jpeg')

	#Convert the picture into a numpy array
	buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

	#Now creates an OpenCV image
	image = cv2.imdecode(buff, 1)

	#Load a cascade file for detecting faces
	face_cascade = cv2.CascadeClassifier('/home/pi/faces.xml')

	#Convert to grayscale
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	#Look for faces in the image using the loaded cascade file
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)

	GPIO.output(6,0)
	GPIO.output(5,0)
	print "Found "+str(len(faces))+" face(s)"
	if(len(faces) > 0):
		flashing_thread = threading.Thread(target=led_flash, args='6')
		flashing_thread.start()
	else:
		flashing_thread = threading.Thread(target=led_flash, args='5')
		flashing_thread.start()
	

	#Draw a rectangle around every found face
	for (x,y,w,h) in faces:
	    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

	#Save the result image
	cv2.imwrite('result.jpg',image)
	GPIO.output(6,0)
	GPIO.output(5,0)

# Set the interrupt - call ledSwitch function on button press - set debounce
GPIO.add_event_detect(4, GPIO.RISING, callback = ledSwitch, bouncetime = 2000)


try:
    while True:
        time.sleep(60)

except KeyboardInterrupt:
    GPIO.cleanup()