import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="mahi123",auth_plugin='mysql_native_password',database='nlp')
print(mydb)
if(mydb):
    print("Connection successful")
else:
    print("Unsucessful")

mycursor = mydb.cursor()
#mycursor.execute("create database d2")

# sql_query="insert into nlp1(item,percentage,direction) values(%s,%s,%s)"
# detected =[("bottel","70","left"),("laptop","72","left"),("chair","66","right"),("mobile","78","front"),("table","74","back")]
# mycursor.executemany(sql_query,detected)
# mydb.commit()

#select from database
i=0
for i in range(5):
    sql_query="insert into nlp1 values(%s,%s,%s)"
    #detected =[("bottel","70","left"),("laptop","72","left"),("chair","66","right"),("mobile","78","front"),("table","74","back")]
    detected=('mobile',str(i),'left')
    #print(detected)
    mycursor.execute(sql_query,detected)
    mydb.commit()
mycursor.execute("select * from nlp1")

myresult = mycursor.fetchall()
for row in myresult:
    print(row)