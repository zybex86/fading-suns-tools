import logging
from datetime import datetime

from django.conf import settings
from pytz import timezone


class TimezoneFormatter(logging.Formatter):
    """Custom timezone formatter"""

    def converter(self, timestamp):
        """Converts timestamt in utx to specific timezone"""
        utc_dt = datetime.fromtimestamp(timestamp)
        converted = utc_dt.astimezone(timezone(settings.LOGGING_TIME_ZONE))
        return converted.timetuple()
