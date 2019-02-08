from django import template
from django.utils import timezone

from datetime import date, timedelta

register = template.Library()

@register.filter
def display_date(value):
    """ Returns humanized date eg. 'Today at 11:01am' """
    current_time = timezone.now()
    today = current_time.date()
    value_date = value.date()
    if value_date == today:
        _date = "Today"
    elif value_date == (today - timedelta(1)):
        _date = "Yesterday"
    else:
        _date = value_date

    _time = value.time().strftime('%R')
    return f"{_date} at {_time}"
