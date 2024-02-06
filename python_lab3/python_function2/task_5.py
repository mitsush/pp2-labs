from movies_list import movies


def average_rating(category_name):
    ratings = 0
    movie_count = 0

    for movie in movies:
        for key, value in movie.items():
            if movie["category"] == category_name:
                ratings += movie["imdb"]
                movie_count += 1
                break

    return (ratings / movie_count)


category = [movie['category'] for movie in movies]
print(average_rating(category[12]))
