# import nltk

corpus = 'abraham_lincoln.txt.utf-8.txt'


def import_file(corpus):  # takes txt file, opens, reads, returns as string
    with open(corpus) as opened_file:
        read_file = opened_file.read()
    return read_file

def analyze_file(read_file)
