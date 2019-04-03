import pymysql

def getConnection():
	#You can change the connection arguments.
	connection = pymysql.connect("localhost","root","123456","phamhongthai")
	return connection