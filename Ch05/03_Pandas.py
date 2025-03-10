# quiz1.csv에서 Name, Age, Salary의 Column만 가져오기

import pandas as pd

data1 = pd.read_csv("C:/Users/human/ku-python/data/quiz1.csv", sep=";", usecols=["Name", "Age", "Salary"])
print(data1)
data2 = pd.read_csv("C:/Users/human/ku-python/data/quiz1.csv", sep=";", usecols=[1, 2, 3])
print(data2)
