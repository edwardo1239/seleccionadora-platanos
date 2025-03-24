import RPi.GPIO as GPIO
import time
import picamera

GPIO.setmode(GPIO.BCM)

x = True
TRIG = 4
ECHO = 18

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

camera = picamera.PiCamera()
camera.resolution = (400,400)
camera.shutter_speed = 10000

def sensor():
	GPIO.output(TRIG, True)
	time.sleep(0.00002)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO) == False:
	    start = time.time()

	while GPIO.input(ECHO) == True:
	    end = time.time()

	sig_time = end-start

	#CM:
	distance = sig_time / 0.000058

	print('Distance: {} centimeters'.format(distance))

	GPIO.cleanup()

	return distance

while x:
	distance = sensor()

	if distance > 45.5:
		dist = distance
		pass
	elif distance <= 45.5:
		peso = input("ingrese el peso:")
		if peso == "n":
			x = False
		altura = dist - distance
		picam.capture("{}_{}.jpg".format(str(altura), str(peso)))






