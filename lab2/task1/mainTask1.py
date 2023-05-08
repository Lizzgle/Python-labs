from task1.functions import correctText
def mainTask1():
    with open("task1/test.txt") as f:
        text = f.read()
    print(text)

    correctText(text)