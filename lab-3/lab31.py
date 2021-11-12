import RPi.GPIO as GPIO
from time import sleep
import time

# gpio indices
YELLOW = 2
WHITE = 3

GPIO.setmode(GPIO.BCM) # set gpio pin numbering as BCM
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(WHITE, GPIO.OUT)

timeout = time.time() + 10 # 10 seconds from now

def lit(gpio_index, duration):
  GPIO.output(gpio_index, GPIO.HIGH)
  sleep(duration)
  GPIO.output(gpio_index, GPIO.LOW)

while time.time() < timeout:
  lit(YELLOW, 1)
  lit(WHITE, 1)

GPIO.cleanup()
