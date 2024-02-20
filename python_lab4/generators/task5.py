

def generator(n):
    numbers = reversed(range(n))
    for i in numbers:
        yield i

print([i for i in generator(int(input()))])