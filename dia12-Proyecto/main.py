import random

level = input('Ingrese la dificultad. "facil", "dificil": ')
intentos = 0
if level == 'facil':
    intentos = 10
elif level == 'dificil':
    intentos = 5

numero_pc = random.randint(1,99)
while intentos != 0:
    numero_user = int(input('Ingresa un numero para adivinar: '))
    if numero_pc > numero_user:
        print('FRIO no estas cerca, te falta para llegar del numero')
        print(intentos)
        intentos -= 1
    elif numero_pc < numero_user:
        print('FRIO no estas cerca, te pasaste del numero')
        print(intentos)
        intentos -= 1
    else:
        print('Lo lograste')
        print(intentos)
        intentos = 0
print('game over')
