import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="1379", database= "python_database")
print(mydb)
print()

mycursor=mydb.cursor()
# str1=input("Enter the name of Database to be created : ")
# mycursor.execute(f"CREATE DATABASE {str1}")
# print("Database created")

# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
    # print(i)

# mycursor.execute("CREATE TABLE students(name varchar(10) not null, age int not null )")

mycursor.execute("SHOW tables")
for i in mycursor:
    print(i)
