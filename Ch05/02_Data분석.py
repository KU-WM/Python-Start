import pandas as pd

s1 = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
s2 = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])

s3 = pd.Series([10, 20, 30, 40], name="S3")
s4 = pd.Series([10, 20, 30, 40], name="S4")

test = [["이름", "나이", "국어"],
        ["철수", 25, 87],
        ["영희", 23, 79]]

df = pd.DataFrame(test)
print(df.info())

# 큰수의 법칙 / 오캄의 면도날
# DataFrame에서 행이 많아야 한다 - 큰수의 법칙
# DataFrame에서 열이 너무 많으면 좋지 않다. - 오캄의 면도날