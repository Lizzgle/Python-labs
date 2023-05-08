import re
from task1.constants import ABBREVIATIONS, FILES, ELLIPSIS, DOUBLE_SIGNS, NAME, FLOAT_NUMBERS
from task1.constants import NUM_SENTENCIS, NUM_NONDECLARE_SENTENCIS
def correctText(text):
    word = re.sub(FILES, "", text)
    word = re.sub(ELLIPSIS, ".", word)
    word = re.sub(DOUBLE_SIGNS, "?", word)
    word = re.sub(NAME, "", word)
    word = re.sub(FLOAT_NUMBERS, "", word)

    for abbr in ABBREVIATIONS:
        word = re.sub(abbr, "", word)

    print(word)

    return word

def amountOfSentences(text):
    return len(re.findall(NUM_SENTENCIS, text))

def amountOfNondecSentences(text):
    return len(re.findall(NUM_NONDECLARE_SENTENCIS, text))