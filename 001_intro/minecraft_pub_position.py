import mcpi.minecraft as minecraft
import mcpi.block as block
import paho.mqtt.client as mqtt
import time

# Just using the local broker address
broker_address = "127.0.0.1"

def main():
   client = mqtt.Client("MINECRAFTPUB")
   client.connect(broker_address)
   print("Connected to MQTT broker")

   mc = minecraft.Minecraft.create()
   mc.postToChat("Hello Minecraft!, MQTT Here!")

   while (True):
      pos = mc.player.getTilePos()
      print ("Minecraft X: ", pos.x, "Minecraft Y: ",pos.y, "Minecraft Z: ", pos.z)
      client.publish('minecraft/pos/x',pos.x)
      client.publish('minecraft/pos/y',pos.y)
      client.publish('minecraft/pos/z',pos.z)

      time.sleep(1)

main()

