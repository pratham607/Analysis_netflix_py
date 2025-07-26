import pandas as pd
import matplotlib.pyplot as plt

#reading the cleaned data

df=pd.read_csv("cleaned_netflix_titles.csv",encoding="latin1")
#print(df)

#creaating a subset
df=df.dropna(subset=["type","release_year","rating","country","duration"])


#Bar graph


type_count=df["type"].value_counts()
plt.bar(type_count.index,type_count.values,color=["blue","orange"])
plt.xlabel("Type of movies")
plt.ylabel("Count of movies")
plt.title("Number of movies VS TV shows")
plt.tight_layout()
plt.savefig("Movies  VS  TV shoes")
plt.show()


#pie chart


rate_count=df["rating"].value_counts()
plt.pie(rate_count,labels="Netflix ratings",autopct="%1.1f%%")
plt.title=("Netflix rating analysis")
plt.tight_layout()
plt.savefig("Ratings")
plt.show()

#Histogram


movies_count = df[df["type"] == "Movie"].copy()


movies_count["duration_int"] = movies_count["duration"].str.replace(" min", "", regex=False).astype(int)

plt.hist(movies_count["duration_int"], bins=30, color="orange", edgecolor="black")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
#plt.title("Movie Durations on Netflix")
plt.savefig("Duration")
plt.show()


#scater plot  df=df.dropna(subset=["type","release_year","rating","country","duration"])

relese_count=df["release_year"].value_counts().sort_index()
plt.scatter(relese_count.index,relese_count.values,color="pink")
plt.xlabel("Years")
plt.ylabel("Number of movies")
#plt.title("Number of movies relesed per year")
plt.tight_layout()
plt.savefig("Release per year")
plt.show()
