import RPi.GPIO as GPIO

LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
try:
  print('Press Ctrl-C to stop program')
  GPIO.output(LED_PIN, GPIO.HIGH)
  while True:
    next
except KeyboardInterrupt:
  print('Program terminated')
finally:
  GPIO.cleanup()
