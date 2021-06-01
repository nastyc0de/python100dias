# import csv

# with open('dia25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1])
#     print(temp)  
import pandas as pd

data = pd.read_csv('weather_data.csv')
print(data)
