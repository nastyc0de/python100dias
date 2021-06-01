# importar los modulos
from  turtle import Screen,shape,Turtle
import pandas as pd
# Crear un screen
screen = Screen()
screen.title('USA States Game')
image = 'dia25/us-states-game-start/blank_states_img.gif'
screen.addshape(image)
shape(image)

correct_answer = []

data = pd.read_csv('dia25/us-states-game-start/50_states.csv')
all_state = data['state'].to_list()

while len(correct_answer) < 50:
    answer = screen.textinput(title=f'{len(correct_answer)}/50 Adivina el estado', prompt='Escribe un estado: ').title()
    if answer == 'Exit':
        missing_states = []
        for state in all_state:
            if state not in correct_answer:
                missing_states.append(state)
        print(missing_states)
        export_dataframe = pd.DataFrame(missing_states)
        export_dataframe.to_csv('missing.csv')
        break
    if answer in all_state:
        correct_answer.append(answer)
        state = data[data['state'] == answer]
        cord = Turtle()
        # cord.hideturtle()
        cord.penup()
        cord.goto(int(state.x),int(state.y))
        cord.write(answer)

