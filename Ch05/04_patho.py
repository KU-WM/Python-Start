import pandas as pd

data = pd.read_csv("c:/Users/human/ku-python/data/pathogenicity_scores.csv", usecols=["Patient_ID", "Mutation_ID", "SCORE_A"])
data = data[(data["SCORE_A"]) >= 0.5]
# data[["Patient_ID", "Mutation_ID", "SCORE_A"]][(data["SCORE_A"]) >= 0.5]
print(data)