file_path = 'the_early_cave.txt'
frm = '-$!@#$%^&*()_+-=[]}{/},.?:;|'
to = '                            '
trans_table = str.maketrans(frm, to)


def histogram(word_list):
    words = {}
    for x in word_list:
        if x in words:
            words[x] += 1
        else:
            words[x] = 1
    print(words.get('only'))
    return words
    # sorted_words = sorted(words.items(), key=operator.itemgetter(1))
    # return sorted_words


def cumulative_distribution(words):
    distribution_list = []
    distribution_range = 0
    for word, freq in words.items():
        if word not in distribution_list:
            upper_limit = distribution_range + freq
            distribution_range += freq
            distribution_list.append((word, upper_limit))
    return distribution_list


def txt_to_list(file_path):
    with open(file_path) as f:
        myFile = f.read()
        # print(myFile)
        myString = myFile.translate(trans_table).lower()
        myList = myString.split()
        return myList


def main():
    word_list = txt_to_list(file_path)
    x = histogram(word_list)
    return cumulative_distribution(x)


if __name__ == '__main__':
    main()
