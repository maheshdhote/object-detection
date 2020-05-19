import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="mahi123",auth_plugin='mysql_native_password')
print(mydb)
if(mydb):
    print("Connection successful")
else:
    print("Unsucessful")
