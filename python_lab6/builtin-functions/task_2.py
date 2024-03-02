string = input()


def upper_lower_count(string: str):
    return (
        len(list(filter(str.islower, string))),
        len(list(filter(str.isupper, string))),
    )


upper, lower = upper_lower_count(string)

print(
    "The number of upper strings: {0}. The number of lower strings: {1}".format(
        upper, lower
    )
)
