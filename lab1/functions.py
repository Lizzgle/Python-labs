
#task2
def inputData(a):
    while True:
        if a.isdigit():
            return a
        else:
            return inputData(input("Try again "))

def operation(num1, num2, operator):
    match operator:
        case 'add':
            return num1 + num2

        case 'sub':
            return num1 - num2

        case 'mul':
            return num1 * num2

        case 'del':
            return num1 / num2

        case _:
            return print("This operation does not exist")
