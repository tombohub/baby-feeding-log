from zoneinfo import ZoneInfo

from django.utils import timezone


def get_local_date():
    my_timezone = ZoneInfo("America/Toronto")
    return timezone.localdate(timezone=my_timezone)
