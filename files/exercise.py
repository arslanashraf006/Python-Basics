#poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.

from collections import Counter
import string

# Step 1: Read the file
with open("C:\\Users\\REGEN\\Documents\\python basics\\files\\poem.txt", "r") as file:
    text = file.read()

# Step 2: Preprocess text - lowercasing and removing punctuation
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))

# Step 3: Split into words
words = text.split()

# Step 4: Count word occurrences
word_counts = Counter(words)

# Step 5: Find the maximum occurrence
max_count = max(word_counts.values())

# Step 6: Find all words with the maximum count
most_common_words = [word for word, count in word_counts.items() if count == max_count]

# Output result
print(f"Most frequent word(s): {most_common_words}")
print(f"Occurrence count: {max_count}")
