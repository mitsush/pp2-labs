


def unique_elements(some_list):
    new_list = list()

    for i in some_list:
        if i not in new_list:
            new_list.append(i)


    return new_list

# print(unique_elements([100, 75, 100, 20, 75, 12, 75, 25]))
