from tkinter import *
from numpy import flip
import pandas as pd
import random

from pandas.core.frame import DataFrame
BACKGROUND_COLOR = "#B1DDC6"
value_dict = {}
dict_data = {}
# funciones
try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    org_data = pd.read_csv('./data/french_words.csv')
    dict_data = DataFrame.to_dict(org_data, orient='records')
else:
    dict_data = DataFrame.to_dict(data, orient='records')


def generate_word():
    global value_dict, flip
    window.after_cancel(flip)
    value_dict = random.choice(dict_data)
    value = value_dict['French']
  
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(lang, text=value, fill='black')
    flip = window.after(3000, func=flip_card)

def flip_card():
    value = value_dict['English']
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(lang, text=value, fill='white')
    canvas.itemconfig(card, image=card_back)

def is_known():
    dict_data.remove(value_dict)
    data = pd.DataFrame(dict_data)
    data.to_csv('./data/words_to_learn.csv', index=False)
    generate_word() 

# window
window = Tk()
window.title('Flash Card')
window.minsize(width=900, height=650)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip = window.after(3000, func=flip_card)
# canvas
canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
card = canvas.create_image(400, 263, image=card_front)

title = canvas.create_text(400, 150, text='', fill='black', font=('Arial', 40, 'italic'))
lang = canvas.create_text(400, 263, text='',fill='black', font=('Arial', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR ,highlightthickness=0)

canvas.grid(row=0, column=0, columnspan=2)
# window.after(3000,canvas.itemconfig(card, image=card_back))
# buttons
ok_img = PhotoImage(file='./images/right.png')
okBtn = Button(image=ok_img, highlightthickness=0,border=0, command=is_known)
okBtn.grid(row=1, column=0)

wrong_img = PhotoImage(file='./images/wrong.png')
wrongBtn = Button(image=wrong_img, highlightthickness=0, border=0, command=generate_word)
wrongBtn.grid(row=1, column=1)


generate_word()

window.mainloop()
