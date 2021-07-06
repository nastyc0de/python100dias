# Create the logging_decorator() function 👇
def logging_decorator(function):
  def internal(*args):
    print(f'usaste la funcion {function.__name__}{args}')
    res = function(*args)
    print(f'resultado: {res}')
  return internal


# Use the decorator 👇
@logging_decorator
def suma(a, b, c):
  return a + b + c

suma(1,2,3)