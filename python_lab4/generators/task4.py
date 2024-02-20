

def square(a, b):
    numbers = range(a, b + 1)
    for i in numbers:
        yield i * i

print([i for i in square(int(input()), int(input()))])