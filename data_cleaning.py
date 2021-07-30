import pandas as pd 
import csv 

df = pd.read_csv("bright_stars_data.csv")
del df["Luminosity"]
df.to_csv("main.csv")

print(df.shape)
print(list(df))