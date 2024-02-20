

def generator(n):
    numbers = range(n)
    for i in numbers:
        yield i * i

print([i for i in generator(int(input()))])