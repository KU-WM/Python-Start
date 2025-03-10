import pandas as pd
import numpy as np

data = pd.read_csv('data/amazon.csv')
data.info()
print(data.isna().sum())
data.fillna("")
data = data.replace({"|": 0})
data['rating'] = data['rating'].astype(float)

data['rating_count'] = data['rating_count'].fillna('0')
data['rating_count'] = data['rating_count'].str.replace(",", "").astype('int32')

data = data[(data['rating'] >= 4.5)]

print(data.sort_values("rating_count", ascending=False)[:5])



# import pandas as pd
# import numpy as np

# data = pd.read_csv('c:/Users/human/ku-python/data/amazon.csv')
# data.fillna("")
# data = data.replace({"|": 0})
# data['rating'] = data['rating'].astype(float)

# data['rating_count'] = data['rating_count'].fillna('0')
# data['rating_count'] = data['rating_count'].str.replace(",", "").astype('int32')

# data = data[(data['rating'] >= 4.5)]

# data.sort_values("rating_count", ascending=False)[:5]
