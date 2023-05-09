import unittest

from task1.functions import correctText, amountOfSentences, amountOfNondecSentences, showOnlyWords, lengthAllWords, averageLengthSent, averageLengthWords, topNgrams

class CorrectText1(unittest.TestCase):
    def test_CorrectText(self):
        text = "Hey. Hey! Hey? HEY?! Hey..."
        assert correctText(text) == "Hey. Hey! Hey? HEY? Hey."

class CorrectText2(unittest.TestCase):
    def test_CorrectText(self):
        text = "0.2. 9/0.9 etc."
        assert correctText(text) == ". ."

class CorrectText3(unittest.TestCase):
    def test_CorrectText(self):
        text = "Mr. John, Mrs. Beth and their friend Dr. Pilulkin."
        assert correctText(text) == "John, Beth and their friend Pilulkin."

class CorrectText4(unittest.TestCase):
    def test_CorrectText(self):
        text = "Sep. 8, 2003 on the St. Leninskaya, Bldg. 13."
        assert correctText(text) == " ,  on the Leninskaya, ."


class AmountOfSentences1(unittest.TestCase):
    def test_AmountOfSentences(self):
        text = "I have got many toys. I have got balls, soldiers, cars, planes and different robots. " \
               "I like them all, but most of all I like my set of Lego Star Wars. " \
               "My parents gave this set to me for my last birthday. "
        assert amountOfSentences(text) == 4

class AmountOfSentences2(unittest.TestCase):
    def test_AmountOfSentences(self):
        text = "Hey! How are you? Wow... What are you doing?!"
        correcttext = correctText(text)
        assert amountOfSentences(correcttext) == 4


class AmountOfNondecSentences1(unittest.TestCase):
    def test_AmountOfNondecSentences(self):
        text = "Hey! How are you? Wow... What are you doing?!"
        correcttext = correctText(text)
        assert amountOfNondecSentences(correcttext) == 3


class ShowOnlyWords1(unittest.TestCase):
    def test_ShowOnlyWords(self):
        text = "Hey! How are you? Wow... What are you doing?!"
        assert showOnlyWords(text) == ['Hey', 'How', 'are', 'you', 'Wow', 'What', 'are', 'you', 'doing']


class LengthAllWords1(unittest.TestCase):
    def test_LengthAllWords(self):
        text = "Hey! How are you? Wow... What are you doing?!"
        onlywords = showOnlyWords(text)
        assert lengthAllWords(onlywords) == 30


class AverageLengthSent1(unittest.TestCase):
    def test_AverageLengthSent(self):
        text = "Hey! How are you? Wow... What are you doing?!"
        correcttext = correctText(text)
        onlywords = showOnlyWords(text)
        assert averageLengthSent(correcttext, onlywords) == 8


class AverageLengthWords(unittest.TestCase):
    def test_AverageLengthWords(self):
        text = "Hey! How are you? Wow... What are you doing?!"
        onlywords = showOnlyWords(text)
        assert averageLengthWords(onlywords) == 3

class TopNgrams(unittest.TestCase):
    def test_TopNgrams(self):
        text = "Hey! How are you? Wow... What are you doing?!"
        onlywords = showOnlyWords(text)
        assert topNgrams(text, onlywords, n=4, k=10) == [('Hey How are you', 1), ('How are you Wow', 1), ('are you Wow What', 1), ('you Wow What are', 1), ('Wow What are you', 1), ('What are you doing', 1)]