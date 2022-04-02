from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)





camera = PiCamera()
GPIO.output(pin, GPIO.HIGH)
camera.start_preview()

sleep(100)
camera.stop_preview()



  
