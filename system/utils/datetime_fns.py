from system import Config
from datetime import datetime, date, timedelta
import calendar


def isInAppointmentRange(provided_date, slot_start , scheduled_day, starting_day, end_hour, req_specfic_week=None):
    return (
        is_valid_provided_date(provided_date, scheduled_day) and
        valid_specific_week(provided_date, scheduled_day, req_specfic_week) and
        after_booking_starts(provided_date, starting_day) and
        before_booking_ends(provided_date, end_hour , slot_start)
    )


def parse_date(provided_date):
    return datetime.strptime(provided_date, Config.UTC_String_Format)

def get_week_day(parsed_date):
    output_week = parsed_date.weekday()
    return  output_week+1 if(output_week>=0 and output_week<6) else 0

def is_valid_provided_date(provided_date, scheduled_day):
    # we are taking sunday as 0 but in date time sunday is 6. we need to change it
    output_week = get_week_day(parse_date(provided_date))
    return output_week == scheduled_day


def after_booking_starts(provided_date, starting_day):
    today = datetime.today()
    parsed_provided_date = parse_date(provided_date)
    delta = parsed_provided_date - today
    difference_days = delta.days
    return difference_days <= starting_day


def before_booking_ends(provided_date, end_hour , slot_start):
    parsed_provided_date = parse_date(provided_date)
    parsed_provided_date = datetime.combine(parsed_provided_date,slot_start)
    difference_time = parsed_provided_date - timedelta(hours=end_hour)
    return datetime.now() < difference_time


def valid_specific_week(provided_date, req_weekday, req_specfic_week=None):
    if (req_specfic_week == None):
        return True
    parsed_provided_date = parse_date(provided_date)
    calendar.setfirstweekday(calendar.SUNDAY)
    month = parsed_provided_date.month
    year = parsed_provided_date.year
    month_days = calendar.monthcalendar(year, month)
    week = month_days[req_specfic_week - 1]
    parsed_provided_date_day = parsed_provided_date.day
    return week[req_weekday] == parsed_provided_date_day

def get_weekdays_between_dates(start,end):
    data=[]
    parsed_start = parse_date(start)
    parsed_end = parse_date(end)

    cur = parsed_start

    while cur<parsed_end:
        data.append(get_week_day(cur))
        cur+=timedelta(days=1)
    return list(set(data))