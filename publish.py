
import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883)
mqttc.publish("hackher413", "Door Unlocked")
mqttc.loop(2)
