import random
import bisect


def weighted_choice_b(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    print(bisect.bisect_right(totals, rnd))


if __name__ == '__main__':
    weights = [2, 3, 5]
    weighted_choice_b(weights)
