from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window =Tk()
        self.window.title('Quizzier')
        self.window.config(bg= THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.quest = self.canvas.create_text(150, 125, width=280, text='question', fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score = Label(text='Score: 0', fg='white',bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        true_img = PhotoImage(file='./images/true.png')
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.press_true)
        self.true_btn.grid(row=2,column=0)

        wrong_img = PhotoImage(file='./images/false.png')
        self.wrong_btn = Button(image=wrong_img, highlightthickness=0, command=self.press_wrong)
        self.wrong_btn.grid(row=2,column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():

            self.score.config(text=f'Score: {self.quiz.score}')
            quest_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quest, text=quest_text)
        else:
            self.canvas.itemconfig(self.quest, text='Llegaste al limite')
            self.true_btn.config(state='disabled')
            self.wrong_btn.config(state='disabled')

    def press_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def press_wrong(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)