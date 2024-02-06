from movies_list import movies


def bad_rating(movie_name):
    for movie in movies:
        for key, value in movie.items():
            if movie["name"] == movie_name:
                if movie["imdb"] < 5.5:
                    return True


names = [movie['name'] for movie in movies]
print(bad_rating(names[8]))
