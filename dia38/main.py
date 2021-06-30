import requests
import os
from datetime import datetime

APP_ID = os.environ["API_ID_38"]
print(APP_ID)
API_KEY = os.environ.get('API_KEY_38')
print(os.environ[API_KEY_38])
URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# workout = input("Que ejercicio hiciste hoy dia: ")
workout = '10min of squats'
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY

}
body = {
    "query": workout
}
response = requests.post(url=URL,json=body,headers=header )
data = response.json()
# EXERCISE = data['exercises'][0]['name']
# DURATION = data['exercises'][0]['duration_min']
# CALORIES = data['exercises'][0]['nf_calories']


day = datetime.now()
DATE = day.strftime("%x")
TIME = day.strftime("%X")
# # Usando La Configuracion basica
# SECRET = 'Basic YW5kcmVzOjE5OTEyOTA4'
SECRET = os.environ.get('SECRET_38')
# En sheety
sheety_url = 'https://api.sheety.co/3f11d98e83a8af02d3de93f531888435/myWorkouts/workouts'

for exercise in data["exercises"]:
    dataBody = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
header_config = {
    "Authorization": SECRET
}
send = requests.post(url=sheety_url, json=dataBody, headers=header_config)
print(send.text)
