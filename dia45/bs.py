from os import name
from bs4 import BeautifulSoup
import requests

response = requests.get(url='https://news.ycombinator.com/')
yc_data = response.text

# obtener un elemento
soup = BeautifulSoup(yc_data, 'html.parser')
# art_tag = soup.find(name='a', class_='storylink')
# art_text = art_tag.getText()
# art_link = art_tag.get("href")
# art_upvote = soup.find(name='span', class_='score').getText()

# print(art_text)
# print(art_link)
# print(art_upvote)

# obtener una lista de todos los elementos
art_list_text = []
art_list_link = []
articles = soup.find_all(name='a', class_='storylink')
for article in articles:
    art_text = article.getText()
    art_list_text.append(art_text)
    art_link = article.get("href")
    art_list_link.append(art_link)

art_upvote =[ int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

number = max(art_upvote)
index = art_upvote.index(number)
print(art_list_text[index])
print(art_list_link[index])
# print(art_list_text)
# print(art_list_link)
# print(art_upvote)


# with open('./website.html') as datafile:
#     data = datafile.read()

# soup = BeautifulSoup(data, "html.parser")
# all_a = soup.find_all(name='a')
# # print(all_a)

# # for tag in all_a:
# #     print(tag.get("href"))

# # section = soup.find(name='h3', class_='heading')
# # print(section.name)

# name = soup.select_one("#name")
# print(name)

# heading = soup.select(".heading")
# print(heading.gettext)