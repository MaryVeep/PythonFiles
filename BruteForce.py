# adapted from https://stackoverflow.com/questions/11747254/python-brute-force-algorithm Martjin Pieters' answer
import random
from itertools import chain, product

length = 5
pasw = ''
characters = 'abcdefghijklmnopqrstuvwxyz'  # lowercase only to save time

# create a random password designated length
for x in range(length):
    pasw += characters[random.randint(0, len(characters) - 1)]


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


attempts = 0
for attempt in bruteforce(characters, length):
    # comment out the print line to make it run much faster
    # print(attempt)
    attempts += 1
    if attempt == pasw:
        break
print(f"Password was {pasw}, took {attempts} attempts")
