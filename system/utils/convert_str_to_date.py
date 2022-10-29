from datetime import datetime
from system.Config import Config

def convert_str_to_date(date_string):
    return datetime.date(datetime.strptime(date_string,Config.UTC_String_Format))