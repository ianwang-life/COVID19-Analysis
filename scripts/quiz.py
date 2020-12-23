# Name of the Question.py file must match the name after from and import (including uppercase)
from Question import Question

question_prompts = [
    "When was the first version of Python 3 released?\n(a) 2005\n(b) 2007\n(c) 2008\n\n",
    "The Max OS X, originally released as Darwin, is based on what operating system?\n(a) Unix\n(b) BSD\n(c) Windows\n\n",
    "Linux is the only operating system that is _____.\n(a) Closed-source\n(b) Open-source\n\n"
]

q = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b")
]

def run_quiz(q):
    score = 0
    for question in q:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(q)) + " correct!")

run_quiz(q)
