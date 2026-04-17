# Simple  Decision Tree Example

import pandas as pd

# Loading dataset
df = pd.read_excel("C:/Users/AVICHAL TRIVEDI/Documents/College 2nd Year (Repositories)/Machine Learning 4th semester/ESE-2/imdb.xlsx")

data = []

# Creating dataset in the format of nested list
for i in range(len(df)):
    duration = df.loc[i, "duration"]
    score = df.loc[i, "imdb_score"]

    if pd.isna(duration) or pd.isna(score):
        continue

    movie_length = duration          # in minutes
    rating_score = score * 10        # scale to 0–100

    if score >= 7:
        result = "Hit" 
    else:
        result = "Flop"

    data.append([movie_length, rating_score, result])

# Decision Tree Logic
def decision_tree(movie_length, rating_score):

    if movie_length >= 120:      # long movie
        if rating_score >= 70:
            return "Hit"
        else:
            return "Flop"
    else:
        return "Flop"

# Testing
print("Prediction:", decision_tree(130, 75))  # Expected Hit
print("Prediction:", decision_tree(90, 80))   # Likely Flop

# Plotting
import matplotlib.pyplot as plt

plt.scatter(df["duration"], df["imdb_score"])
plt.xlabel("Movie Length")
plt.ylabel("IMDb Score")
plt.axvline(x=120)   # your rule: length >= 120
plt.axhline(y=7)     # your rule: rating >= 7
plt.show()