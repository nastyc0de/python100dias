import requests
import datetime


LAT = -17.960060
LONG = -67.093269
EMAIL = 'nastybitsz@gmail.com'

def is_close_enough():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    lat = float(data['iss_position']['latitude'])
    long = float(data['iss_position']['longitude'])
    if LAT -5 < lat < LAT +5 and LONG -5 < long < LONG +5:
        return True

# iss_pos = (lat, long)


# def get_quote():
#     response = requests.get(url='https://api.kanye.rest')
#     response.raise_for_status()
#     data = response.json()
#     quote = data['quote']
#     return quote

# a = get_quote()
# print(a)
def is_night():
    parameters = {
        'lat': LAT,
        'lng': LONG,
        'formatted':0
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data =response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    time = datetime.datetime.now().hour

    if sunrise <= time <= sunset:
        return True
if is_close_enough() and is_night():
    print('Esta cerca, revisa el cielo')
else:
    print('Falta.Espera')