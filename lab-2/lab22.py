# because adafruit was installed for python2,
# this code should only be run with python2

import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
  if humidity is not None and temperature is not None:
    print('Temp={0:0.2f}*C Humidity={1:0.2f}%'.format(temperature, humidity))
  else:
    print('Fail to retrieve data from sensor DHT22')
