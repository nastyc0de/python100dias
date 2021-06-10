from os import cpu_count
from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    name = websiteInput.get()
    password = passwordInput.get()
    email = emailInput.get()
    
    if len(password) == 0 or len(email) == 0:
        empty_field = messagebox.askquestion(title=name, message='No dejes datos vacios')
    else:
        is_ok = messagebox.askokcancel(title=name, message=f'Estos son los datos \nEmail: {email} \nPassword: {password}')
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{name} | {email} | {password}\n')
                websiteInput.delete(0, END)
                passwordInput.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #
# ventana
window = Tk()
window.title('Password Generator')
window.minsize(300, 300)
window.config(padx=20, pady=20)
# logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
# labels
websiteLbl = Label(text='Website:')
websiteLbl.grid(column=0, row=1)
emailLbl = Label(text='Email/Username:')
emailLbl.grid(column=0, row=2)
passwordLbl = Label(text='password:')
passwordLbl.grid(column=0,row=3)
# inputs
websiteInput = Entry(width=35)
websiteInput.grid(column=1, row=1, columnspan=2)
websiteInput.focus()

emailInput = Entry(width=35)
emailInput.grid(column=1, row=2, columnspan=2)
emailInput.insert(0, 'password@gmail.com')

passwordInput = Entry(width=21)
passwordInput.grid(column=1,row=3)
# buttons
generateBtn = Button(text='Generate Password')
generateBtn.grid(column=2, row=3)
addBtn = Button(text='Add', width=36, command=get_data)
addBtn.grid(column=1, row=4, columnspan=2)

window.mainloop()