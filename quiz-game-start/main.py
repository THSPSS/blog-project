from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text = question["question"] #"queston" : Value about question"
    question_answer = question["correct_answer"] #"answer : Value about answer"
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


quiz_brain = QuizBrain(question_bank)


while quiz_brain.stll_has_question():
      quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score was : {quiz_brain.score}/{quiz_brain.question_number}")



