import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\\Users\\AVICHAL TRIVEDI\\Documents\\College 2nd Year (Repositories)\\Machine Learning 4th semester\\Created or Used files (data)\\imdb (for R).xlsx")
categorical_cols = ['movie_title', 'content_rating']

df_cat = df[categorical_cols]
print(df_cat.head())

print("Unique values in each categorical column:")
print(df_cat.nunique())

print("Frequency of content ratings:")
print(df['content_rating'].value_counts())

print("Percentage distribution:")
print(df['content_rating'].value_counts(normalize=True) * 100)

# Bar Plot
df['content_rating'].value_counts().plot(kind='bar')

plt.title("Content Rating Distribution")
plt.xlabel("Rating Category")
plt.ylabel("Number of Movies")

plt.show()

# Grouping for avg
group = df.groupby('content_rating')['imdb_score'].mean()

print(group)