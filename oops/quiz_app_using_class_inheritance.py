# 🔹 Plan
# We will create a base class Quiz and child class TimedQuiz.
# Quiz class → Handles normal quiz logic.
# TimedQuiz class → Inherits from Quiz and adds a timer feature.

# What is super()?
# super() is used inside a child class to access methods/attributes of the parent class.
# It is commonly used to call the parent constructor (__init__).
#3️⃣ What is Method Overriding?-Overriding means the child class writes its own version of a parent method, replacing the parent one.
import random
import time

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz: # Quiz class → Handles normal quiz logic.
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    def run(self):
        for q in self.questions:
            ans = input(q.prompt)
            if ans.lower() == q.answer:
                self.score += 1
        print(f"Score: {self.score}/{len(self.questions)}")

# ✅ Child class adds timer
class TimedQuiz(Quiz): 
    def __init__(self, questions, time_limit):
        super().__init__(questions)#We use super().__init__(questions) to call parent constructor.
        self.time_limit = time_limit

# ✅ Child class adds timer
class TimedQuiz(Quiz):
    def __init__(self, questions, time_limit):
        super().__init__(questions)#We use super().__init__(questions) to call parent constructor.
        self.time_limit = time_limit

    def run(self):
            for q in self.questions:
                print(q.prompt)
                start = time.time()
                ans = input("Your answer: ")
                end = time.time()

                if end - start > self.time_limit:
                    print("⏳ Time Over!")
                    continue
                if ans.lower() == q.answer:
                    self.score += 1
            print(f"Score: {self.score}/{len(self.questions)}")

# ✅ Using the child class
questions = [
    Question("Capital of India?\n(a) Delhi\n(b) Mumbai\n(c) Kolkata\n", "a"),
    Question("Language of the web?\n(a) Python\n(b) JavaScript\n(c) C++\n", "b")
]

quiz = TimedQuiz(questions, 10)  # 10 sec per question
quiz.run()