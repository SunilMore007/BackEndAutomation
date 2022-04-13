import time

import paho.mqtt.client as mqtt  # import the client1

#broker = "121.0.0.1"

broker = "localhost"
port = 1883

client = mqtt.Client("MQTT python publisher")  # create new instance
client.connect(broker, port)  # connect to broker

