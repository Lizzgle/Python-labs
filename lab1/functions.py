
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

        case 'div':
            if not num2:
                return print("Division by 0 is not possible")
            return num1 / num2

        case _:
            return print("This operation does not exist")


def evenNumbers(list, newList):
    for num in list:
        if int(num) % 2 == 0:
            newList.append(num)
        else:
            int(num)+1

    if not len(newList):
        return print("The entered list is empty or does not have even-numbers")
    else:
        return newList
