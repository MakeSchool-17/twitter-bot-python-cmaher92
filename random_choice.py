import random
import sys


choices = ['unknown']*70 + ['yes']*15 + ['no']*15
random_choice = random.shuffle(choices)
print(random_choice)
