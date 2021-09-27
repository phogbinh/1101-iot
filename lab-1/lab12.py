import RPi.GPIO as GPIO
from time import sleep
import time

# gpio indices
RED = 2
YELLOW = 3
GREEN = 4

GREEN_TIME = 3
YELLOW_TIME = 1
RED_TIME = 5

GPIO.setmode(GPIO.BCM) # set gpio pin numbering as BCM
for i in range(2, 5):
  GPIO.setup(i, GPIO.OUT)

timeout = time.time() + 10 # 10 seconds from now

def lit(gpio_index, duration):
  GPIO.output(gpio_index, GPIO.HIGH)
  sleep(duration)
  GPIO.output(gpio_index, GPIO.LOW)

while time.time() < timeout:
  lit(GREEN, GREEN_TIME)
  lit(YELLOW, YELLOW_TIME)
  lit(RED, RED_TIME)

GPIO.cleanup()
