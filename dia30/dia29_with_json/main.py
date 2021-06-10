from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter = [choice(letters) for _ in range(randint(8, 10))]
    number = [choice(numbers) for _ in range(randint(2, 4))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]
    

    password_list = letter+ number + symbol
    shuffle(password_list)
    password = ''.join(password_list)
    passwordInput.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    name = websiteInput.get()
    password = passwordInput.get()
    email = emailInput.get()
    new_data = {
        name:{
            'email':email,
            'password':password

        }
    }
    if len(password) == 0 or len(name) == 0:
        messagebox.askquestion(title=name, message='No dejes datos vacios')
    else:
        try:
            with open('data.json', 'r') as data_file:
                # leyendo los datos (antiguos)
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # guardando los datos actualizados
                json.dump(new_data, data_file, indent=4)
        else:
                # actualizar los datos antiguos con el nuevo dato
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # guardando los datos actualizados
                json.dump(data, data_file, indent=4)
        finally:    
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
generateBtn = Button(text='Generate Password', command=generate_password)
generateBtn.grid(column=2, row=3)
addBtn = Button(text='Add', width=36, command=get_data)
addBtn.grid(column=1, row=4, columnspan=2)

window.mainloop()