from abc import ABC, abstractmethod
from collections import namedtuple
from dataclasses import dataclass
from datetime import date
from os import getenv, getcwd
from pathlib import Path
from typing import Any, List, Optional
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup  # type: ignore

local = getcwd()
# local = '/tmp'
TMP = getenv("TMP", local)
TODAY = date.today()
Candidate = namedtuple("Candidate", "name votes")
LeaderBoard = namedtuple(
    "LeaderBoard", "Candidate Average Delegates Contributions Coverage"
)
Poll = namedtuple(
    "Poll",
    "Poll Date Sample Sanders Biden Gabbard Spread",
)


@dataclass
class File:
    """File represents a filesystem path.

    Variables:
        name: str -- The filename that will be created on the filesystem.
        file: Path -- Path object created from the name passed in.

    Methods:
        [property]
        data: -> Optional[str] -- If the file exists, it returns its contents.
            If it does not exists, it returns None.
    """

    def __init__(self, name: str):
        self.name = name
        self.path = Path("{}/{}_{}".format(TMP, TODAY, name))

    @property
    def data(self):
        if self.path.exists():
            with open(self.path) as f:
                return f.read()
        else:
            return None


@dataclass
class Web:
    """Web object.

    Web is an object that downloads the page from the url that is passed
    to it and stores it in the File instance that is passed to it. If the
    File already exists, it just reads the file, otherwise it downloads it
    and stores it in File.

    Variables:
        url: str -- The url of the web page.
        file: File -- The File object to store the page data into.

    Methods:
        [property]
        data: -> Optional[str] -- Reads the text from File or retrieves it from the
            web if it does not exists.

        [property]
        soup: -> Soup -- Parses the data from File and turns it into a BeautifulSoup
            object.
    """

    def __init__(self, url: str, file: File):
        self.url = url
        self.file = file

    @property
    def data(self) -> Optional[str]:
        """Reads the data from the File object.

        First it checks if the File object has any data. If it doesn't, it retrieves
        it and saves it to the File. Once the. It then reads it from the File and
        returns it.

        Returns:
            Optional[str] -- The string data from the File object.
        """
        if self.file.data:
            return self.file.data
        else:
            urlretrieve(self.url, self.file.path)
            with open(self.file.path) as f:
                return f.read()

    @property
    def soup(self) -> Soup:
        """Converts string data from File into a BeautifulSoup object.

        Returns:
            Soup -- BeautifulSoup object created from the File.
        """
        return Soup(self.data, 'html.parser')


