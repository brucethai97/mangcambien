import conn #Ket noi voi module connect database
import pymysql.cursors
from random import randint
import time
import random
from datetime import datetime, timedelta
connection = conn.getConnection() #Goi ham ket noi database
cursor = connection.cursor() 
print ("Connect successfull!")
#Ham tao bang
def tables():
 cursor.execute("drop table if exists sensors")
 sql = """create table sensors(
            id int(10) primary key auto_increment,
            temperature int(3) not null,
            humidity int(3) not null,
            time datetime not null
           )
        """
 cursor.execute(sql)
 connection.close()
#random insert 10 gia tri
def israndoms():
  try:
    for x in range(0,10):
      temp = randint(20,40)
      humi = randint(20,35)
      start = datetime.now()
      end = start + timedelta(days=2)
      randomdate = start + (end - start) * random.random()
      if temp !='' and humi !='' and randomdate !='':
        sql = "insert into sensors(temperature,humidity,time) values (%s,%s,%s)"
        cursor.execute(sql,(temp,humi,randomdate)) 
        connection.commit() # commit to insert records into database
  except:
    connection.rollback()
#Ham insert
def inserts():
 try:
  sql = "insert into sensors(temperature,humidity,time) values (12,05,'1996-12-05 12:05:30')"
  cursor.execute(sql)
  connection.commit()
 except:
  connection.rollback()
#Ham select
def selects():
 try:
  sql = "select * from sensors"
  cursor.execute(sql)
  results = cursor.fetchall()
  print (results)
 except:
  print ("Khong co du lieu")
 connection.close()

#Sap xep tang,giam theo truong trong bang
def selected(a,b):
 try:
  if a == 'id':
    if b == 'tang':
      sql = "select * from sensors order by id asc"
    if b == 'giam':
      sql = "select * from sensors order by id desc"
  if a == 'temperature':
    if b == 'tang':
      sql = "select * from sensors order by temperature asc"
    if b == 'giam':
      sql = "select * from sensors order by temperature desc"
  if a == 'humidity':
    if b == 'tang':
      sql = "select * from sensors order by humidity asc"
    if b == 'giam':
      sql = "select * from sensors order by humidity desc"
  if a == 'time':
    if b == 'tang':
      sql = "select * from sensors order by time asc"
    if b == 'giam':
      sql = "select * from sensors order by time desc"
  cursor.execute(sql)
  results = cursor.fetchall()
  print("id","\t")
  print (results[0])
 except:
  print ("Khong co du lieu")
 connection.close()
#ham Update
def updates():
 try:
  sql = "update sensors set temperature=40, humidity=50 where id = 1"
  cursor.execute(sql)
  connection.commit()
 except:
  connection.rollback()
 connection.close()
#Ham Delete
def deletes():
 try:
  sql = "delete from sensors where id<2"
  cursor.execute(sql)
  connection.commit()
 except:
  connection.rollback()
 connection.close()
