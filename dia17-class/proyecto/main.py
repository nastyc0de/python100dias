from question_model import Question
from data import question_data
from quiz_model import QuizBrain

question_bank = []

for item  in question_data:
    question = Question(item['text'], item['answer'])
    question_bank.append(question)

quiz_1 = QuizBrain(question_bank)
while quiz_1.still_has_question(): 
    quiz_1.next_question()

print('Tu has terminado la encuesta')
print(f'Tu marcador final es: {quiz_1.score}/{quiz_1.question_number}')

