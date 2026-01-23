with open("story.txt", "r") as f:
    story = f.read()

target_sym_start = "<"
target_sym_end = ">"

start = -1
words = set()

# Find all placeholders
for i, char in enumerate(story):
    if char == target_sym_start:
        start = i
    elif char == target_sym_end and start != -1:
        word = story[start:i+1]
        words.add(word)
        start = -1

answers = {}

# Ask user for replacements
for word in words:
    user_word = input(f"Enter a replacement for {word}: ")
    answers[word] = user_word

# Replace placeholders
for word in words:
    story = story.replace(word, answers[word])

print("\n📖 Your final story:\n")
print(story)
