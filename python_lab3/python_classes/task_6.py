class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

numbers_list = [i for i in range(2, 20)]
prime_filter = PrimeFilter(numbers_list)
print(*prime_filter.filter_primes(), sep=", ")
