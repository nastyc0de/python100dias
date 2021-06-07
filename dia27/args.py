# def add(*args):
#     return sum(args)




# print(add(2,5,7,8,2,1,5,7,9,5,1))
# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)

# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']
        self.color = kwargs.get('color')

my_car = Car(make='Nissan', model='GT-R', color='blue')
print(my_car.color)