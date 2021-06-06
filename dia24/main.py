# file = open('/home/serie5/Escritorio/Python en 100 dias/dia24/file.txt')
# contents = file.read()
# print(contents)
# file.close()

# with open('/home/serie5/Escritorio/Python en 100 dias/dia24/file.txt') as file:
#     contents = file.read()
#     print(contents)

# with open('/home/serie5/Escritorio/Python en 100 dias/dia24/file.txt', mode='w') as file:
#     file.write('New Text')

# with open('/home/serie5/Escritorio/Python en 100 dias/dia24/file.txt', mode='a') as file:
#     file.write('\n New Text')

with open('/home/serie5/Escritorio/Python en 100 dias/dia24/new_file.txt', mode='a') as file:
    file.write('\n New Text')