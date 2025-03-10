import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/human/ku-python/data/HM_all_stores.csv")

# NaN값 제거
# data.dropna(how='any', inplace=True)
# print(data)
# print(data.info())

# 선형보간
data.interpolate(inplace=True)
data.replace({np.nan: ""}, inplace=True)
print(data.isna().sum())
print(data.info())
