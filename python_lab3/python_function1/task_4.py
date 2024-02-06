from math import sqrt


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(sqrt(n)) + 1))


def filter_prime(numbers):
    print(*filter(is_prime, numbers), sep='\n')


# filter_prime([1, 2, 8, 110, 15, 17, 19]) -> 2\n17\n19
