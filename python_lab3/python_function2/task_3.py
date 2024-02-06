from movies_list import movies


def filter_category(category_name):
    for movie in movies:
        for key, value in movie.items():
            if movie["category"] == category_name:
                print(key, value, sep=" - ")
                break


category = [movie['category'] for movie in movies]
filter_category(category[12])
