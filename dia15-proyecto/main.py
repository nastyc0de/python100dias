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


def is_enough_resource(ingredients):
    is_enough = True
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f'No existe los suficientes recursos para preparar el cafe {item}')
            is_enough = False
    return is_enough


def process_coins():
    """Return the total of coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many quarters?: "))*0.1
    total += int(input("how many quarters?: "))*0.05
    total += int(input("how many quarters?: "))*0.01
    return total


def is_transactions_succesful(money_received, drink_cost):
    """Retorna Verdadero. Cuando el pago es aceptado, o falso si el dinero es insuficiente"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Aqui esta tu cambio: {change}")
        global money
        money += drink_cost
        return True
    else:
        print('Lo siento no cuenta con el dinero suficiente')
        return False


def make_coffee(drink_name, order_ingredients):
    """ Deduce el requerimiento de ingredientes desde los recursos"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Aqui esta tu orden: {drink_name}")

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
        if is_enough_resource(drink["ingredients"]):
            payment = process_coins()
            if is_transactions_succesful(payment, drink['cost']):
                make_coffee(prompt, drink["ingredients"])

# procesar las monedas quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

# hacer el cafe