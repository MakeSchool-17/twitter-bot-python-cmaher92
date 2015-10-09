import nltk


def import_file(corpus):  # takes txt file, opens, reads, returns as string
    with open(corpus) as opened_file:
        read_file = opened_file.read()
        return read_file


def tokenize_text(read_file):  # tokenize file using natural language tk
    tokenized_corpus = nltk.word_tokenize(read_file)
    return tokenized_corpus


def main():
    corpus = 'abraham_lincoln.txt.utf-8.txt'
    read_file = import_file(corpus)
    return read_file
    tokenized_corpus = tokenize_text(read_file)
    return tokenized_corpus

if __name__ == '__main__':
    print(main())
