# 컬럼의 데이터타입을 적정한 형태로 변환시키기
# country를 기준으로 그룹화하고, 매장 개수가 몇개가 있는지 확인 (storeCode)

import pandas as pd
import numpy as np

data = pd.read_csv("data/HM_all_stores.csv")
data.info()
print(data.head(10))

dt = data.melt()
dt['day_of_week'] = dt['day_of_week'].astype('category')
dt['opening_hours'] = dt['opening_hours'].astype('category')
dt['longitude'] = dt['longitude'].astype('float32')
dt['latitude'] = dt['latitude'].astype('float32')
data.interpolate(inplace=True)
data.fillna('', inplace=True)

print(data.isna().sum())

filtered_data = data.pivot_table(index='country', values='storeCode', aggfunc='count')
print(filtered_data)