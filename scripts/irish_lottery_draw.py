"""Python script to get the next Irish lottery draw.

    The Irish lottery draw takes place twice weekly on a Wednesday and a
Saturday  at 8pm. Write a function that calculates and returns the next
valid draw date based on the current date and time and also on an
optional supplied date.

Example: If we provide 2017-4-10 13:00 date (i.e Monday) the
script has to return 2017-4-12 20:00
"""
__author__ = 'me@kartheek.net (Karnati Kartheek)'

from datetime import datetime, timedelta


def next_draw_date(date=datetime.now()):
    """Function to get the next irish lottery draw date for current date or
    for the date provided.

    Checks the date (current/provided) against the conditions and calculates
    the day difference between the current and the next lottery date.

    Finally using the day difference value the next lottery date is created.

    Args:
        date: (datetime or current datetime)
    Returns:
        next draw date object

    """
    wed_weekday = 2
    sat_weekday = 5
    draw_hour = 20
    days_diff = 0

    if date.weekday() in [wed_weekday, sat_weekday] and date.hour < draw_hour:
        # provided date is next valid lottery date
        days_diff = 0
    elif date.weekday() < wed_weekday or date.weekday() >= sat_weekday:
        days_diff = (wed_weekday-date.weekday()) % 7
    elif date.weekday() > wed_weekday or date.weekday() < sat_weekday:
        days_diff = (sat_weekday-date.weekday()) % 7

    new_date = date+timedelta(days=days_diff)
    return new_date.replace(hour=20, minute=00, second=00, microsecond=00)
