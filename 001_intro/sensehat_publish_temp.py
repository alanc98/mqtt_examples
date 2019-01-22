from sense_emu import SenseHat
# from sense_hat import SenseHat

import time
import paho.mqtt.client as mqtt

# Change broker_address to match the address of your Pi
broker_address = "192.168.0.200"
client = mqtt.Client("PYTHONTEST")
client.connect(broker_address)

sense = SenseHat()

while True:
    temp = sense.temp
    client.publish('test/temperature', sense.temp)
    time.sleep(1)
