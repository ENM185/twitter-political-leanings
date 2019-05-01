import os.path
import keras
import json
import numpy as np
from keras.models import load_model
import pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import re

with open(os.path.dirname(__file__) + '/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = load_model('model.h5')

def clean(text) :
    text = text.lower()
    text = re.sub(r"[^A-Za-z0-9^!./'=\s]", "", text)
    return text

text = [clean("")] #From a tweet

sequence = tokenizer.texts_to_sequences(text)
input = pad_sequences(sequence, maxlen=31)

pred = model.predict(input)[0][0]

if pred > .5 :
    print(str(pred*100) + "% Republican")
else:
    print(str((1-pred)*100) + "% Democrat")