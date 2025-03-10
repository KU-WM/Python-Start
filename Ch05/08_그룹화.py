import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/human/ku-python/data/pathogenicity_scores.csv")
data.info()
print("============================================")
print(data[data['Mutation_ID'] >= 12000][data['Mutation_ID'] < 12011])
print("============================================")
print(data[data['Mutation_ID'] >= 12000][data['Mutation_ID'] < 12011].groupby('Patient_ID')['SCORE_A'].mean())


