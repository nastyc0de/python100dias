import requests

response = requests.get(url='https://jsonplaceholder.typicode.com/posts')
data = response.json()