import time


number = int(input())
milliseconds = int(input())


def invoke_squareroot(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return number**0.5


print(
    f"Square root of {number} after {milliseconds} miliseconds is",
    invoke_squareroot(number, milliseconds),
)
