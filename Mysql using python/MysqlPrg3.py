import mysql.connector as msc 
mydb=msc.connect(host="localhost", user="root", password="1379")

mycursor=mydb.cursor()
# mycursor.execute("show databases")
# for i in mycursor:
#     print(i)

mycursor.execute("use python_database")
mycursor.execute("show tables")
for i in mycursor:
    print(i)

# size=int(input("Enter the size : "))      # wrong way of inserting data
# for i in range(size):
#     name=input("Enter the Name : ")
#     age=int(input("Enter the age : "))
# mycursor.execute(f"insert into school(name, age) values ({name}, {age})")
# mycursor.execute("select * from students")
# for i in mycursor:
#     print(i)

sqlFormual= "INSERT INTO students (name, age) VALUES (%s, %s)"
# student1=("Rishu",22)

# mycursor.execute(sqlFormual,student1)
# mydb.commit()


size=int(input("Enter the size : "))  
list1=[]    
for i in range(size):
    name=input("Enter the Name : ")
    age=int(input("Enter the age : "))
    list1.append((name,age))
mycursor.executemany(sqlFormual,list1)

mydb.commit()
