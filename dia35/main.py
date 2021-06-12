import requests
import os
from twilio.rest import Client


account_sid = ''
auth_token = ''

API_KEY =''
LAT = -17.960060
LONG = -67.093269
EXCLUDE = 'current,daily,minutely'

parameters = {
    'lat':LAT,
    'lon':LONG,
    'exclude':EXCLUDE,
    'appid':API_KEY
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
data = response.json()
hourly = data['hourly'][:12]
code = [hour_data['weather'][0]['id'] for hour_data in hourly]
will_rain = False
for data in code:
    if data < 700:
        will_rain = True

if will_rain:
    print('Va llover en Varsovia lleva un paraguas...')
    # client = Client(account_sid, auth_token)
    # message = client.messages \
    #             .create(
    #                  body="Va llover en Varsovia lleva un paraguas",
    #                  from_='+19123304775',
    #                  to='+59169604496'
    #              )

    # print(message.status)
