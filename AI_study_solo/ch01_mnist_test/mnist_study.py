import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, BatchNormalization, Conv2D
from tensorflow.keras.models import load_model

import matplotlib.pyplot as plt
import random

import os

os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

# 데이터셋 받아오기
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

print(x_train.shape, x_test.shape)

# for i in range(1, 4 ,1):
#     for j in range(i, 4, 1):
#         plt.subplot(i, 4, j)
#         plt.imshow(x_train[random.randint(0, 60000)], cmap="gray")
#     plt.show()

# 리사이즈?
x_train = x_train.reshape(-1, 28, 28, 1) / 255
x_test = x_test.reshape(-1, 28, 28, 1) / 255
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print(x_train[0], y_train[0], sep="\n-------------------------\n")

# 신경망 구축? / 각 함수 동작방식 모름
model = Sequential()
model.add(Conv2D(32, (2, 2), activation="relu", input_shape=(28, 28, 1)))
model.add(BatchNormalization())

model.add(Conv2D(64, (2, 2), activation="relu"))
model.add(BatchNormalization())

model.add(Conv2D(128, (2, 2), 2, activation="relu"))
model.add(BatchNormalization())

model.add(Conv2D(32, (2, 2), activation="relu"))
model.add(BatchNormalization())

model.add(Conv2D(64, (2, 2), activation="relu"))
model.add(BatchNormalization())

model.add(Conv2D(128, (2, 2), 2, activation="relu"))
model.add(BatchNormalization())
model.add(Flatten())

model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))

model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics=["acc"])
history = model.fit(x_train, y_train, validation_data = (x_test, y_test), epochs = 30, batch_size = 256)

model.save("mnist_test.h5")
