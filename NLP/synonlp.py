# from nltk.corpus import wordnet

# syns = wordnet.synsets("chair")
# print(syns)


# import nltk 
# from nltk.corpus import wordnet 
# synonyms = [] 
# antonyms = [] 
  
# for syn in wordnet.synsets("bottle"): 
#     for l in syn.lemmas(): 
#         synonyms.append(l.name()) 
#         if l.antonyms(): 
#             antonyms.append(l.antonyms()[0].name()) 
  
# print(set(synonyms)) 
# #print(set(antonyms)) 


# from itertools import chain
# from nltk.corpus import wordnet

# synonyms = wordnet.synsets('computer')
# lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
# print(lemmas)
y="L1"
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
    z="F:\\JupyterNotebook\\Object Detection 2\\input\\"
    input_path = (z+y+".jpeg")
    print(input_path)
    
