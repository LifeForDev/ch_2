from django.core.exceptions import ValidationError

import datetime


def expireValid(value):
    if datetime.date.today() + datetime.timedelta(6*365/12) > value:
        raise ValidationError('Date must be early than 6 month')
