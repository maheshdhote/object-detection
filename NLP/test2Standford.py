import stanfordnlp
extract=[]
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English
doc = nlp("where is bed")
doc.sentences[0].print_dependencies()
for sent in doc.sentences:
     for word in sent.words:
         if( word.dependency_relation=='obj' or word.dependency_relation=='nsubj' or word.dependency_relation=='amod'): #word.dependency_relation=='obl' or
             extract.append(word.text)
        
print(extract)         
from itertools import chain
from nltk.corpus import wordnet
list_of_words=list()
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



import pyttsx3 
engine = pyttsx3.init() 
 

mycursor = mydb.cursor()
mycursor.execute("select item,direction from nlp1")
myresult = mycursor.fetchall()
detected=list()
for row in myresult:
    detected.append(row)
print(detected)
for i in detected:
    if any(i[0] in s for s in list_of_words):
        print("Yes") 
        engine.say(i[0]+" is on your "+i[1]+"side") 
        engine.runAndWait() 
    else:
        #print("no")









#print(*[f'text: {word.text+" "}Dependency: {word.dependency_relation}' for sent in doc.sentences for word in sent.words], sep='\n')
# for i in doc.sentences[0].dependencies:
#     if(i!=None):
#         for word in i:
#             # print("1"+str(j))
#             print(*[f'text: {word.text+" "}\tlemma: {word.lemma}\dependency: {word.dependency_relation}'])
# print(*[f'text: {word.text+" "}\tlemma: {word.lemma}\tupos: {word.upos}\txpos: {word.xpos}' for sent in doc.sentences for word in sent.words], sep='\n')
