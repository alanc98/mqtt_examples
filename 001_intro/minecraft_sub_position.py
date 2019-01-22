#!/usr/bin/env python

import time
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
   print "--->",message.topic, ":", message.payload

broker_address = "127.0.0.1"
client = mqtt.Client("MINECRAFTSUB")
client.on_message = on_message
client.connect(broker_address)
client.loop_start()
client.subscribe('minecraft/pos/x')
client.subscribe('minecraft/pos/y')
client.subscribe('minecraft/pos/z')

try:
   while True:
      time.sleep(5)

except KeyboardInterrupt:
   client.loop_stop()
   pass 
