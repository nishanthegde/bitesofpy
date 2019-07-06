from datetime import datetime

BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')
PY2_RETIRED_DT = datetime.strptime('2020-04-12 00:00:00', '%Y-%m-%d %H:%M:%S')

def py2_earth_hours_left():
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth"""
    left = PY2_RETIRED_DT - BITE_CREATED_DT
    left_earth_hours = round(left.total_seconds()/3600,2)

    return left_earth_hours


def py2_miller_min_left():
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller"""
    left = PY2_RETIRED_DT - BITE_CREATED_DT
    left_earth_mins = round(left.total_seconds()/60,2)

    left_miller_hours = left_earth_mins/3679200
    left_miller_mins = round(left_miller_hours * 60,2) #assume that 1 miller hour is 60 miller mins (same as earth)

    return left_miller_mins

# def main():
#     """Imagine you landed on Planet Miller (from the movie Interstellar) where 1 hour takes 7 Earth years (known as the gravitational time dilation effect - see here if interested).

#     Given a fixed start date BITE_CREATED_DT calculate:

#     How many hours Python 2 has left on Planet Earth
#     How many minutes Python 2 has left on Planet Miller"""

#     print(BITE_CREATED_DT)
#     print(type(BITE_CREATED_DT))
#     print(PY2_RETIRED_DT)
#     print(type(PY2_RETIRED_DT))

#     print(py2_earth_hours_left())
#     print(py2_miller_min_left())

# if __name__ == "__main__":
#     main()
