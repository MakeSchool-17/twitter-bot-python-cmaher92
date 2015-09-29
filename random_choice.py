import random


def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            print(i)
if __name__ == '__main__':
    weights = [2, 3, 5]
    weighted_choice(weights)
