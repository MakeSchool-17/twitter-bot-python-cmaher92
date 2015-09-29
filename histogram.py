import operator

file_path = 'the_early_cave.txt'
frm = '''-$!@#$%^&*()_+-=[]}{/},.?':|'''
to = '                            '
trans_table = str.maketrans(frm, to)


def histogram(word_list):
    words = {}
    for x in word_list:
        if x in words:
            words[x] += 1
        else:
            words[x] = 1
    sorted_words = sorted(words.items(), key=operator.itemgetter(1))
    # print(sorted_words)
    return sorted_words


def txt_to_list(file_path):
    with open(file_path) as f:
        myFile = f.read()
        # print(myFile)
        myString = myFile.translate(trans_table).lower()
        myList = myString.split()
        return myList


if __name__ == '__main__':
    word_list = txt_to_list(file_path)
    length = len(word_list)
    histogram(word_list)
    print("Number of words:", length)
