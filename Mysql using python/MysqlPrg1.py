import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="1379")
if mydb.is_connected():
    print("connection succesfull")
    a=mydb.connection_id
    print(a)
    mydb.close()
else:
    print("Not succesfull")