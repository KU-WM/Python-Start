import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten, BatchNormalization, Conv2D
from keras.models import load_model
from keras.utils import to_categorical

import matplotlib.pyplot as plt
import random

# 데이터셋 받아오기
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

print(x_train.shape, x_test.shape)

# for i in range(1, 4 ,1):
#     for j in range(i, 4, 1):
#         plt.subplot(i, 4, j)
#         plt.imshow(x_train[random.randint(0, 60000)], cmap="gray")
#     plt.show()

# 리사이즈
# reshape(-1, 28, 28, 1)의 경우 기존 (60000, 28, 28)의 크기를 가진 3차원 데이터를
# (60000, 28, 28, 1)의 4차원 형식으로 변환해 줌 => 각 테이터를 28 * 28 * 1(픽셀의 채널값 / 흑백 1, RGB 3)로 변환
# reshape의 -1은 데이터가 들어오는 양(이 경우는 60000개의 데이터)을 개발자가 알 수 없음으로
# -1은 입력된 데이터 크기에 따라 자동으로 계산된 차원을 설정
x_train = x_train.reshape(-1, 28, 28, 1) / 255
x_test = x_test.reshape(-1, 28, 28, 1) / 255

# 정수형 레이블을 원-핫 인코딩으로 바꿔줌
# 원-핫 인코딩이란 간단히 0을 해당 레이블들의 정수의 최대치만큼 나열하고 
# 해당하는 부분만 1로 바꾸어 표시하는 방식
# ex)
# [1, 3, 2] => [[0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
# 레이블이 정수형이 아닌경우 LabelEncoder / StringLookup을 통하여 정수형으로 변환 후 학습
# lableEncoding.py 참고
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
# print(x_train[0], y_train[0], sep="\n-------------------------\n")

# 신경망 구축
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
