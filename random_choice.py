import re

source_text = open('the_early_cave.txt').read().split()
print(source_text)


def histogram(source_text):
    histog = []
    index = 0
    for word in source_text:
        filter(word)
        if word in histog:
            histog.append((word, 0))
            index += 1
        else:
            histog[index][1] = 1
            index = 1
    print(histog)

def filter(word):
    re.sub(r'-_W+', '', word)
    word = word.lstrip('_-?.,"')
    word = word.rstrip('_-?.,"')
    return word


if __name__ == "__main__":
    histogram(source_text)
