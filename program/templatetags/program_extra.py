from django.utils.timezone import datetime, timedelta
from django.template import Library

register = Library()


@register.filter
def currency_format(money):
    try:
        money = float(money)
    except(TypeError, ValueError):
        raise '<{} Not expected>'.format(money)
    return '{:,.2f}'.format(money)


@register.simple_tag
def date():
    yesterday = datetime.now() - timedelta(days=1)
    return str(yesterday).split()[0]
