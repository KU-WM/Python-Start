from sklearn import datasets
import matplotlib.pyplot as plt

digit = datasets.load_digits()

plt.figure(figsize=(5, 5))
plt.imshow(digit.images[0], cmap=plt.cm.gray_r, interpolation='nearest')

plt.show()
print(digit.data[0])
print("이 숫자는", digit.target[0], "입니다.")