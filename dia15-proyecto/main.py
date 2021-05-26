MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
turn_on = True
while turn_on:
    #  prompt para preguntar al usuario
    prompt = input("​What would you like? (espresso/latte/cappuccino):")
    # apagar la maquina si se ingresa "off"
    if prompt == "off":
        turn_on = False
    # imprimir un reporte si se ingresa "report"
    elif prompt == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['water']}ml")
        print(f"coffee: {resources['water']}g")
        print(f"money: ${money}")
# revisar si se tiene los recursos suficientes
    else:
        drink = MENU[prompt]
# procesar las monedas quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

# hacer el cafe