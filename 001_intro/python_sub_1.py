#!/usr/bin/env python
import time
import paho.mqtt.client as mqtt

# This is callback function. It is called when 
# an MQTT message that you are subscribing to is received
def on_message(client, userdata, message):
   print ('got a message !')
   print (message.payload) 

# Change broker_address to match the address of your Pi
# Mine happens to be 192.168.0.200
broker_address = '192.168.0.200'

# Create the MQTT client object
client = mqtt.Client("PYTHONSUB1")

# Set the message callback function
client.on_message = on_message

# Connect to the MQTT Broker
client.connect(broker_address)

#
# This is the MQTT Client loop. 
# It is used to check for new messages.
# once this loop starts, the main program needs
# to sleep, or do something else  
client.loop_start()

# SUbscribe to a topic
client.subscribe('test/temperature')

# The main part of the program. This is where
# it can do something else, or just kill time while the 
# MQTT client is waiting for messages in the background
# we could publish MQTT messages here if we wnated to
try:
   while True:
      time.sleep(5)

# if the user presses control-c to quit, stop the MQTT loop
except KeyboardInterrupt:
   client.loop_stop()
   pass 
