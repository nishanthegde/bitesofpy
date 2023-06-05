import calendar
from datetime import date
from typing import Tuple

"""
Sample text if on-track:
Congratulations! You are on track with your steps goal. The target for 2023-01-12 is 164,383 steps and you are 11 ahead.

Sample text if not on track:
You have some catching up to do! The target for 2023-09-30 is 27,300 pages read and you are 2 behind.
"""


def goal_tracker(
    desc: str, annual_target: int, current_score: int, score_date: Tuple[int, int, int]
):
    """Return a string determining whether a goal is on track
    by calculating the current target and comparing it with the current achievement.
    The function assumes the goal is to be achieved in a calendar year. Think New Year's Resolution :)
    """
    try:
        sd = date(score_date[0], score_date[1], score_date[2])
    except ValueError:
        print("Score Date is not valid")

    # number of days delta
    days_delta = (sd - date(score_date[0], 1, 1)).days + 1

    # target daily rate
    if score_date[0] % 4 == 0:
        tgt_daily_rate = annual_target / 366
    else:
        tgt_daily_rate = annual_target / 365

    # target score
    tgt_score = int(tgt_daily_rate * days_delta)

    if current_score >= tgt_score:
        return f"Congratulations! You are on track with your {desc} goal. The target for {sd} is {format(tgt_score,',')} {desc} and you are {format(current_score-tgt_score,',')} ahead."
    else:
        return f"You have some catching up to do! The target for {sd} is {format(tgt_score,',')} {desc} and you are {format(tgt_score-current_score,',')} behind."
