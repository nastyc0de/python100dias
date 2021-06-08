from tkinter import *

window = Tk()
window.title('Convertidor a Km')
window.minsize(height=200, width=300)
window.config(pady=50, padx=20)

def calculate():
    input= input_value.get()
    res = float(input)*1.60934
    result.config(text=f"{res}")
    return 
# input
input_value = Entry(width=10)
input_value.grid(column=1, row=0)

# label
miles = Label(text='Miles')
miles.grid(column=2,row=0)

equal = Label(text='es igual a:')
equal.grid(column=0,row=1)

result = Label(text='0')
result.grid(column=1,row=1)

km = Label(text='Km')
km.grid(column=2,row=1)

# button
calculate_btn = Button(text='Calculate', command=calculate)
calculate_btn.grid(column=1, row=2)


window.mainloop()
