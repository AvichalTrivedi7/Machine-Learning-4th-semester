import random
import math

# Dataset (2D points)
data = [
    [1, 2], [2, 3], [3, 4],
    [8, 8], [9, 10], [10, 9]
]

# Distance function
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# K-Means function
def kmeans(data, k, iterations=5):
    
    # Step 1: Random centroids
    centroids = random.sample(data, k)

    for _ in range(iterations):
        clusters = [[] for _ in range(k)]

        # Step 2: Assign points to nearest centroid
        for point in data:
            distances = [distance(point, c) for c in centroids]
            min_index = distances.index(min(distances))
            clusters[min_index].append(point)

        # Step 3: Update centroids
        new_centroids = []
        for cluster in clusters:
            if cluster:
                x_mean = sum(p[0] for p in cluster) / len(cluster)
                y_mean = sum(p[1] for p in cluster) / len(cluster)
                new_centroids.append([x_mean, y_mean])
            else:
                new_centroids.append(random.choice(data))

        centroids = new_centroids

    return clusters

# Run
clusters = kmeans(data, k=2)

print("Clusters:", clusters)
