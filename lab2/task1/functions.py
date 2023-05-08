import re
from task1.constants import ABBREVIATIONS, FILES, ELLIPSIS, DOUBLE_SIGNS, NAME, NUMBERS, MATH_SIGNS
from task1.constants import NUM_SENTENCES, NUM_NONDECLARE_SENTENCES, PUNCTUATION
def correctText(text):
    word = re.sub(FILES, "", text)
    word = re.sub(ELLIPSIS, ".", word)
    word = re.sub(DOUBLE_SIGNS, "?", word)
    word = re.sub(NAME, "", word)
    word = re.sub(NUMBERS, "", word)
    word = re.sub(MATH_SIGNS, "", word)

    for abbr in ABBREVIATIONS:
        word = re.sub(abbr, "", word)

    print(word)

    return word

def amountOfSentences(text):
    return len(re.findall(NUM_SENTENCES, text))

def amountOfNondecSentences(text):
    return len(re.findall(NUM_NONDECLARE_SENTENCES, text))

def showOnlyWords(text):
    t = re.sub(NUMBERS, "", text)
    t = re.sub(MATH_SIGNS, "", t)
    t = re.sub(PUNCTUATION, "", t)

    print(t)

    return t.split()

