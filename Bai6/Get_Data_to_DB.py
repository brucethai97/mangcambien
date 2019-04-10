import pymysql
import json

def Sensor(jsonData):
	json_Dict = json.loads(jsonData.decode("utf-8"))
	SensorID = json_Dict['sensor_id']
	Temperature = json_Dict['temperature']
	Humidity = json_Dict['humidity']
	Data_time = json_Dict['date_time']
	db = pymysql.connect("localhost","root","123456","wsn")
	cursor = db.cursor()

	sql = "insert into sensors(sensor_id,temperature,humidity,date_time) values (%s,%s,%s,%s)"
	data = (SensorID,Temperature,Humidity,Data_time)
	cursor.execute(sql,data)
	db.commit()
	print("Sensor created new value")
	print("------------------------")
	db.close()