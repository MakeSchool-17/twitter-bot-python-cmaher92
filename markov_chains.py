import random

tokens = ['the', 'the', 'the', 'the', 'best', 'times', 'times', 'worst']
probs = ['0.5', '0.125', '0.25', '0.125']

def uniformSample(items):
    while True:
        for (index, prob) in enumerate(probs):
            if random.random() <= prob:
                return items[index]

sample = weightedSample(types, probs)
