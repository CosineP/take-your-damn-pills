import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883)
#mqttc.connect("iot.eclipse.org", 1883)
#pay = '{"ble":"98:D3:31:90:86:16", "cmd":"Door Locked"}'
mqttc.publish("hackher413", "Door Unlocked")
mqttc.loop(2) #timeout = 2s
#esp8266simran