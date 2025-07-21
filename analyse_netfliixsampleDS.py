import pandas  as pd
df=pd.read_csv("netflix_titles.csv",encoding="latin1")
df.info()
print(df)
df=df.dropna(axis=1,how="all")
print(df)
df.to_csv("cleaned_netflix_titles.csv",index=False)
#clened data 
#oprations
import pandas as pd
df=pd.read_csv("cleaned_netflix_titles.csv",encoding="utf8")
print(df)
df.info
type_data1=df[df["type"]=="Movies"]
print(type_data1)
type_data2=df[df["type"]=="TV Show"]
print(type_data2)
print(df.iloc[:,7])
data_09=df[df["release_year"]==2009]
print(data_09)
data_10=df[df["release_year"]==2010]
print(data_10)
data_11=df[df["release_year"]==2011]
print(data_11)
data_12=df[df["release_year"]==2012]
print(data_12)
data_13=df[df["release_year"]==2013]
print(data_13)
data_14=df[df["release_year"]==2014]
print(data_14)
data_15=df[df["release_year"]==2015]
print(data_15)
data_16=df[df["release_year"]==2016]
print(data_16)
data_17=df[df["release_year"]==2017]
print(data_17)
data_18=df[df["release_year"]==2018]
print(data_18)
data_19=df[df["release_year"]==2019]
print(data_19)
data_20=df[df["release_year"]==2020]
print(data_20)
data_21=df[df["release_year"]==2021]
print(data_21)
print(df["country"])
info=df[df["country"]=="India"]
print(info)
import pandas as pd
import numpy as np
df=pd.read_csv("cleaned_netflix_titles.csv",encoding="latin1")
print(df)
print(df["duration"].unique())
df["duration_num"]=df["duration"].str.extract('(\d+)').astype(float)
mean_duration=np.mean(df["duration_num"])
print(mean_duration)