from django import template
from django.contrib import messages

register = template.Library()


@register.filter(name='notify')
def notify(value):
    if int(value) == 20:
        return 'alert-info'
    elif int(value) == 25:
        return 'alert-success'
    elif int(value) == 30:
        return 'alert-warning'
    elif int(value) == 40:
        return 'alert-error'
    else:
        return ''
