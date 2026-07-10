import pandas as pd

df=pd.read_csv("netflix_titles.csv",encoding="latin1")

print(df.info())
print(df.isnull().sum())

df["director"]=df["director"].fillna("Unknown")
df["cast"]=df["cast"].fillna("Not Available")

print(df.isnull().sum())

df=df.drop_duplicates(subset=["show_id"])

df["date_added"]=pd.to_datetime(df["date_added"])

print(df.info())
df.to_csv("netflix_titles_cleaned.csv",index=False)