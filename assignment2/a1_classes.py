from moviecollection import MovieCollection
from movie import Movie

FILENAME = "movies.json"
CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller", "Other"]


def main():
    print("Must-See Movies 2.0 - by Your Name")
    collection = MovieCollection()
    collection.load_movies(FILENAME)
    print(f"{len(collection.movies)} movies loaded from {FILENAME}")
    menu(collection)
    collection.save_movies(FILENAME)
    print(f"{len(collection.movies)} movies saved to {FILENAME}")
    print("Have a nice day :)")


def menu(collection: MovieCollection):
    while True:
        print("\nMenu:\nD - Display movies\nA - Add new movie\nW - Watch a movie\nQ - Quit")
        choice = input(">>> ").strip().lower()
        if choice == "d":
            display_movies(collection)
        elif choice == "a":
            add_movie(collection)
        elif choice == "w":
            watch_movie(collection)
        elif choice == "q":
            break
        else:
            print("Invalid menu choice")


from operator import attrgetter

def display_movies(collection):
    sorted_movies = sorted(collection.movies, key=attrgetter("year", "title"))
    for i, movie in enumerate(sorted_movies, 1):
        print(f"{i}. {movie}")
    print(f"{collection.get_number_watched()} movies watched. {collection.get_number_unwatched()} still to watch.")



def add_movie(collection):
    title = get_non_blank_input("Title: ")
    year = get_valid_int("Year: ", min_value=1)
    print("Categories available:", ", ".join(CATEGORIES))
    category = get_non_blank_input("Category: ").capitalize()
    if category not in CATEGORIES:
        print("Invalid category; using Other")
        category = "Other"
    new_movie = Movie(title, year, category)
    collection.add_movie(new_movie)
    print(f"{title} ({category} from {year}) added to movie list")


def watch_movie(collection):
    unwatched_movies = [m for m in collection.movies if not m.is_watched]
    if not unwatched_movies:
        print("No more movies to watch!")
        return
    display_movies(collection)
    movie_number = get_valid_int("Enter the movie number to mark watched: ", min_value=1, max_value=len(collection.movies))
    selected = collection.movies[movie_number - 1]
    if selected.is_watched:
        print(f"You have already watched {selected.title}.")
    else:
        selected.mark_watched()
        print(f"{selected.title} ({selected.year}) watched.")


def get_non_blank_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input can not be blank")


def get_valid_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Number must be >= {min_value}")
            elif max_value is not None and value > max_value:
                print(f"Number must be <= {max_value}")
            else:
                return value
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == '__main__':
    main()
