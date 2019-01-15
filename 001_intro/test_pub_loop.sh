#!/bin/bash 
COUNTER=0
while [  $COUNTER -lt 50 ]; do
     echo The counter is $COUNTER
     let COUNTER=COUNTER+1 
     mosquitto_pub -h 192.168.0.200 -t 'test/counter' -m $COUNTER
     sleep 1
done
