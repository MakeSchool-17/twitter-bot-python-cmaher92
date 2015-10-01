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


def cumulative_distribution(histogram):
    distribution_list = []
    distribution_range = 0
    for word, freq in histogram.items():
        if word not in distribution_list:
            upper_limit = distribution_range + freq
            distribution_range += freq
            distribution_list.append((word, upper_limit))
    return distribution_list


def sample_from_sum(distribution_list):
    token_tuple = distribution_list[-1]
    # print(token_tuple)
    tokens = token_tuple[-1]
    # print(tokens)
    for word, upper_limit in distribution_list:
        index = random.randint(0, tokens - 1)
        if index < upper_limit:
            return word


def txt_to_list(file_path):
    with open(file_path) as f:
        my_file = f.read()
        # print(myFile)
        my_string = my_file.translate(trans_table).lower()
        my_list = my_string.split()
        return my_list


def main():
    word_list = txt_to_list(file_path)
    x = histogram(word_list)
    y = cumulative_distribution(x)
    return sample_from_sum(y)


if __name__ == '__main__':
    print(main())
