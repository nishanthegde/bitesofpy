from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    if not day_of_year:
        day_of_year = datetime.now().timetuple().tm_yday

    rate = books_goal / 365

    return round((rate * day_of_year), 2) <= books_read
