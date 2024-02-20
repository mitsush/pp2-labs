

def generator(n):
    numbers = range(n)
    for i in numbers:
        if i % 3 == 0 & i % 4 == 0:
            yield i

print([i for i in generator(int(input()))])