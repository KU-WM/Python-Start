import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, BatchNormalization, Conv2D
from tensorflow.keras.models import load_model
import numpy as np 

import matplotlib.pyplot as plt
import random

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

model2 = load_model('mnist_test.h5')


x_train = x_train.reshape(-1, 28, 28, 1) / 255.
x_test = x_test.reshape(-1, 28, 28, 1) / 255.
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

predict = model2.predict(x_test)

loss = 0
for i in range(0, 10000 ,1):
    if np.argmax(y_test[i]) != np.argmax(predict[i]):
        print("Actual : {}\tPredict : {}".format(np.argmax(y_test[i]), np.argmax(predict[i])),)
        loss += 1

print("loss : ", loss)