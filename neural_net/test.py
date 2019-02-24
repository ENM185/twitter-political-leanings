import os.path
import keras
import json
import numpy as np
from keras.models import load_model

with open(os.path.dirname(__file__)+"/../common_words/words.json") as common_words_file:
    common_words = json.load(common_words_file)

model = load_model('model.h5')

text = "" #From a tweet
arr = [[]]

for common_word in common_words:
    if common_word in text.lower().split():
        arr[0].append(1)
    else:
        arr[0].append(0)

pred_arr = np.array(arr)

if sum(arr[0]) >= 5:
    pred = model.predict([pred_arr])
    if pred[0][0] > pred[0][1]:
        print("Republican")
    else:
        print("Democrat")
else:
    print("Not large enough")