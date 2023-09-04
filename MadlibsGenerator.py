# Madlibs generator by akmalznal
# Taught and inspired by Tech With Tim on YouTube

# OPENING TEXT FILE
with open("story.txt", "r") as f:
    story = f.read()

# SEARCH EMPTY WORDS
start = "<"
end = ">"
start_of_word = -1

words = set()

for i, char in enumerate(story):
    if char == start:
        start_of_word = i

    if char == end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

# REPLACE WORDS IN WORDS LIST
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

# REPLACE WORDS IN STORY
for word in words:
    story = story.replace(word, answers[word])

print(story)








