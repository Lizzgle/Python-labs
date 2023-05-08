from task1.functions import correctText, amountOfSentences, amountOfNondecSentences
def mainTask1():
    with open("task1/test.txt") as f:
        text = f.read()
    print(text)

    CORRECT_TEXT = correctText(text)

    print(f"amount of sentences in the text: {amountOfSentences(CORRECT_TEXT)}")

    print(f"amount of non-declarative sentences in the text: {amountOfNondecSentences(CORRECT_TEXT)}")