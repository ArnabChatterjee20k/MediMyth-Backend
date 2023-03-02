from system import Config
from datetime import datetime, date, timedelta
import calendar


def isInAppointmentRange(provided_date, slot_start , scheduled_day, starting_day, end_hour, req_specfic_week=None):
    print(
        is_valid_provided_date(provided_date, scheduled_day) ,
        valid_specific_week(provided_date, scheduled_day, req_specfic_week) ,
        after_booking_starts(provided_date, starting_day) ,
        before_booking_ends(provided_date, end_hour , slot_start)
    )
    return (
        is_valid_provided_date(provided_date, scheduled_day) and
        valid_specific_week(provided_date, scheduled_day, req_specfic_week) and
        after_booking_starts(provided_date, starting_day) and
        before_booking_ends(provided_date, end_hour , slot_start)
    )


def parse_date(provided_date):
    return datetime.strptime(provided_date, Config.UTC_String_Format)

def get_week_day(parsed_date):
    """
        returns -> value from 0 to 6 based on date
        .day of date object give us the date but we need week that is from 0 to 6
    """
    output_week = parsed_date.weekday()
    return  output_week+1 if(output_week>=0 and output_week<6) else 0

def is_valid_provided_date(provided_date, scheduled_day):
    # we are taking sunday as 0 but in date time sunday is 6. we need to change it
    output_week = get_week_day(parse_date(provided_date))
    return output_week == scheduled_day


def after_booking_starts(provided_date, starting_day):
    # use valid date function before using it
    # if the provided date is valid then the difference betweent the provided date and today should be <=starting day
    # to check whether we are apply after the slot or scheduled day use before booking end function
    today = datetime.today()
    parsed_provided_date = parse_date(provided_date)
    delta = parsed_provided_date - today
    difference_days = delta.days
    return difference_days <= starting_day


def before_booking_ends(provided_date, end_hour , slot_start):
    # use valid date function before using it
    parsed_provided_date = parse_date(provided_date)
    parsed_provided_date = datetime.combine(parsed_provided_date,slot_start)
    difference_time = parsed_provided_date - timedelta(hours=end_hour)
    print(difference_time,"and",datetime.now(),"and",datetime.now() < difference_time)
    return datetime.now() < difference_time


def valid_specific_week(provided_date, req_weekday, req_specfic_week=None):
    """
        provided_date is the appointment date that the user picks
        req_weekday is the week day that is specific week present in the schema
    """
    if (req_specfic_week == None):
        return True
    # print(provided_date, req_weekday)
    parsed_provided_date = parse_date(provided_date)
    calendar.setfirstweekday(calendar.SUNDAY)
    month = parsed_provided_date.month
    year = parsed_provided_date.year
    month_days = calendar.monthcalendar(year, month)
    week = month_days[req_specfic_week - 1]
    parsed_provided_date_day = parsed_provided_date.day
    print(parsed_provided_date.day,parsed_provided_date_day,week[req_weekday],req_weekday)
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