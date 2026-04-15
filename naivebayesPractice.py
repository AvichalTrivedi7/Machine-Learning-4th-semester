# Simple Naive Bayes (Spam Detection)

# Training data
data = [
    ("Win money now", "Spam"),
    ("Limited offer win cash", "Spam"),
    ("Meeting at 5pm", "Not Spam"),
    ("Project discussion tomorrow", "Not Spam")
]

# Step 1: Count words per class
word_counts = {"Spam": {}, "Not Spam": {}}
class_counts = {"Spam": 0, "Not Spam": 0}

for text, label in data:
    class_counts[label] += 1
    words = text.lower().split()
    
    for word in words:
        if word not in word_counts[label]:
            word_counts[label][word] = 0
        word_counts[label][word] += 1

# Step 2: Prediction function
def predict(text):
    words = text.lower().split()
    scores = {}

    for label in class_counts:
        # Start with prior probability
        score = class_counts[label] / sum(class_counts.values())

        for word in words:
            word_freq = word_counts[label].get(word, 0) + 1  # Laplace smoothing
            total_words = sum(word_counts[label].values()) + len(word_counts[label])
            
            score *= word_freq / total_words

        scores[label] = score

    return max(scores, key=scores.get)

# Test
print(predict("win cash now"))
