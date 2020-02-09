import paho.mqtt.client as mqtt
import json
from gpiozero import LED, DistanceSensor

from datetime import datetime
from time import sleep

led = LED(17)
dist = DistanceSensor(trigger=27, echo=22)

led.off()
dont_reset = False

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("hackher413")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global goal_h
    global goal_m
    msg = msg.payload.decode()
    with open("last_date", "w") as ld:
        ld.write(msg)
    parse_date(msg)

def parse_date(date_str):
    global goal_h
    global goal_m
    print("setting time to ", date_str)
    date_str = date_str.split(":")
    goal_h = int(date_str[0])
    goal_m = int(date_str[1])

# hack to make sure we have internet on boot
sleep(45)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
# for if mosquitto decides to be annoying
#client.connect("iot.eclipse.org", 1883, 60)
# poor folks error handling
goal_h = "error"
goal_m = "error"
with open("last_date") as ld:
    parse_date(ld.read())

while True:
    print("working")
    client.loop()
    time = datetime.now()
    hour = time.hour
    min = time.minute
    big = .1
    if dist.distance > big and not dont_reset:
        print("thank you")
        led.off()
        dont_reset = True
    if hour >= goal_h and min >= goal_m:
        if not dont_reset:
            print("take your damn pills")
            led.on()
    else:
        # will happen around midnight (not very explicit i know, sorry)
        dont_reset = False
    sleep(0.5)

