import mysql.connector as msc 
mydb=msc.connect(host="localhost", user="root", password="1379")

mycursor=mydb.cursor()
mycursor.execute("use python_database")
mycursor.execute("select * from students order by age ")
# mycursor.execute("select name from students")
myresult=mycursor.fetchall()
# myresult=mycursor.fetchone()
for i in myresult:
    print(i)