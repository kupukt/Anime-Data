import os 
import numpy as np
import pandas as pd
import collections
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting

print("What is the most watched genre of anime?")

df = pd.read_csv("CSV/anime.csv")

df= df.dropna()

# remove all 18+ anime
dfDropGenre = df.loc[df['genre'].str.contains("Hentai", case=True)].index

df = df.drop(dfDropGenre)

print(df)

for item in list(df['genre'].index):
    df.loc[item, 'genre'] = df.loc[item, "genre"] + ","
    
genre = []
for item in list(df['genre'].sum().split(",")):
    genre.append(item.strip())
    
counter = collections.Counter(genre)
genre_dict = dict(sorted(dict(counter).items(), key=lambda item: item[1], reverse = True))
del genre_dict[""]
df_genre = pd.Series(data = genre_dict)

print(df_genre)

'''l=[]

for i,idx in df.iterrows():
    p=[a for a in idx['genre'].strip().split(',')]
    l.extend(p)

genre_series = pd.Series(l)

genre_series.value_counts().plot.bar(figsize=(16,10))'''

df['rating'] = pd.to_numeric(df['rating'])

ratingdf = df.loc[df['rating'].nlargest(10).index]


print(ratingdf)










