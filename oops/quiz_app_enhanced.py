
# 🔁 Optional Enhancements (Try these later): 

# - Shuffle the questions
# - Add difficulty levels
# - Track high scores
# - Timer for each question
# - Save results to a file


import random
import time

class Question:
    def __init__(self, prompt, answer, difficulty):
        self.prompt = prompt
        self.answer = answer
        self.difficulty = difficulty

questions = [
    Question("What is the capital of India?\n(a) Delhi\n(b) Mumbai\n(c) Kolkata\n", "a", "Easy"),
    Question("Which language is known as the language of the web?\n(a) Python\n(b) JavaScript\n(c) C++\n", "b", "Medium"),
    Question("What does OOP stand for?\n(a) Object Oriented Programming\n(b) Original Open Platform\n(c) Other Output Package\n", "a", "Hard")
]

high_score = 0

def save_score(score):
    with open("quiz_scores.txt", "a") as file:
        file.write(f"Score: {score}/{len(questions)}\n")

def run_quiz(questions):
    global high_score
    score = 0
    random.shuffle(questions)  # Shuffle questions

    for each in questions:
        print(f"\nDifficulty: {each.difficulty}")
        print(each.prompt)

        start = time.time()
        answer = input("Your answer: ")
        end = time.time()

        if end - start > 10:
            print("⏳ Time Over!")
            continue

        if answer.lower() == each.answer:
            score += 1

    print(f"\n✅ You got {score}/{len(questions)} correct!")

    if score > high_score:
        high_score = score
        print("🎉 New High Score!")

    save_score(score)

while True:
    run_quiz(questions)
    again = input("\nPlay again? (y/n): ")
    if again.lower() != "y":
        break
