# Simple Linear Regression (y = mx + b)

# Dataset: Hours studied -> Marks scored
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

n = len(x)

# Step 1: Calculate means
mean_x = sum(x) / n
mean_y = sum(y) / n

# Step 2: Calculate slope (m)
num = 0
den = 0

for i in range(n):
    num += (x[i] - mean_x) * (y[i] - mean_y)
    den += (x[i] - mean_x) ** 2

m = num / den

# Step 3: Calculate intercept (b)
b = mean_y - m * mean_x

# Step 4: Prediction
def predict(x_new):
    return m * x_new + b

# Test
x_test = 6
print("Prediction:", predict(x_test))