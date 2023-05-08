import re
from task1.constants import ABBREVIATIONS, FILES, ELLIPSIS, DOUBLE_SIGNS, NAME, NUMBERS, MATH_SIGNS
from task1.constants import NUM_SENTENCES, NUM_NONDECLARE_SENTENCES, PUNCTUATION
def correctText(text):
    t = re.sub(FILES, "", text)
    t = re.sub(ELLIPSIS, ".", t)
    t = re.sub(DOUBLE_SIGNS, "?", t)
    t = re.sub(NAME, "", t)
    t = re.sub(NUMBERS, "", t)
    t = re.sub(MATH_SIGNS, "", t)

    for abbr in ABBREVIATIONS:
        t = re.sub(abbr, "", t)

    # print(t)

    return t

def amountOfSentences(text):
    return len(re.findall(NUM_SENTENCES, text))

def amountOfNondecSentences(text):
    return len(re.findall(NUM_NONDECLARE_SENTENCES, text))

def showOnlyWords(text):
    t = re.sub(NUMBERS, "", text)
    t = re.sub(MATH_SIGNS, "", t)
    t = re.sub(PUNCTUATION, "", t)

    # print(t)

    return t.split()

def lengthAllWords(onlyWords):
    lengthAllWords = 0

    for word in onlyWords:
        lengthAllWords += len(word)

    # print(lengthAllWords)
    return lengthAllWords

def averageLengthSent(correctText, onlyWords):
    countSent = amountOfSentences(correctText)

    if not countSent:
        return 0

    # print(countSent)
    return round(lengthAllWords(onlyWords) / countSent)

def averageLengthWords(onlyWords):
    # print(len(onlyWords))
    return round(lengthAllWords(onlyWords) / len(onlyWords))
