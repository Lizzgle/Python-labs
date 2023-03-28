# Task1
import functions

print("Hello world")

#Task2
first = functions.inputData(input("Enter first number "))
second = functions.inputData(input("Enter second number "))
operator = input("Enter operation ")

result = functions.operation(int(first), int(second), operator)
print(result)
