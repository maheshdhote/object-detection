
# # importing the pyttsx library 
# import pyttsx3 
  
# # initialisation 
# engine = pyttsx3.init() 
  
# # testing 
# engine.say("My first code on text-to-speech") 
# engine.say("Thank you, Geeksforgeeks") 
# engine.runAndWait() 
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