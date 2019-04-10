import paho.mqtt.client as mqtt
import random,json
from datetime import datetime
from time import sleep

#MQTT settings
MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "home/sensors"

# Ham ket noi den may chu MQTT
def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print ("Unable to connect to MQTT Broker...")
	else:
		print ("connected with MQTT Broker: " + str(MQTT_Broker))

def on_publish(client, userdata, mid):
	pass

def on_disconnect(client, userdata, rc):
	if rc != 0:
		pass

mqttc = mqtt.Client()
mqttc.username_pw_set(username="brucewayne",password="123456")
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)

#Publish data
def publish_to_topich(topic, message):
	mqttc.publish(topic,message)
	print (("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic)))
	print ("")

# fake randum sensors
def publish_fake_sensor_values_to_mqtt():
	Humidity_Fake_Value = int(random.uniform(50,100))
	Temperature_Fake_Value = int(random.uniform(20,30))
	Sensor_data = {}
	Sensor_data['sensor_id'] = "DHT-11"
	Sensor_data['temperature'] = Temperature_Fake_Value
	Sensor_data['humidity'] = Humidity_Fake_Value
	Sensor_data['date_time'] = (datetime.today()).strftime("%d-%b-%y %H:%M:%S")
	sensor_json_data = json.dumps(Sensor_data)
	print("Puplishing fake Sensor Value: ")
	publish_to_topich (MQTT_Topic, sensor_json_data)
	sleep(3)

while True:
	publish_fake_sensor_values_to_mqtt()
	sleep(3)