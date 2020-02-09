import paho.mqtt.client as mqtt
import json
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("hackher413")
	
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	msg = msg.payload.decode()
	print(msg)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()

# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
