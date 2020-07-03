import json
import random
import tensorflow
import tflearn
import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


with open('intents.json') as file:
    data = json.load(file)

print(data['intents'])
#date 03-july-2020
#Tensorflow error has been resolved by VC 2015, 2017(one installation setup in d/apps) distribution installation 
# Worked till here but need to solve some unknown erorrs might be arising because of system configuration


# words = []
# labels = []
# docs_x = []
# docs_y = []

# for intent in data['intents']:
#     for pattern in intent['patterns']:
#         wrds = nltk.word_tokenize(pattern)
#         words.extend(wrds)
#         docs_x.append(wrds)
#         docs_y.append(intent["tag"])

#     if intent['tag'] not in labels:
#         labels.append(intent['tag'])
