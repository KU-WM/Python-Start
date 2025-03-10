import pandas as pd

print(pd.__version__)

s1 = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
s2 = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])

s3 = pd.Series([10, 20, 30, 40], name="S3")
s4 = pd.Series([10, 20, 30, 40], name="S4")

x1 = [1, 2, 3, 4]
x2 = [1, 2, 3, 4]

# 리스트의 경우 +연산시 append로 처리가 된다.
print(x1 + x2)

print(s1)

# Series의 경우 +를 하면 백터 연산을 진행하여 같은 인덱스를 가진 데이터끼리 더한다.
# 일치하는 인덱스가 없는경우 NaN이 뜨며 연산이 되지 않는다.
print(s1 + s2)

# series를 합치는 경우 DataFrame을 이용한다.
df = pd.DataFrame({'Column1': s1, 'Column2': s2})
print(df)

pd.concat([s3, s4], axis=0)