import nltk
from nltk.stem.lancaster import LancasterStemmer
Stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json

with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs = []
 
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wods = nltk.word_tokenize(pattern)
        words.extend(wods)
        docs.append[pattern]

    if intent["tag"] not in labels:
        labels.append(intent["tag"])