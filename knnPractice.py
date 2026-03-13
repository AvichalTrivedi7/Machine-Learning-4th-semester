import math

# Step 1: Dataset (Height, Weight) -> Label
data = [
    [150, 50, "Underweight"],
    [160, 60, "Normal"],
    [170, 70, "Normal"],
    [180, 90, "Overweight"],
    [175, 85, "Overweight"]
]

# Step 2: Euclidean Distance Function
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Step 3: KNN Function
def knn(new_point, k):

    distances = []

    # calculate distance from all points
    for point in data:
        dist = distance(new_point, point)
        distances.append((dist, point[2]))

    # sort by distance
    distances.sort()

    # take k nearest neighbors
    neighbors = distances[:k]

    # count labels
    votes = {}
    for d, label in neighbors:
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1

    # return label with highest vote
    return max(votes, key=votes.get)


# Step 4: Test data
new_person = [165, 65]

result = knn(new_person, 3)

print("Prediction:", result)