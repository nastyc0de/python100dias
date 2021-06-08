import tkinter

window = tkinter.Tk()
window.title('app')
window.minsize(width=500, height=300)


def button_clicked():
    my_label.config(text=input.get())

# label
my_label = tkinter.Label(text='Es un label', font=('Arial', 24, 'bold'))
# my_label.pack()
my_label.grid(column=0, row=0)
# my_label['text'] = 'Nuevo texto'
# my_label.config(text='cassas')

# button

button = tkinter.Button(text='Haz click', command=button_clicked)
button.grid(column=1,row=1)

new_button = tkinter.Button(text='New Haz click', command=button_clicked)
new_button.grid(column=2, row=0)

# entry
input = tkinter.Entry()
input.grid(column=3, row=2)


window.mainloop()