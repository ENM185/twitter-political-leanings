import json
import os.path
import pandas as pd
import numpy as np
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, Embedding
from sklearn.model_selection import train_test_split
import pickle

csv_data = pd.read_csv(os.path.dirname(__file__) + '/../dataset/data.csv', sep=',', names = ['tweet', 'party'])
parties = csv_data['party'].map(lambda x: 1 if (x == "Republican") else 0)

tokenizer = Tokenizer(num_words = 20000)
tokenizer.fit_on_texts(csv_data['tweet'])
sequences = tokenizer.texts_to_sequences(csv_data['tweet'])
data = pad_sequences(sequences)

with open(os.path.dirname(__file__) + '/tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

X_train, X_test, y_train, y_test = train_test_split(data, parties, test_size=0.33, random_state=42)

model = Sequential()

model.add(Embedding(20000, 100, input_length=31))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


model.fit(X_train, y_train, epochs=10, batch_size=1, verbose=1)

score = model.evaluate(X_test, y_test)
print(score)

model.save('model.h5')
del(model)