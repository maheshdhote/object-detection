#image segmentation

import os
import cv2
from tensorflow.keras import backend
import pyrebase

firebaseConfig = {
  
  "apiKey": "AIzaSyBJ2GIuBXhF7qjWfrHqXZ_guYlkj5TQhRg",
  "authDomain": "thirdeye-3ec17.firebaseapp.com",
  "databaseURL": "https://thirdeye-3ec17.firebaseio.com",
  "projectId": "thirdeye-3ec17",
  "storageBucket": "thirdeye-3ec17.appspot.com",
  "messagingSenderId": "681490047688",
  "appId": "1:681490047688:web:70f00fac7172cdfa33bbfd"
}



firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
for i in range(15):
    try:
        print(str(i)+".jpeg")
        storage.child(str(i)+".jpeg").download("input/"+str(i)+".jpeg")
    except:
        pass



# Database

import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="mahi123",auth_plugin='mysql_native_password',database='nlp')
print(mydb)
if(mydb):
    print("Connection successful")
else:
    print("Unsucessful")

mycursor = mydb.cursor()




import numpy as np


#object detection

from imageai.Detection import ObjectDetection

detector = ObjectDetection()

model_path = (r'F:\JupyterNotebook\Object Detection 2\models\resnet50_coco_best_v2.0.1.h5')



detector.setModelTypeAsRetinaNet()
detector.setModelPath(model_path)
detector.loadModel()
list = os.listdir('./input/') # dir is your directory path
number_files = len(list)
mycursor.execute("truncate nlp1")
for i in range(1,number_files):
        input_path = (r'F:\JupyterNotebook\Object Detection 2\input\frame'+str(i)+'.jpg')
        output_path = (r'F:\JupyterNotebook\Object Detection 2\output\newimage'+str(i)+'.jpg')
        print(input_path)
        print(output_path)
        detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
        for eachItem in detection:
            print(eachItem["name"] , " : ", eachItem["percentage_probability"])	
            sql_query="insert into nlp1(item,percentage,direction) values(%s,%s,%s)"
            #detected =[("bottel","70","left"),("laptop","72","left"),("chair","66","right"),("mobile","78","front"),("table","74","back")]
            detected=(eachItem["name"],eachItem["percentage_probability"],"left")
            print(detected)
            mycursor.execute(sql_query,detected)
            mydb.commit()
mycursor.execute("select * from nlp1")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)