# because adafruit was installed for python2,
# this code should only be run with python2

import Adafruit_DHT
import RPi.GPIO as GPIO
import time

SOUND_SPEED = 34300 # centimeters / second
BUZZER_TIME_SCALE = 10

DHT_SENSOR = Adafruit_DHT.DHT22
GPIO_DHT = 4
GPIO_BUZZER = 2
GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_BUZZER, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def get_distance(temperature):
  GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(GPIO_TRIGGER, GPIO.LOW)
  while GPIO.input(GPIO_ECHO) == 0:
    next
  start = time.time()
  while GPIO.input(GPIO_ECHO) == 1:
    next
  end = time.time()
  distanceTraveled = (SOUND_SPEED + 60 * temperature) * (end - start)
  return distanceTraveled / 2 # go back and forth

while True:
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, GPIO_DHT)
  if humidity is not None and temperature is not None:
    print('Temp={0:0.2f}*C Humidity={1:0.2f}%'.format(temperature, humidity))
    distance = get_distance(temperature)
    print('Distance: {:.1f}cm'.format(distance))
    GPIO.output(GPIO_BUZZER, GPIO.HIGH)
    time.sleep(distance / BUZZER_TIME_SCALE)
    GPIO.output(GPIO_BUZZER, GPIO.LOW)
  else:
    print('Fail to retrieve data from sensor DHT22')
