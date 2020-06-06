from django import template

register = template.Library()


@register.filter(name='notify')
def notify(value):
    if int(value) == 10:
        return 'alert-primary'
    elif int(value) == 25:
        return 'alert-success'
    elif int(value) == 30:
        return 'alert-warning'
    elif int(value) == 40:
        return 'alert-danger'
    else:
        return 'alert-primary'
