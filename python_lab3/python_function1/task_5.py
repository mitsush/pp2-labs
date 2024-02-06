from itertools import permutations


def all_permutations(string):
    perms = permutations(string)
    for i in perms:
        print(*i, sep="")


all_permutations("Hello")
