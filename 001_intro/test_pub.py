#!/usr/bin/env python

import time
import paho.mqtt.client as mqtt

# Change broker_address to match your Pi
broker_address = "192.168.0.200"
client = mqtt.Client("TESTPC")
client.connect(broker_address)

client.publish('test/temperature', 28.445)

