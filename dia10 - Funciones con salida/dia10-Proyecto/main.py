# Calculator

# Sumar
def add(n1, n2):
    return n1 + n2
# Restar
def sub(n1, n2):
    return n1 - n2
# Multiplicar
def mult(n1, n2):
    return n1 * n2
# Dividir
def divi(n1, n2):
    return n1 / n2

op_dict = {
    "+":add,
    "-":sub,
    "*":mult,
    "/":divi,
}
num1 = int(input('Ingrese el 1er numero: '))
num2 = int(input('Ingrese el 2do numero: '))

for operation in op_dict:
    operation_simbol = input("Escoge una operacion: ")
    if operation_simbol == operation:
        answer = op_dict[operation]
# print(f"{num1} {operation_simbol} {num2} = {answer}")1
