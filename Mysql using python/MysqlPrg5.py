import mysql.connector as msc
mydb= msc.connect(host="localhost", user="root", password="1379", database="python_database")
mycursor=mydb.cursor()

# mycursor.execute("show tables")
# for i in mycursor:
    # print(i)

# mycursor.execute("select * from students where name=\'Rishu\'")
# mycursor.execute("select * from students where name like 'R%'")


sql = "select * from students where name = %s "
mycursor.execute(sql, ("Rishu", ))
myresult=mycursor.fetchall()
for i in myresult:
    print(i)