import tkinter

window = tkinter.Tk()
window.title('app')
window.minsize(width=500, height=300)


# label
my_label = tkinter.Label(text='Es un label', font=('Arial', 24, 'bold'))
my_label.pack()
# my_label['text'] = 'Nuevo texto'
# my_label.config(text='cassas')

# button

def button_clicked():
    my_label.config(text=input.get())

button = tkinter.Button(text='Haz click', command=button_clicked)
button.pack()

# entry
input = tkinter.Entry()
input.pack()


window.mainloop()