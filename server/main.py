from flask import Flask, request, Response,render_template
import json
import os
from paho.mqtt import client

app = Flask(__name__,template_folder='.')

mqttc = client.Client()
mqttc.connect("test.mosquitto.org", 1883)
#mqttc.connect("iot.eclipse.org", 1883)
#pay = '{"ble":"98:D3:31:90:86:16", "cmd":"Door Locked"}'

@app.route('/')
def login():
	return render_template('takeyourdamnpills.html')


@app.route('/set_alarm/', methods=['POST'])
def set_alarm():
  data = request.json
  
  mqttc.publish("hackher413", data['hours'] + ":" + data['minutes'])
  mqttc.loop(2) #timeout = 2s

  return 'success'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0',port='5000')

