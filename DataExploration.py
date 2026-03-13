import pandas as pd

df = pd.read_excel(r"C:\\Users\\AVICHAL TRIVEDI\Documents\\College 2nd Year (Repositories)\\Machine Learning 4th semester\\Created or Used files (data)\\imdb (for R).xlsx")
df['ID'] = df.index + 1
print(df)


column_names = ['ID','director_id','country_id','title_year','imdb_score', 'gross', 'duration']
df_numeric = df[column_names]
print(df_numeric)
# can also use df_numeric = pd.read_excel(r"path", usecols=column_names)


print("describe() gives statistical values like count, mean, std, min, max, quartiles")
print(df_numeric.describe()) 

print("info() gives basic info about class, range, total columns, datatype, constraints, memory usage")
print(df_numeric.info())  

print("head - top 5 elements")
print(df_numeric.head(5)) 

print("tail - bottom 5 elements")
print(df_numeric.tail(5)) 

print("duplicate gives duplicate rows")
print(df_numeric.duplicated().sum())

print("isnull and sum together give total missing per column")
print(df_numeric.isnull().sum()) 

print("isnull and mean - percentage missing")
print(df_numeric.isnull().mean()*100) # percentage missing

print("useful for understanding categorical variables")
print(df[["movie_title"]].nunique()) # Useful for understanding categorical variables.


print("Correlation Heatmap (using seaborn)")

import seaborn as sns
import matplotlib.pyplot as plt
corr_matrix = df_numeric.corr()
print(corr_matrix)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()


print("Pairwise Scatterplot Matrix (numeric columns)")
sns.pairplot(df_numeric)
plt.show()


print("Boxplots for Outlier Visualization")
df_numeric.boxplot(figsize=(10,5))
plt.show()


print("Histograms for Distribution")
df_numeric.hist(figsize=(10, 6), bins=20)
plt.show()


print("Grouping to Check trends or summaries across categories.")
df.groupby('director_id')['gross'].sum().sort_values(ascending=False)


print("Skewness and Kurtosis") 
print(df_numeric.skew())
print(df_numeric.kurt())


print("pivoting table")
result = df_numeric.pivot(index='ID', columns='director_id', values='imdb_score')
print(result)


print("sorting values")
sorte = df_numeric.sort_values(['imdb_score'], ascending=[True])
print(sorte)


print("using groupby")
test = df_numeric.groupby(['director_id', 'imdb_score'])
print(test.size())


print("dropping duplicates")
dupli_less = df_numeric.drop_duplicates(['director_id', 'imdb_score'])
print(dupli_less)


print("fill null values with 1234")
mvalue = df_numeric.fillna(1234)
print(mvalue)
