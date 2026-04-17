# Simple Linear Regression (y = mx + b)

import pandas as pd

# Loading dataset
df = pd.read_excel("C:/Users/AVICHAL TRIVEDI/Documents/College 2nd Year (Repositories)/Machine Learning 4th semester/ESE-2/imdb.xlsx")

# Extracting columns
x = df["duration"].tolist()      # movie duration
y = df["imdb_score"].tolist()   # IMDb rating

n = len(x)
print("Amount of rows in dataset: ", n)

mean_x = sum(x) / n
mean_y = sum(y) / n

num = 0
den = 0

for i in range(n):
    num += (x[i] - mean_x) * (y[i] - mean_y)
    den += (x[i] - mean_x) ** 2

m = num / den
b = mean_y - m * mean_x

def predict(x_new):
    return m * x_new + b

# Example prediction
x_test = int(input("Please enter the duration (in minutes) of the movie you want to predict imdb Score of: "))   # 150 minutes movie
print("Predicted IMDb Score:", predict(x_test))

# Plotting
import matplotlib.pyplot as plt

plt.scatter(df["duration"], df["imdb_score"])
plt.xlabel("Movie Length")
plt.ylabel("IMDb Score")
plt.show()