from movies_list import movies


def bad_rating(movies):
    bad_movies = list()

    for movie in movies:
        for key, value in movie.items():
            if movie["imdb"] < 5.5:
                 bad_movies.append(movie)
                 break

    print(*bad_movies)


bad_rating(movies)
