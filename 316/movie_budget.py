from datetime import date
from typing import Dict, Sequence, NamedTuple


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def rent_or_stream(
        renting_history: RentingHistory,
        streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    rent_per_month = {}
    for movie in renting_history:
        if str(movie.date).rsplit('-', 1)[0] not in rent_per_month:
            rent_per_month[str(movie.date).rsplit('-', 1)[0]] = movie.price
        else:
            rent_per_month[str(movie.date).rsplit('-', 1)[0]] += movie.price

    for k, v in rent_per_month.items():
        if v <= STREAMING_COST_PER_MONTH:
            rent_per_month[k] = RENT
        else:
            rent_per_month[k] = STREAM

    return dict(sorted(rent_per_month.items()))

