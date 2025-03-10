import pandas as pd
data = pd.read_csv("C:/Users/human/ku-python/data/treatment.csv")

# data.info()
# data.head(3)
# data.describe()

tidy = data.melt(id_vars="name", var_name="treatment", value_name="result")

print(tidy)

tidy = tidy.replace({'treatment': {'treatmenta': 'a', 'treatmentb': 'b'}})
print(tidy)
