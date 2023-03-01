
#task2
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
