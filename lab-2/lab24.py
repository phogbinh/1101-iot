# because adafruit was installed for python2,
# this code should only be run with python2

import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from threading import Thread

SOUND_SPEED = 34300 # centimeters / second
RANGE = [0, 8, 25]
INTERVAL = [0.1, 0.3, 1]

DHT_SENSOR = Adafruit_DHT.DHT22
GPIO_DHT = 4
GPIO_BUZZER = 2
GPIO_TRIGGER = 23
GPIO_ECHO = 24

is_blink = False
thread = None

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

def blink(interval):
  while is_blink:
    GPIO.output(GPIO_BUZZER, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(GPIO_BUZZER, GPIO.LOW)
    time.sleep(interval)

try:
  print('Press Ctrl-C to terminate the program')
  while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, GPIO_DHT)
    if humidity is not None and temperature is not None:
      print('Temp={0:0.2f}*C Humidity={1:0.2f}%'.format(temperature, humidity))
      distance = get_distance(temperature)
      print('Distance: {:.1f}cm'.format(distance))
      interval = INTERVAL[2]
      if (RANGE[0] < distance <= RANGE[1]):
        interval = INTERVAL[0]
      elif (RANGE[1] < distance <= RANGE[2]):
        interval = INTERVAL[1]
      if thread is not None:
        is_blink = False
        thread.join()
      is_blink = True
      thread = Thread(target=blink, args=(interval, ))
      thread.start()
    else:
      print('Fail to retrieve data from sensor DHT22')
except KeyboardInterrupt:
  print('Program terminated')
finally:
  if thread is not None:
    is_blink = False
    thread.join()
  GPIO.cleanup()
