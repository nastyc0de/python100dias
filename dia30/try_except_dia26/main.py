
# usando el ciclo for

# numbers = [1, 2, 3, 4]

# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print (new_list)

# usando listas de comprension
# new_list = [n + 1 for n in numbers]
# print(new_list)

# new_list = []
# for n in range(20):
#     rand = random.randint(1,9)
#     new_list.append(rand)
# print(new_list)

# new_list = [random.randint(1,9) for n in range(20)]
# print(new_list)
# set_a = set(new_list)
# print(list(set_a))

# name = 'Andres'
# letter_list = [letter for letter in name]

# string_l = ''
# v = []
# for i in range(13):    
#     v.append(i)
# string_l +=  str(v)
# print(string_l)
# v = [i for i in range(14)]
# string_l += str(v)

# value = [i*2 for i in range(1,5)]
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# new_names = [name.upper() for name in names if len(name) > 5]

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
# #Write your 1 line code 👇 below:
# squared_numbers = [num ** 2 for num in numbers]

# #Write your code 👆 above:

# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 

# 34, 55]
# # 🚨 Do Not Change the code above

# #Write your 1 line code 👇 below:
# result = [num for num in numbers if num % 2 == 0]

# #Write your code 👆 above:

# print(result)

# with open('/home/serie5/Escritorio/Python en 100 dias/dia26/file1.txt') as f1:
#     data1 = f1.readlines()
# with open('/home/serie5/Escritorio/Python en 100 dias/dia26/file2.txt') as f2:
#     data2 = f2.readlines()

# result = [int(num1) for num1 in data1 if num1 in data2]
# print(result)

# diccionarios

# student_scores = { student:random.randint(1,100) for student in names}
# passed_students = {student:score for (student, score) in student_scores.items() if score > 60}
# sentence = "What is the Airspeed Velocity of an Unladen Swallow? is the Airspeed Velocity Unladen Swallow? Unladen Swallow? Airspeed Velocity"
# # Don't change code above 👆

# # Write your code below:
# result = {word:len(word) for word in sentence.split()}

# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆


# # Write your code 👇 below:
# weather_f = {key:(value * 9/5) + 32 for (key, value) in weather_c.items()}


# print(weather_f)

# Listas de comprension con dataframe de Pandas

# studen_dict = {
#     'student':['Andres', 'James', 'Adan'],
#     'score':[56,66,89]
# }
import pandas as pd

# data_dict = pd.DataFrame(studen_dict)
# # for (key, value) in data_dict.items():
# #     print(key)
# # usar iterrows()
# for (index, row) in data_dict.iteritems():
#     print(row)

data = pd.read_csv('./nato_phonetic_alphabet.csv')
# for (key, value) in data.iterrows():
#     print(value.letter, value.code)
data_dict = { value.letter:value.code for (key, value) in data.iterrows()}
# name = input('Ingrese un nombre:' )
def generate_phonetic():
    name = input('Ingrese un nombre: ')
    try:
        code_dict = [data_dict[letter] for letter in name.upper()]
    except KeyError:
        print('Lo siento solo caracteres alfanumericos')
        generate_phonetic()
    else:
        print(code_dict)
generate_phonetic()
    