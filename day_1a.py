import pandas as pd

df = pd.read_csv("input_1.txt",sep="\s+",header=None) 
for col in df:
    df[col] = df[col].sort_values(ignore_index=True)
df[2] = abs(df[0] - df[1])
print(df[2].sum())


