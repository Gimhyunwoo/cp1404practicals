class Movie:
    """A class to represent a movie."""

    def __init__(self, title, year, category, is_watched=False):
        self.title = title
        self.year = int(year)
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        watched_mark = " " if self.is_watched else "*"
        return f"{watched_mark} {self.title:35} - {self.year:4} ({self.category})"

    def mark_watched(self):
        self.is_watched = True

    def mark_unwatched(self):
        self.is_watched = False

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "category": self.category,
            "is_watched": self.is_watched
        }

    @staticmethod
    def from_dict(data):
        return Movie(data["title"], data["year"], data["category"], data["is_watched"])
