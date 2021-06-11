from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window =Tk()
        self.window.title('Quizzier')
        self.window.config(width=300, height=700, bg=           THEME_COLOR, padx=20)
        self.canvas = Canvas(width=300, height=250,bg='white')
        self.canvas.create_text(text='question')
        self.canvas.grid(column=0,row=1)

        self.window.mainloop()
