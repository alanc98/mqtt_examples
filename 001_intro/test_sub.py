#!/usr/bin/env python
import time
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
   print ('got a message !')
   print (message.payload) 

# Change broker_address to match the address of your Pi
broker_address = '192.168.0.200'
client = mqtt.Client("TEST")
client.on_message = on_message
client.connect(broker_address)
client.loop_start()
client.subscribe('test/temperature')

try:
   while True:
      time.sleep(5)

except KeyboardInterrupt:
   client.loop_stop()
   pass 
