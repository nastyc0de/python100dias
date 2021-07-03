import requests
from datetime import datetime

TOKEN = "thisissecret" 
USER = "nasty"
GRAPH_ID = "graph1"

url = "https://pixe.la/v1/users"
params = {
    "token":TOKEN, 
    "username":USER, 
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=url, json=params)
# print(response.text)
graph_url = f"{url}/{USER}/graphs"
graph_params = {
    "id":GRAPH_ID,
    "name":"graph-nasty",
    "unit":"commit",
    "type":"int",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_url, json=graph_params, headers=headers)
# pixel = f"{url}/{USER}/graphs/{GRAPH_ID}"
# today = datetime.now()
# pixel_body ={
#     "date": today.strftime("%Y%m%d"),
#     "quantity":"4",
# }

# response = requests.post(url=pixel, json=pixel_body, headers=headers)
# print(response.text)
today = datetime.now()

DATE = today.strftime("%Y%m%d")
pixelPut = f"{url}/{USER}/graphs/{GRAPH_ID}/{DATE}"
pixelPut_body = {
    "quantity":"20",
}
response = requests.delete(url=pixelPut, json=pixelPut_body, headers=headers)
print(response.text)