"""
Program: Must-See Movies 1.0
Author: Hyunwoo Kim
Description: A program to track movies to watch and watched movies.
"""

import csv

# Constants
FILENAME = "movies.csv"
WATCHED = 'w'
UNWATCHED = 'u'
CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]


def main():
    """Main program to run the movie manager."""
    print("Must-See Movies 1.0 - by Your Name")
    movies = load_movies(FILENAME)
    print(f"{len(movies)} movies loaded from {FILENAME}")

    while True:
        print("\nMenu:\nD - Display movies\nA - Add new movie\nW - Watch a movie\nQ - Quit")
        choice = input(">>> ").strip().upper()
        if choice == 'D':
            display_movies(movies)
        elif choice == 'A':
            add_movie(movies)
        elif choice == 'W':
            mark_movie_watched(movies)
        elif choice == 'Q':
            save_movies(FILENAME, movies)
            print(f"{len(movies)} movies saved to {FILENAME}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def load_movies(filename):
    """Load movies from a CSV file into a list of [title, year, category, status]."""
    movies = []
    try:
        with open(filename, "r", encoding="utf-8") as in_file:
            reader = csv.reader(in_file)
            for row in reader:
                title, year, category, status = row
                movies.append([title, int(year), category, status])
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with an empty movie list.")
    return movies


def save_movies(filename, movies):
    """Save movies to a CSV file."""
    with open(filename, "w", newline='', encoding="utf-8") as out_file:
        writer = csv.writer(out_file)
        for movie in movies:
            writer.writerow([movie[0], movie[1], movie[2], movie[3]])


def display_movies(movies):
    """Display the list of movies, sorted by year then title, with watched/unwatched markers."""
    movies.sort(key=lambda x: (x[1], x[0]))
    count_watched = sum(1 for m in movies if m[3] == WATCHED)
    count_unwatched = len(movies) - count_watched
    for i, movie in enumerate(movies, start=1):
        mark = "*" if movie[3] == UNWATCHED else " "
        print(f"{i:2}. {mark} {movie[0]:35} - {movie[1]:4} ({movie[2]})")
    print(f"{count_watched} movies watched. {count_unwatched} movies still to watch.")


def add_movie(movies):
    """Prompt the user for movie details and add it to the list."""
    title = get_non_blank_input("Title: ")
    year = get_valid_number("Year: ", minimum=1)
    print(f"Categories available: {', '.join(CATEGORIES)}")
    category = get_non_blank_input("Category: ").title()
    if category not in CATEGORIES:
        print("Invalid category; using Other")
        category = "Other"
    movies.append([title, year, category, UNWATCHED])
    print(f"{title} ({category} from {year}) added to movie list")


def mark_movie_watched(movies):
    """Prompt the user to mark a movie as watched."""
    unwatched_movies = [m for m in movies if m[3] == UNWATCHED]
    if not unwatched_movies:
        print("No more movies to watch!")
        return

    display_movies(movies)
    while True:
        try:
            number = int(input("Enter the movie number to mark watched.\n>>> "))
            if number < 1:
                print("Number must be >= 1")
            elif number > len(movies):
                print("Invalid movie number.")
            else:
                if movies[number - 1][3] == WATCHED:
                    print(f"You have already watched {movies[number - 1][0]}.")
                else:
                    movies[number - 1][3] = WATCHED
                    print(f"{movies[number - 1][0]} ({movies[number - 1][1]}) watched.")
                break
        except ValueError:
            print("Invalid input; enter a valid number")


def get_non_blank_input(prompt):
    """Get non-blank input from the user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input can not be blank")


def get_valid_number(prompt, minimum=None):
    """Get a valid integer from the user with optional minimum check."""
    while True:
        try:
            number = int(input(prompt))
            if minimum is not None and number < minimum:
                print(f"Number must be >= {minimum}")
            else:
                return number
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == "__main__":
    main()
