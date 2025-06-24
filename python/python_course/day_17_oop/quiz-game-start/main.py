from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create question bank
question_bank = []
for question in question_data:
    q = question['text']
    a = question['answer']
    mew_question = Question(q, a)
    question_bank.append(mew_question)


quiz = QuizBrain(q_list=question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print("Quiz complete!")
print(f"Final score:{quiz.score}/{len(question_bank)}")