import random


def upcase_first_letter(sentenceString):
    return sentenceString[0].upper() + sentenceString[1:]


def generateSentence(int):
    with open('/usr/share/dict/words', encoding='utf-8') as a_file:
        lists = a_file.readlines()
        words = []
        for word in lists:
            word = word.split('\n')[0]
            words.append(word)
        # print(words)
        sentence = random.sample(words, int)
        sentenceString = ' '.join(sentence)
        print(upcase_first_letter(sentenceString))

generateSentence(9)
