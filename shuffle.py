import random
import sys


if __name__ == '__main__':
    input = sys.argv[1:]
    random.shuffle(input)
    print(input)
