from datetime import date
from datetime import timedelta

def get_next_date(weekday):
    today = date.today()
    # print(today.weekday())

    offset = (weekday - today.weekday() ) % 7
    next_date = today + timedelta(days=offset)
    return next_date.strftime(r"%y-%m-%d")


