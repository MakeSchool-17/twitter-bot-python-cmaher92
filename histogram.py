import random

file_path = 'the_early_cave.txt'
frm = '-$!@#$%^&*()_+-=[]}{/},.?:;|'
to = '                            '
trans_table = str.maketrans(frm, to)


def histogram(word_list):
    histogram = {}
    for x in word_list:
        if x in histogram:
            histogram[x] += 1
        else:
            histogram[x] = 1
    # print(words.get('only'))
    return histogram
    # sorted_words = sorted(words.items(), key=operator.itemgetter(1))
    # return sorted_words


def test_histogram(selected_words_list):
    hgram = []                           # create a new list called hgram
    for word in words:                   # for each word in the list of words
        index = find(word, hgram)        # check if word is in hgram already
        if index is None:                # if word is not in histogram
            hgram.append((word, 1))      # add a new word-count pair to hgram
        else:                            # if word is already in hgram
            count = hgram[index][1]      # find its current count
            new_pair = (word, count + 1) # make a new word-count pair
            hgram[index] = new_pair      # replace word-count pair
    return hgram                         # return the hgram


def find(item, hgram):
    for index, pair in enumerate(hgram):
        if pair[0] == item:
            return index
    return None


def cumulative_distribution(histogram):
    distribution_list = []
    distribution_range = 0
    for word, freq in histogram.items():
        if word not in distribution_list:
            upper_limit = distribution_range + freq
            distribution_range += freq
            distribution_list.append((word, upper_limit))
    return distribution_list


def list(length):
    dict_words = '/usr/share/dict/words'
    words_str  = open(dict_words, 'r').read()
    all_words  = words_str.split("\n")
    return all_words[0:length]


def sample_from_sum(distribution_list):
    token_tuple = distribution_list[-1]
    # print(token_tuple)
    tokens = token_tuple[-1]
    # print(tokens)
    index = random.randint(0, tokens - 1)
    for word, upper_limit in distribution_list:
        if index < upper_limit:
            return word


def list(length):
    dict_words = '/usr/share/dict/words'
    words_str  = open(dict_words, 'r').read()
    all_words  = words_str.split("\n")
    return all_words[0:length]


# def test_probability():


def txt_to_list(file_path):
    with open(file_path) as f:
        my_file = f.read()
        # print(myFile)
        my_string = my_file.translate(trans_table).lower()
        my_list = my_string.split()
        return my_list


def main():
    word_list = txt_to_list(file_path)
    histogram_dict = histogram(word_list)
    distribution_list = cumulative_distribution(histogram_dict)
    word = sample_from_sum(distribution_list)
    # words_in_list = list(10)
    # print(words_in_list)
    return word

if __name__ == '__main__':
    main()
