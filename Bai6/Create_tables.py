import pymysql
db = pymysql.connect("localhost","root","123456","wsn")
cursor = db.cursor()
cursor.execute("drop table if exists sensors")
sql = """create table sensors(
			id int(10) primary key auto_increment,
			sensor_id char(10) not null,
			temperature int(3) not null,
			humidity int(3) not null,
			date_time char(30) not null
			)"""
cursor.execute(sql)
db.close()