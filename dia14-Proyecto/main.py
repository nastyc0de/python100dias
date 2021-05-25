from art import logo, vs
from game_data import data
import random

print(logo)


def take_info_from_data(dict_pick):
    name = dict_pick['name']
    # followers = dict['follower_count']
    desc = dict_pick['description']
    country = dict_pick['country']
    return f"{name}, a {desc} from {country}"


def check_answer(pick, a_follower, b_follower):
    if a_follower > b_follower:
        return pick == 'a'
    else:
        return pick == 'b'


point = 0
finish = True

b = random.choice(data)
while finish:
    a = b
    b = random.choice(data)

    while a == b:
        b = random.choice(data)
    print(f'Compara: {take_info_from_data(a)}')
    print(vs)
    print(f'Contra: {take_info_from_data(b)}')

    pick = input('Quien tiene mas seguidores: "A" o "B" ').lower()
    a_follower = a['follower_count']
    b_follower = b['follower_count']
    is_correct = check_answer(pick, a_follower, b_follower)

    if is_correct:
        point += 1
        print(f'correcto. Marcador: {point}')
    else:
        finish = False
        print(f'incorrecto. Marcador final: {point}')