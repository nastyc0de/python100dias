from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

# window
window = Tk()
window.title('Flash Card')
window.minsize(width=900, height=650)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# canvas
canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front)

canvas.create_text(400, 150, text='Title',font=('Arial', 40, 'italic'))
canvas.create_text(400, 263, text='Word',font=('Arial', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR ,highlightthickness=0ce)

canvas.grid(row=0, column=0, columnspan=2)
# buttons
ok_img = PhotoImage(file='./images/right.png')
okBtn = Button(image=ok_img, highlightthickness=0,border=0)
okBtn.grid(row=1, column=0)

wrong_img = PhotoImage(file='./images/wrong.png')
wrongBtn = Button(image=wrong_img, highlightthickness=0, border=0)
wrongBtn.grid(row=1, column=1)

# labels
# title = Label(text='Title',bg='white',fg='black',font=('Arial', 40, 'italic'))
# title.place(x=400, y=150)
# title.grid(row=0,column=0,columnspan=2)
# word = Label(text='Word',bg='white',fg='black',font=('Arial', 60, 'bold'))
# word.place(x=400, y=263)
# word.grid(row=0,column=0,columnspan=2)
window.mainloop()
