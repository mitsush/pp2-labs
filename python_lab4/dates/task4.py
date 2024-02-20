from datetime import datetime


def day_diff(first_day, second_day):
    date_format = "%d.%m.%Y %H:%M:%S"

    diff = datetime.strptime(first_day, date_format) - datetime.strptime(second_day, date_format)

    return diff.total_seconds()


# print(day_diff("27.02.2024 18:29:00", "28.02.2024 18:29:00"))