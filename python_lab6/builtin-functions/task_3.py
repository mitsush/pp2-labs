string = input()


def reverse_string(string: list):
    return reversed(string)


print(True if string == "".join(list(reverse_string(string))) else False)
