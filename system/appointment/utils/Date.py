from marshmallow.fields import Field
import datetime as dt
from marshmallow import utils
class Date(Field):
    """ISO8601-formatted date string.

    :param kwargs: The same keyword arguments that :class:`Field` receives.
    """
    default_error_messages = {
        'invalid': 'Not a valid date.',
        'format': '"{input}" cannot be formatted as a date.',
    }

    def __init__(self, format=None, **kwargs):
        super(Date, self).__init__(**kwargs)
        self.dateformat = format

    def _serialize(self, value, attr, obj):
        if value is None:
            return None
        try:
            return value.isoformat()
        except AttributeError:
            self.fail('format', input=value)
        return value

    def _deserialize(self, value, attr, data,**kwargs):
        """Deserialize an ISO8601-formatted date string to a
        :class:`datetime.date` object.
        """
        if not value:  # falsy values are invalid
            self.fail('invalid')
        elif self.dateformat:
            try:
                return dt.datetime.strptime(value, self.dateformat).date()
            except (TypeError, AttributeError, ValueError):
                raise self.fail('invalid')
        try:
            return utils.from_iso_date(value)
        except (AttributeError, TypeError, ValueError):
            self.fail('invalid')