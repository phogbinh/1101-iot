import RPi.GPIO as GPIO
import time

SOUND_SPEED = 34300 # centimeters / second
TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
  GPIO.output(TRIG, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(TRIG, GPIO.LOW)
  while GPIO.input(ECHO) == 0:
    next
  start = time.time()
  while GPIO.input(ECHO) == 1:
    next
  end = time.time()
  distanceTraveled = SOUND_SPEED * (end - start)
  return distanceTraveled / 2 # go back and forth

while True:
  print('{}{:.1f}{}'.format('Distance: ', get_distance(), 'cm'))
