# 1000 ~ 1100행까지 필터링 후 SCORE_B >= 0.5

import pandas as pd

data = pd.read_csv("c:/Users/human/ku-python/data/pathogenicity_scores.csv")
data = data.iloc[1000: 1101][(data["SCORE_B"]) >= 0.5]

# 데이터의 길이 인덱싱이 차이가 있음으로 경고가 뜸 / 아래와 같이 경고 예방가능
# data = data.iloc[1000: 1101][(data.iloc[1000: 1101]["SCORE_B"]) >= 0.5]
print(data)
print(data.info())