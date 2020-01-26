import json
from dataclasses import dataclass
from datetime import datetime
from math import acos, cos, radians, sin
import os
from pathlib import Path
from urllib.request import urlretrieve

from dateutil.parser import parse

URL = "https://bites-data.s3.us-east-2.amazonaws.com/pycons-europe-2019.json"
RESPONSES = "https://bites-data.s3.us-east-2.amazonaws.com/nominatim_responses.json"

# tmp = Path(os.getcwd())
tmp = Path(os.getenv("TMP", "/tmp"))
pycons_file = tmp / "pycons-europe-2019.json"
nominatim_responses = tmp / "nominatim_responses.json"

if not pycons_file.exists() or not nominatim_responses.exists():
    urlretrieve(URL, pycons_file)
    urlretrieve(RESPONSES, nominatim_responses)


@dataclass
class PyCon:
    name: str
    city: str
    country: str
    start_date: datetime
    end_date: datetime
    URL: str
    lat: float = None
    lon: float = None


@dataclass
class Trip:
    origin: PyCon
    destination: PyCon
    distance: float


def _get_pycons():
    """Helper function that retrieves required PyCon data
       and returns a list of PyCon objects
    """
    with open(pycons_file, "r", encoding="utf-8") as f:
        return [
            PyCon(
                pycon["name"],
                pycon["city"],
                pycon["country"],
                parse(pycon["start_date"]),
                parse(pycon["end_date"]),
                pycon["url"],
            )
            for pycon in json.load(f)
        ]


def _km_distance(origin, destination) -> float:
    """ Helper function that retrieves the air distance in kilometers for two pycons """
    lon1, lat1, lon2, lat2 = map(
        radians, [origin.lon, origin.lat, destination.lon, destination.lat]
    )
    return 6371 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )


def update_pycons_lat_lon(pycons: list):
    """
    Update the latitudes and longitudes based on the city and country
    the PyCon takes places. Use requests from the Nominatim API stored in the
    nominatim_responses json file.
    """

    latlon = list()

    with open(nominatim_responses) as f:
        geo = json.load(f)

    for k, v in geo.items():
        latlon.append((k, v[0]['lat'], v[0]['lon']))

    for p in pycons:
        for l in latlon:
            if p.city.lower() in l[0].lower():
                p.lat = float(l[1])
                p.lon = float(l[2])


def create_travel_plan(pycons: list) -> list:
    """
    Create your travel plan to visit all the PyCons.
    Assume it's now the start of 2019!
    Return a list of Trips with each Trip containing the origin PyCon,
    the destination PyCon and the travel distance between the PyCons.
    """
    pycons = sorted(pycons, key=lambda x: x.start_date)
    travel_plan = list()
    for i in range(0, len(pycons) - 1):
        t = Trip(pycons[i], pycons[i + 1], _km_distance(pycons[i], pycons[i + 1]))
        travel_plan.append(t)

    return travel_plan


def total_travel_distance(journey: list) -> float:
    """
    Return the total travel distance of your PyCon journey in kilometers
    rounded to one decimal.
    """
    total_distance = 0
    for t in journey:
        total_distance += t.distance

    return round(total_distance, 1)


def main():
    print('thank you for the waves... ')
    pycons = _get_pycons()
    update_pycons_lat_lon(pycons)
    travel_plan = create_travel_plan(pycons)
    print(len(travel_plan))
    print(travel_plan[0].origin.name)
    print(travel_plan[0].destination.name)
    print(travel_plan[-1].origin.name)
    print(travel_plan[-1].destination.name)

    print(total_travel_distance(travel_plan))


if __name__ == '__main__':
    main()