class Site(ABC):
    """Site Abstract Base Class.

    Defines the structure for the objects based on this class and defines the interfaces
    that should implemented in order to work properly.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        [abstractmethod]
        parse_rows: -> Union[List[LeaderBoard], List[Poll]] -- Parses a BeautifulSoup
            table element and returns the text found in the td elements as
            namedtuples.

        [abstractmethod]
        polls: -> Union[List[LeaderBoard], List[Poll]] -- Does the parsing of the table
            and rows for you. It takes the table index number if given, otherwise
            parses table 0.

        [abstractmethod]
        stats: -- Formats the results from polls into a more user friendly
            representation.
    """

    def __init__(self, web: Web):
        self.web = web

    def find_table(self, loc: int = 0) -> str:
        """Finds the table elements from the Soup object

        Keyword Arguments:
            loc {int} -- Parses the Web object for table elements and
                returns the first one that it finds unless an integer representing
                the required table is passed. (default: {0})

        Returns:
            str -- The html table
        """
        tables = self.web.soup.findAll("table")

        if tables:
            return tables[loc]

    # @abstractmethod
    def parse_rows(self, table: Soup) -> List[Any]:
        """Abstract Method
        
        Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as NamedTuple.

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        tds = []
        rows = table.findAll('tr')
        for tr in rows:
            t = tuple(td.text for td in tr.findAll('td'))
            tds.append(t)

        return [t for t in tds if t]

    def polls(self, table: int = 0) -> List[Any]:
        """Abstract Method

        Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        t = self.find_table(table)
        return self.parse_rows(t)

    def stats(self, loc: int = 0):
        """Abstract Method
        
        Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        pass


@dataclass
class RealClearPolitics(Site):
    """RealClearPolitics object.

    RealClearPolitics is a custom class to parse a Web instance from the
    realclearpolitics website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[Poll] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as Poll namedtuples.

        polls: -> List[Poll] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            RealClearPolitics
            =================
                Biden: 214.0
                Sanders: 142.0
                Gabbard: 6.0

    """

    def __init__(self, web: Web):
        super().__init__(web)

    def parse_rows(self, table: Soup) -> List[Poll]:
        """Parses the row data from the html table.pytest

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as Poll namedtuples.

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        rows = super().parse_rows(table)
        return [Poll(r[0], r[1], r[2], float(r[4].replace('--', '0.0')), float(r[3].replace('--', '0.0')),
                     float(r[5].replace('--', '0.0')), r[6]) for r in rows[1:]]

    def polls(self, table: int = 0) -> List[Poll]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        return super().polls(table)

    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.

        """
        p = super().polls(loc)
        print("\n")
        print("RealClearPolitics")
        print("="*len("RealClearPolitics"))
        print("\n")

@dataclass
class NYTimes(Site):
    """NYTimes object.

    NYTimes is a custom class to parse a Web instance from the nytimes website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[LeaderBoard] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as LeaderBoard namedtuples.

        polls: -> List[LeaderBoard] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            NYTimes
            =================================

                               Pete Buttigieg
            ---------------------------------
            National Polling Average: 10%
                   Pledged Delegates: 25
            Individual Contributions: $76.2m
                Weekly News Coverage: 3

    """

    web: Web

    def __init__(self, web: Web):
        super().__init__(web)

    def parse_rows(self, table: Soup) -> List[LeaderBoard]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as LeaderBoard namedtuples.

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
            the table data.
        """
        rows = super().parse_rows(table)
        return [LeaderBoard(r[0].strip(), r[1], int(r[2]), r[3], int(r[4].replace('#',''))) for r in rows[:3]]


    def polls(self, table: int = 0) -> List[LeaderBoard]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
                the table data.
        """
        pass


    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        pass


def gather_data():
    rcp_file = File("realclearpolitics.html")
    rcp_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_realclearpolitics.html"
    )
    rcp_web = Web(rcp_url, rcp_file)
    rcp = RealClearPolitics(rcp_web)
    rcp.stats(3)

    nyt_file = File("nytimes.html")
    nyt_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_nytimes.html"
    )
    nyt_web = Web(nyt_url, nyt_file)
    nyt = NYTimes(nyt_web)
    nyt.stats()


def main():
    print("thank you for looking after my Mama...")
    # url = "https://projects.fivethirtyeight.com/polls/"
    # test_file = File("test.html")
    # test_web = Web(url, test_file)
    # print(type(test_web.soup))

    # file = File("clamytoe.html")
    # url = "https://clamytoe.dev"
    # test_web = Web(url, file)
    # print(test_web.data)

    rcp_file = File("realclearpolitics.html")
    rcp_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/"
        "2020-03-10_realclearpolitics.html"
    )
    rcp_web = Web(rcp_url, rcp_file)

    rcp = RealClearPolitics(rcp_web)
    rcp.stats(3)
    # table = r.find_table()
    # rows = r.parse_rows(table)
    # print(rows)

    # table = r.find_table()
    # rows = r.parse_rows(table)
    # poll = rows[0]
    # print(type(r.polls()))
    # assert isinstance(rows, list)
    # assert isinstance(poll, Poll)
    # assert isinstance(poll.Sanders, float)

    # nyt_file = File("nytimes.html")
    # nyt_url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
    #            "2020-03-10_nytimes.html")
    # nyt_web = Web(nyt_url, nyt_file)
    #
    # n = NYTimes(nyt_web)
    #
    # table = n.find_table()
    # rows = n.parse_rows(table)
    # leaderboard = rows[0]
    # print(leaderboard)
    # assert isinstance(rows, list)
    # assert isinstance(leaderboard, LeaderBoard)
    # assert isinstance(leaderboard.Delegates, int)
    # assert isinstance(leaderboard.Coverage, int)


if __name__ == "__main__":
    # gather_data()
    main()
