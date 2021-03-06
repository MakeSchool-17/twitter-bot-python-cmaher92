import random
import Hashtable

# [brian] this will be explained below
from collections import defaultdict

file_path = 'the_early_cave.txt'
frm = '-$!@#$%^&*()_+-=[]}{/},.?:;|'
to = '                            '
trans_table = str.maketrans(frm, to)


def histogram(list_of_words):
    histogram = {}
    for x in list_of_words:
        # [brian] This is a really common pattern, so python has tried to make it easy
        # to write by providing `defaultdict` for you.
        if x in histogram:
            histogram[x] += 1
        else:
            histogram[x] = 1
    # print(words.get('only'))
    return histogram
    # sorted_words = sorted(words.items(), key=operator.itemgetter(1))
    # return sorted_words

    # [brian] The above can be written:
    histogram = defaultdict(int)
    for x in list_of_words:
        histogram[x] += 1
    return histogram
    # defaultdict takes a constructor, and when the key isn't found calls that
    # constructor instead of throwing an Exception. Here, `int` is a function
    # which returns 0, the default value.
    # https://docs.python.org/2/library/collections.html#collections.defaultdict


def test_histogram(selected_words_list):
    hgram = []                           # create a new list called hgram
    for word in selected_words_list:     # for each word in the list of words
        index = find(word, hgram)        # check if word is in hgram already
        if index is None:                # if word is not in histogram
            hgram.append((word, 1))      # add a new word-count pair to hgram
        else:                            # if word is already in hgram
            count = hgram[index][1]      # find its current count
            new_pair = (word, count + 1) # make a new word-count pair
            hgram[index] = new_pair      # replace word-count pair
    return hgram                         # return the hgram


def find(item, hgram):
    # [brian] Nice! Just what I would have written
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
    # [brian] Careful, you forgot to close the file! In a small script like this it's not
    # a big problem, but in a larger program this could cause quite a bit of trouble
    words_str  = open(dict_words, 'r').read()
    # [brian] luckily, this is also a common pattern, so python has made writing it easy:
    with open(dict_words, 'r') as words_file:
        words_str = words_file.read()
    # the file will automatically be closed once the program leaves the with block.
    # If you don't know what a context manager is don't worry too much about the syntax,
    # but always wrapping file opens with a with block is a really good habit to get into.

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


def txt_to_list(file_path):              # opens text, makes into list
    with open(file_path) as f:
        my_file = f.read()
        # print(myFile)
        my_string = my_file.translate(trans_table).lower()
        list_of_words = my_string.split()
        return list_of_words


def frequency(word, hgram):               # takes word and list from histogram
    index = find(word, hgram)             # gives the index for the word
    if index:                             # increments found word
        word_count_pair = hgram[index]
        return word_count_pair[1]
    else:
        return 0
        

def main():
    list_of_words = txt_to_list(file_path)  # returns words as a list
    histogram_dict = histogram(list_of_words)    # returns histogram as a dict
    distribution_list = cumulative_distribution(histogram_dict)  # weighted words list
    word = sample_from_sum(distribution_list)
    # histogram_weighted = test_histogram(distribution_list)
    return word

if __name__ == '__main__':
    print(main())
