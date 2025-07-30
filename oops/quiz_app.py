# 🔹 OOP Review + Quiz App Project

# We'll build a console-based quiz app using:

# - Classes & Objects
# - Attributes & Methods
# - Input handling
# - Simple logic to track scores


# ✅ Step 1: Create a Question Class 

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Each object of this class will represent one quiz questions
# ✅ Step 2: Define the Questions 

questions = [
    Question("What is the capital of India?\n(a) Delhi\n(b) Mumbai\n(c) Kolkata\n", "a"),
    Question("Which language is known as the language of the web?\n(a) Python\n(b) JavaScript\n(c) C++\n", "b"),
    Question("What does OOP stand for?\n(a) Object Oriented Programming\n(b) Original Open Platform\n(c) Other Output Package\n", "a")
]

# ✅ Step 3: Create the Quiz Logic 

def run_quiz(questions):
    score = 0
    for each in questions:
        answer = input(each.prompt)
        if answer.lower() == each.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct!")


# ✅ Step 4: Run the App 

run_quiz(questions)
