import pandas as pd

df = pd.read_csv("input_1.txt",sep="\s+",header=None) 
similarity = 0 
counts = df[1].value_counts()
for v in df[0]:
    similarity+= v * counts.get(v, 0)
print(similarity)