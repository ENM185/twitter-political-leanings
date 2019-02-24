import json
import os.path
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.model_selection import train_test_split

with open(os.path.dirname(__file__) + "/../dataset/data.json") as dataset_file:
    data = json.load(dataset_file)

x = np.array(data["Republicans"] + data["Democrats"])
y_train_list = []
for rep in data["Republicans"]:
    y_train_list.append([1,0])
for rep in data["Democrats"]:
    y_train_list.append([0,1])
y = np.array(y_train_list)


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

model = Sequential()

model.add(Dense(982, activation='relu'))
model.add(Dense(80, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=20, batch_size=1, verbose=1)

model.save('model.h5')
del(model)