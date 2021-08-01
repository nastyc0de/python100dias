import requests
def call_movie(title):
    PARAMS = {
        'apikey': 'faf1a00f',
        't':title
    }
    response = requests.get(url='http://www.omdbapi.com/',params=PARAMS)
    data = response.json()
    return {'title': data['Title'], 'year':data['Year'],'img': data['Poster'],'description':data['Plot']}