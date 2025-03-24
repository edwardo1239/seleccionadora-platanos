import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 17

GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.HIGH)

time.sleep(1)

GPIO.output(pin, GPIO.LOW)

time.sleep(1)

GPIO.cleanup()
print("apagado")