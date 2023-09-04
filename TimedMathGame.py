# IMPORTED LIBRARIES
import random
import time

# CONSTANTS
MIN_OPERAND = 3
MAX_OPERAND = 12
OPERATOR = ["+", "-", "*"]
TOTAL_QUESTIONS = 10

# FUNCTION TO GENERATE QUESTIONS
def generate_question():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)

    question = str(left) + operator + str(right)
    answer = eval(question)
    return question, answer

# WRONG COUNTER
wrong = 0 

# THE GAME
game_start = input("Press Enter to Start the Game!")
print("-------------------------")

time_start = time.time()

for i in range (TOTAL_QUESTIONS):
    question, answer = generate_question()
    while True:
        guess = input("Question #" + str(i + 1) + ":" + " " + question + " " + "=" + " ")
        if guess == str(answer):
            break
        wrong += 1

time_end = time.time()
time_taken = round(time_end - time_start, 2)

print("-------------------------")
print("Game Over!")
print("You took", time_taken, "seconds to complete the game!")






