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
try:
    print("Downloading Images from firebase ....")
    storage.child("Images/L1.jpeg").download("input/L1.jpeg")
    storage.child("Images/L2.jpeg").download("input/L2.jpeg")

    storage.child("Images/R1.jpeg").download("input/R1.jpeg")
    storage.child("Images/R2.jpeg").download("input/R2.jpeg")

    storage.child("Images/F1.jpeg").download("input/F1.jpeg")
    storage.child("Images/F2.jpeg").download("input/F2.jpeg")

    storage.child("Images/B1.jpeg").download("input/B1.jpeg")
    storage.child("Images/B2.jpeg").download("input/B2.jpeg")
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
y=""
for i in range(1,9):
    if(i<3):
        if(i%2==0):
            y="L2"
        else:
            y="L1"
    if(i>2 and i<5):
        if(i%2==0):
            y="F2"
        else:
            y="F1"
    if(i>4 and i<7):
        if(i%2==0):
            y="R2"
        else:
            y="R1"
    if(i>6 and i<9):
        if(i%2==0):
            y="B2"
        else:
            y="B1"
    input_path = ('F:\\JupyterNotebook\\Object Detection 2\\input\\'+y+'.jpeg')
    output_path = ('F:\\JupyterNotebook\\Object Detection 2\\output\\'+y+'.jpeg')
    print(input_path)
    print(output_path)
    detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
    for eachItem in detection:
        print(eachItem["name"] , " : ", eachItem["percentage_probability"])	
        sql_query="insert into nlp1(item,percentage,direction) values(%s,%s,%s)"
        #detected =[("bottel","70","left"),("laptop","72","left"),("chair","66","right"),("mobile","78","front"),("table","74","back")]
        detected=(eachItem["name"],eachItem["percentage_probability"],y)
        print(detected)
        mycursor.execute(sql_query,detected)
        mydb.commit()
mycursor.execute("select * from nlp1")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)



# NLP
import stanfordnlp
extract=[]
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English
print("getting query")
#get Query from realtime firebase
from firebase import firebase
firebase = firebase.FirebaseApplication("https://thirdeye-3ec17.firebaseio.com/",None)
result2 = firebase.get('https://thirdeye-3ec17.firebaseio.com/SptoTx','')

print(result2)
doc = nlp(result2)
doc.sentences[0].print_dependencies()
for sent in doc.sentences:
     for word in sent.words:
         if( word.dependency_relation=='obj' or word.dependency_relation=='nsubj' or word.dependency_relation=='amod'): #word.dependency_relation=='obl' or
             extract.append(word.text)
        
print(extract)         
from itertools import chain
from nltk.corpus import wordnet
list_of_words=[]
for i in extract:
    synonyms = wordnet.synsets(i)
    lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    #print(lemmas)
    list_of_words.append(lemmas)
print(list_of_words)

import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="mahi123",auth_plugin='mysql_native_password',database='nlp')
print(mydb)
if(mydb):
    print("Connection successful")
else:
    print("Unsucessful")





#Uploadin to Fiberbase

import pyttsx3 
engine = pyttsx3.init() 
mycursor = mydb.cursor()
mycursor.execute("select item,direction from nlp1")
myresult = mycursor.fetchall()
detected=[]
for row in myresult:
    detected.append(row)
print(detected)
for i in detected:
    if any(i[0] in s for s in list_of_words):
        print("Yes "+i[0]+" is on your "+i[1]+" side") 
        firebase.put('','TxtoSp',i[0]+" is on your "+i[1]+" side")
        print('updated')
        engine.say(i[0]+" is on your "+i[1]+"side") 
        engine.runAndWait() 
        break
    else:
        print("Sorry...")