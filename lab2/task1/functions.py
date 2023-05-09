import re
from task1.constants import ABBREVIATIONS, FILES, ELLIPSIS, DOUBLE_SIGNS, NAME, NUMBERS, MATH_SIGNS
from task1.constants import NUM_SENTENCES, NUM_NONDECLARE_SENTENCES, PUNCTUATION, K
def correctText(text):
    t = re.sub(FILES, "", text)
    t = re.sub(ELLIPSIS, ".", t)
    t = re.sub(DOUBLE_SIGNS, "?", t)
    t = re.sub(NAME, "", t)
    t = re.sub(NUMBERS, "", t)
    t = re.sub(MATH_SIGNS, "", t)

    for abbr in ABBREVIATIONS:
        t = re.sub(abbr, "", t)

    print(t)

    return t

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

def topNgrams(text, onlyWords, n, k):
    text = text.lower()

    ngrams = dict()

    for i in range(len(onlyWords) - n + 1):
        ngram = " ".join(onlyWords[i: i + n])

        if ngram in ngrams:
            ngrams[ngram] += 1
        else:
            ngrams[ngram] = 1

    # print(ngrams)

    return sorted(ngrams.items(), key=lambda x: x[1], reverse=True)[:k]

def menu(text, onlyWords):
    while True:
        inp = input(f"Do you want enter your personal K and N? Please, enter \"y\" or \"n\": \n")

        if inp != "y" and inp != "n":
            print("You enter something wrong, try again\n")

        elif inp == "y":
            N = getNumber(input("n-grams. Enter a number n: "))
            K = getNumber(input("Top-k. Enter a number k: "))

        else:
            N = 4
            K = 10

        ngrams_list = topNgrams(text, onlyWords, int(N), int(K))
        print(f"top-{K} :  {N}-grams in the text:")

        for ngram in ngrams_list:
            print(ngram)
        break


def getNumber(a):
    while True:
        if a.isdigit() and int(a) >= 0:
            return a
        else:
            return getNumber(input("You should enter positive number: "))