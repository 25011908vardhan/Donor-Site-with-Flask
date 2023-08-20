import mysql.connector as mysql
from  datetime import datetime
db=mysql.connect(host="localhost",user="root",passwd="",database="dbmsreg")
cursor=db.cursor()
def insert(name,email,phone):
    sql="insert into information (name,email,phone,date) values (%s,%s,%s,%s)"
    val=(name,email,phone,datetime.today())
    cursor.execute(sql,val)
    db.commit()
def display():
    sql="select * from information"
    cursor.execute(sql)
    data=cursor.fetchall()
    if len(data)==0:
        sql="alter table information auto_increment = 1 "
        cursor.execute(sql)
    # print(type(data[0][0]))
    # for x in data:
    #     print(x[1])
    # print(type(data))
    return data
def delete(id):
    sql="delete from information where id= (%s)"
    # val = ()
    val=(str(id),)
    cursor.execute(sql,val)
    db.commit()