# Simple Decision Tree Example

# Dataset: [Hours Studied, Attendance] -> Result

data = [
    [2, 60, "Fail"],
    [3, 65, "Fail"],
    [5, 75, "Pass"],
    [6, 80, "Pass"],
    [8, 90, "Pass"]
]

# Decision Tree Function
def decision_tree(hours, attendance):

    if hours >= 5:
        if attendance >= 70:
            return "Pass"
        else:
            return "Fail"
    else:
        return "Fail"


# Test Data
hours = 4
attendance = 70

result = decision_tree(hours, attendance)


print("Prediction:", result)

# Another Test
print(decision_tree(6, 80))