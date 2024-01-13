import mysql.connector as msc
mydb=msc.connect(host="localhost", user="root", password="1379", database="python_database")
# print(mydb.is_connected())

mycursor=mydb.cursor()
# sql="update students set age = 100 where name='Rishu' "
# mycursor.execute(sql)
# mydb.commit()
mycursor.execute("select * from students ")
myresult= mycursor.fetchall()
for i in myresult:
    print(i)
