from movies_list import movies


def average_rating(movies):
    ratings = 0

    for movie in movies:
        for key, value in movie.items():
            ratings += movie["imdb"]
            break

    return (ratings / len(movies))


print(average_rating(movies))
