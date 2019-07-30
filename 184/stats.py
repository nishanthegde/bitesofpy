from csv import DictReader
from os import path
from urllib.request import urlretrieve

DATA = path.join('/tmp', 'bite_output_log.txt')
if not path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        pass  # start here

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        pass

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        pass

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        pass

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        pass

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        pass

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        pass