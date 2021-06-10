# file not found
# with open('abc.txt') as file:
#     file.read()

# # keyError
# a_dict = {'key': 'value'}
# value = a_dict['not_key']

# ejemplo
# try:
#     file = open('abc.txt')
#     a_dict = {'key': 'value'}
#     print(a_dict['key'])
# except FileNotFoundError:
#     file = open('abc.txt', 'w')
#     file.write('Something')
# except KeyError as error_msg:
#     print(f'La key {error_msg} no existe')
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print('archivo cerrado')

#  raise
height = float(input('height: '))
weight = int(input('weight: '))
if height > 3:
    raise ValueError('La altura humana no puede ser mayor a 3 metros')
bmi = weight / height ** 2