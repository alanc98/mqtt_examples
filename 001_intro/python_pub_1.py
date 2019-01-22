#!/usr/bin/env python
import time
import paho.mqtt.client as mqtt

# Change broker_address to match the address of your Pi
broker_address = "192.168.0.200"
client = mqtt.Client("PYTHONPUB1")
client.connect(broker_address)

# Publish an MQTT message and quit
client.publish('test/temperature', 28.445)

